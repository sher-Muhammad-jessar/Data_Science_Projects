create database Pharmacy_inventory_system;
use Pharmacy_inventory_system;
CREATE TABLE Pharmacy_Inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    medication_code VARCHAR(20),
    medication_name VARCHAR(100),
    supplier VARCHAR(100),
    stock_level INT,
    dispensing_visit_id VARCHAR(50),
    dispensing_date DATE
);

use Pharmacy_inventory_system;
select * from Pharmacy_Inventory;