import sqlite3
from db_prep import prepare_db

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()


class Hospital:
    def __init__():
        prepare_db()

    def register_patient(
        name,
        insurance_provider,
        insurance_id,
        dob,
        contact_num,
        email_id,
        sex_at_birth,
        address,
        active_status=True,
    ):
        cursor.execute(
            '''INSERT INTO Patient (name, 
                       dob, contact_number, email_id, sex_at_birth, active_status, 
                       address,  insurance_provider=None, insurance_id=None) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                name,
                insurance_provider,
                insurance_id,
                dob,
                contact_num,
                email_id,
                sex_at_birth,
                active_status,
                address,
            ),
        )
        conn.commit()

    def book_appointment(time_booked, patient_id, physician_id, condition):
        cursor.execute(
            '''INSERT INTO Record (time_of_meeting, patient_id,
                       physician_id, condition) VALUES (?, ?, ?, ?)''',
            (time_booked, patient_id, physician_id, condition),
        )
        conn.commit()

    def meet_with_patient(booking_id, remedy, height, weight, bp, procedure_id=None):
        cursor.execute(
            '''UPDATE Record SET remedy = ?, height = ?, weight = ?, bp = ?,
                       procedure_id = ?
                       WHERE id = ?''',
            (
                remedy,
                height,
                weight,
                bp,
                procedure_id,
                booking_id,
            ),
        )
        conn.commit()

    def hire_physician(
        name,
        dept_id,
        position,
        contact_number,
        email_id,
        address,
        nurse_assigned_id=None,
    ):
        cursor.execute(
            '''INSERT INTO Physician (name, department_id,
                       position, contact_number, email_id, nurse_assigned_id,
                       address) VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (
                name,
                dept_id,
                position,
                contact_number,
                email_id,
                nurse_assigned_id,
                address,
            ),
        )
        conn.commit()

    def promote_to_hod(physician_id, dept_id):
        cursor.execute(
            '''INSERT INTO Head (dept_id, physician_id)
                       VALUES (?, ?)''',
            (dept_id, physician_id),
        )
        conn.commit()

    def prescribe_medicine(booking_id, medicine_prescribed_id):
        cursor.execute(
            '''UPDATE Record SET medicine_prescribed_id = ?
            WHERE id = ?''',
            (medicine_prescribed_id, booking_id),
        )
        conn.commit()

    def cancel_appointment(booking_id):
        cursor.execute(
            '''DELETE * FROM Record WHERE id = ?''',
            (booking_id),
        )
        conn.commit()

    def hire_nurse(name, contact_number, email_id, address):
        cursor.execute(
            '''INSERT INTO Nurse (name, contact_number, email_id, address)
            VALUES (?, ?, ?, ?)''',
            (name, contact_number, email_id, address),
        )
        conn.commit()

    def assign_nurse(nurse_id, physician_id):
        cursor.execute(
            '''UPDATE Physician SET nurse_assigned_id = ? WHERE id = ?''',
            (nurse_id, physician_id),
        )
        conn.commit()

    def update_patient(
        patient_id,
        dob=None,
        contact_number=None,
        email_id=None,
        active_status=None,
        address=None,
        insurance_provider=None,
        insurance_id=None,
    ):
        cursor.execute(
            '''UPDATE Patient SET dob = coalesce(?, dob), 
                       contact_number = coalesce(?, contact_number), 
                       email_id = coalesce(?, email_id),
                       active_status = coalesce(?, active_status), 
                       address = coalesce(?, address), 
                       insurance_provider = coalesce(?, insurance_provider),
                       insurance_id = coalesce(?, insurance_id)
                       WHERE id = ?''',
            (
                dob,
                contact_number,
                email_id,
                active_status,
                address,
                insurance_provider,
                insurance_id,
            ),
        )
        conn.commit()

    def update_physician(
        physician_id,
        dept_id=None,
        position=None,
        contact_number=None,
        email_id=None,
        address=None,
        nurse_assigned_id=None,
    ):
        cursor.execute(
            '''UPDATE Physician SET dept_id = coalesce(?, dept_id),
                       position = coalesce(?, position), 
                       contact_number = coalesce(?, contact_number),
                       email_id = coalesce(?, email_id),
                       address = coalesce(?, address),
                       nurse_assigned_id = coalesce(?, nurse_assigned_id) WHERE
                       id = ?''',
            (
                dept_id,
                position,
                contact_number,
                email_id,
                address,
                nurse_assigned_id,
                physician_id,
            ),
        )
        conn.commit()

    def update_nurse(nurse_id, contact_number, email_id, address):
        cursor.execute(
            '''UPDATE Nurse SET  
                       contact_number = coalesce(?, contact_number),
                       email_id = coalesce(?, email_id),
                       address = coalesce(?, address),
                       WHERE
                       id = ?''',
            (contact_number, email_id, address, nurse_id),
        )
        conn.commit()

    def qualify_physician_for_a_procedure(physician_id, procedure_id):
        cursor.execute(
            '''INSERT INTO Physician_Procedure 
                       (physician_id, procedure_id) VALUES (?, ?)''',
            (physician_id, procedure_id),
        )
        conn.commit()
