'''
	Hospital Patient Records Management System in Python with SQLite
'''

import sqlite3

def prepare_db():
	conn = sqlite3.connect("hospital.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Patient` (
		`id` integer primary key NOT NULL UNIQUE,
		`name` TEXT NOT NULL,
		`insurance_provider` TEXT,
		`insurance_id` INTEGER,
		`dob` REAL NOT NULL,
		`contact_number` INTEGER NOT NULL,
		`email_id` TEXT NOT NULL,
		`sex_at_birth` TEXT NOT NULL,
		`active_status` INTEGER NOT NULL DEFAULT '1',
		`address` TEXT
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Nurse` (
		`id` integer primary key NOT NULL UNIQUE,
		`name` TEXT NOT NULL,
		`contact_number` INTEGER NOT NULL,
		`email_id` TEXT NOT NULL,
		`address` TEXT NOT NULL
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Medicine` (
		`id` integer primary key NOT NULL UNIQUE,
		`brand_name` TEXT NOT NULL,
		`contents` TEXT NOT NULL,
		`dosage` INTEGER NOT NULL,
		`additional_notes` TEXT
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Department` (
		`id` integer primary key NOT NULL UNIQUE,
		`title` TEXT NOT NULL,
		`number_of_physicians` INTEGER NOT NULL
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Procedure` (
		`id` integer primary key NOT NULL UNIQUE,
		`name` TEXT NOT NULL,
		`details` TEXT
     )''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Physician` (
		`id` integer primary key NOT NULL UNIQUE,
		`name` TEXT NOT NULL,
		`department_id` INTEGER NOT NULL,
		`position` TEXT NOT NULL,
		`contact_number` INTEGER NOT NULL,
		`email_id` TEXT NOT NULL,
		`nurse_assigned_id` INTEGER,
		`address` TEXT NOT NULL,
	FOREIGN KEY(`department_id`) REFERENCES `Department`(`id`),
	FOREIGN KEY(`nurse_assigned_id`) REFERENCES `Nurse`(`id`)
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Head` (
		`id` integer primary key NOT NULL UNIQUE,
		`dept_id` INTEGER NOT NULL,
		`physician_id` INTEGER NOT NULL,
		FOREIGN KEY(`dept_id`) REFERENCES `Department`(`id`),
		FOREIGN KEY(`physician_id`) REFERENCES `Physician`(`id`)
	)''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Record` (
		`id` integer primary key NOT NULL UNIQUE,
		`time_of_meeting` REAL,
		`procedure_id` INTEGER,
		`patient_id` INTEGER NOT NULL,
		`physician_id` INTEGER NOT NULL,
		`condition` TEXT NOT NULL,
		`remedy` TEXT,
		`height` REAL,
		`weight` REAL,
		`bp` REAL,
		`medicine_prescribed_id` INTEGER,
	FOREIGN KEY(`procedure_id`) REFERENCES `Procedure`(`id`),
	FOREIGN KEY(`patient_id`) REFERENCES `Patient`(`id`),
	FOREIGN KEY(`physician_id`) REFERENCES `Physician`(`id`),
	FOREIGN KEY(`medicine_prescribed_id`) REFERENCES `Medicine`(`id`)
	);''')
	conn.commit()
	cursor.execute('''CREATE TABLE IF NOT EXISTS `Physician_Procedure` (
		`id` integer primary key NOT NULL UNIQUE,
		`physician_id` INTEGER NOT NULL,
		`procedure_id` INTEGER NOT NULL,
	FOREIGN KEY(`physician_id`) REFERENCES `Physician`(`id`),
	FOREIGN KEY(`procedure_id`) REFERENCES `Procedure`(`id`)
      )''')
	conn.commit()
