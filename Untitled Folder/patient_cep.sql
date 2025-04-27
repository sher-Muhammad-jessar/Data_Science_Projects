 create database patient;

CREATE TABLE Patient_Records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id VARCHAR(50),
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    visit_date DATE,
    diagnosis_code VARCHAR(10),     -- ICD-10 format
    treatment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
use patient;
SELECT * from Patient_Records ;
 show databases;