-- Create database
CREATE DATABASE datawarehouse_medical;
USE datawarehouse_medical;

-- -----------------------------------------
-- Step 1: Creating the Dimension Tables
-- -----------------------------------------

-- Date Dimension Table
CREATE TABLE Date_Dimension (
    DateID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE NOT NULL,
    Day INT NOT NULL,
    Month INT NOT NULL,
    Year INT NOT NULL,
    Quarter INT NOT NULL
);

-- Patient Dimension Table
CREATE TABLE Patient_Dimension (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(50) NOT NULL
);

-- Disease Dimension Table
CREATE TABLE Disease_Dimension (
    DiseaseCode VARCHAR(10) PRIMARY KEY,
    DiseaseName VARCHAR(255) NOT NULL
);

-- Zip Code Dimension Table (Region)
CREATE TABLE ZipCode_Dimension (
    ZipCode VARCHAR(10) PRIMARY KEY,
    Region VARCHAR(255)
);

-- Medication Dimension Table
CREATE TABLE Medication_Dimension (
    MedicationID INT PRIMARY KEY AUTO_INCREMENT,
    MedicationName VARCHAR(255) NOT NULL
);

-- -----------------------------------------
-- Step 2: Creating the Fact Tables
-- -----------------------------------------

-- Fact Table: Patient Visits
CREATE TABLE Fact_Patient_Visits (
    VisitID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    DateID INT,
    DiagnosisCode VARCHAR(10),
    Treatment VARCHAR(255),
    FOREIGN KEY (PatientID) REFERENCES Patient_Dimension(PatientID),
    FOREIGN KEY (DateID) REFERENCES Date_Dimension(DateID)
);

-- Fact Table: Hospital Billing
CREATE TABLE Fact_Hospital_Billing (
    BillingID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    DateID INT,
    ProcedureCost DECIMAL(10,2),
    MedicationCost DECIMAL(10,2),
    InsuranceClaim DECIMAL(10,2),
    FOREIGN KEY (PatientID) REFERENCES Patient_Dimension(PatientID),
    FOREIGN KEY (DateID) REFERENCES Date_Dimension(DateID)
);

-- Fact Table: Pharmacy Inventory
CREATE TABLE Fact_Pharmacy_Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    MedicationID INT,
    DateID INT,
    StockLevel INT,
    FOREIGN KEY (MedicationID) REFERENCES Medication_Dimension(MedicationID),
    FOREIGN KEY (DateID) REFERENCES Date_Dimension(DateID)
);

-- ✅ FIXED Fact Table: Disease Outbreaks (Using DateID instead of OutbreakDate)
CREATE TABLE Fact_Disease_Outbreaks (
    OutbreakID INT PRIMARY KEY AUTO_INCREMENT,
    DiseaseCode VARCHAR(10),
    ZipCode VARCHAR(10),
    DateID INT,
    NumberOfCases INT,
    FOREIGN KEY (DiseaseCode) REFERENCES Disease_Dimension(DiseaseCode),
    FOREIGN KEY (ZipCode) REFERENCES ZipCode_Dimension(ZipCode),
    FOREIGN KEY (DateID) REFERENCES Date_Dimension(DateID)
);

-- -----------------------------------------
-- Sample Queries
-- -----------------------------------------

-- Query 1: Average Treatment Cost by Gender, Age Group, and Diagnosis
SELECT 
    pd.Gender,
    CASE 
        WHEN pd.Age BETWEEN 0 AND 18 THEN '0-18'
        WHEN pd.Age BETWEEN 19 AND 35 THEN '19-35'
        WHEN pd.Age BETWEEN 36 AND 60 THEN '36-60'
        ELSE '60+'
    END AS Age_Group,
    fpv.DiagnosisCode,
    ROUND(AVG(fhb.ProcedureCost + fhb.MedicationCost), 2) AS Avg_Treatment_Cost
FROM Fact_Hospital_Billing fhb
JOIN Patient_Dimension pd ON fhb.PatientID = pd.PatientID
JOIN Fact_Patient_Visits fpv ON fhb.PatientID = fpv.PatientID
GROUP BY pd.Gender, Age_Group, fpv.DiagnosisCode;

-- Query 2: Medication Stock Status
SELECT 
    md.MedicationName,
    fpi.StockLevel,
    CASE 
        WHEN fpi.StockLevel < 100 THEN '⚠️ Low Stock - Replenishment Needed'
        WHEN fpi.StockLevel BETWEEN 100 AND 300 THEN 'Normal'
        ELSE 'High Stock'
    END AS Replenishment_Status
FROM Fact_Pharmacy_Inventory fpi
JOIN Medication_Dimension md ON fpi.MedicationID = md.MedicationID;

-- Query 3: Disease Outbreak and Visit Analysis by Year and Region
SELECT 
    dd.Year,
    zd.Region,
    ddo.DiseaseCode,
    SUM(ddo.NumberOfCases) AS Outbreak_Cases,
    COUNT(fpv.VisitID) AS Hospital_Visits
FROM Fact_Disease_Outbreaks ddo
JOIN ZipCode_Dimension zd ON ddo.ZipCode = zd.ZipCode
JOIN Date_Dimension dd ON ddo.DateID = dd.DateID
JOIN Fact_Patient_Visits fpv ON fpv.DateID = dd.DateID
JOIN Patient_Dimension pd ON fpv.PatientID = pd.PatientID
WHERE zd.Region IS NOT NULL
GROUP BY dd.Year, zd.Region, ddo.DiseaseCode
ORDER BY dd.Year;

-- -----------------------------------------
-- View All Records from Fact Tables
-- -----------------------------------------
SELECT * FROM Fact_Patient_Visits;
SELECT * FROM Fact_Hospital_Billing;
SELECT * FROM Fact_Pharmacy_Inventory;
SELECT * FROM Fact_Disease_Outbreaks;
