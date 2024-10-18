CREATE TABLE IF NOT EXISTS `Patient` (
	`id` integer primary key NOT NULL UNIQUE,
	`name` TEXT NOT NULL,
	`insurance_provider` TEXT,
	`insurance_id` INTEGER,
	`dob` REAL NOT NULL,
	`contact_number` INTEGER NOT NULL,
	`email_id` TEXT NOT NULL,
	`sex_at_birth` TEXT NOT NULL,
	`active_status` INTEGER NOT NULL DEFAULT '1'
);
CREATE TABLE IF NOT EXISTS `Record` (
	`id` integer primary key NOT NULL UNIQUE,
	`patient_id` INTEGER NOT NULL,
	`physician_id` INTEGER NOT NULL,
	`condition` TEXT NOT NULL,
	`remedy` TEXT NOT NULL,
	`height` REAL NOT NULL,
	`weight` REAL NOT NULL,
	`bp` REAL NOT NULL,
	`medicine_prescribed_id` INTEGER NOT NULL,
FOREIGN KEY(`patient_id`) REFERENCES `Patient`(`id`),
FOREIGN KEY(`physician_id`) REFERENCES `Physician`(`id`),
FOREIGN KEY(`medicine_prescribed_id`) REFERENCES `Medicine`(`id`)
);
CREATE TABLE IF NOT EXISTS `Physician` (
	`id` integer primary key NOT NULL UNIQUE,
	`name` TEXT NOT NULL,
	`department_id` INTEGER NOT NULL,
	`position` TEXT NOT NULL,
	`contact_number` INTEGER NOT NULL,
	`email_id` TEXT NOT NULL,
	`nurse_assigned_id` INTEGER NOT NULL,
	`address` TEXT NOT NULL,
FOREIGN KEY(`department_id`) REFERENCES `Department`(`id`),
FOREIGN KEY(`nurse_assigned_id`) REFERENCES `Nurse`(`id`),
);
CREATE TABLE IF NOT EXISTS `Department` (
	`id` integer primary key NOT NULL UNIQUE,
	`title` TEXT NOT NULL,
	`number_of_physicians` INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `Head` (
	`id` integer primary key NOT NULL UNIQUE,
	FOREIGN KEY(`dept_id`) REFERENCES `Department`(`id`),
	FOREIGN KEY(`physician_id`) REFERENCES `Physician`(`id`)
)
CREATE TABLE IF NOT EXISTS `Nurse` (
	`id` integer primary key NOT NULL UNIQUE,
	`name` TEXT NOT NULL,
	`contact_number` INTEGER NOT NULL,
	`email_id` TEXT NOT NULL,
	`address` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Medicine` (
	`id` integer primary key NOT NULL UNIQUE,
	`brand_name` TEXT NOT NULL,
	`contents` TEXT NOT NULL,
	`dosage` INTEGER NOT NULL
);