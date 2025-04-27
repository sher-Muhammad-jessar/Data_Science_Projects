create database Hospital_Billing_System;

CREATE TABLE Hospital_Billing (
    billing_id INT PRIMARY KEY AUTO_INCREMENT,
    visit_id VARCHAR(50),
    patient_id VARCHAR(50),
    billing_date VARCHAR(20), -- Stored as text due to inconsistent formats
    procedure_cost DECIMAL(10, 2),
    medication_cost DECIMAL(10, 2),
    insurance_claim DECIMAL(10, 2)
);
 use Hospital_Billing_System;
 select * from Hospital_Billing;
