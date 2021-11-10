create database LPG;
use LPG;
create table customers (Customer_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(50) NOT NULL, Address VARCHAR(100) NOT NULL, Phone_No VARCHAR(20) NOT NULL, Email VARCHAR(50), ID_Proof VARCHAR(50) NOT NULL, ID_Proof_No VARCHAR(50) NOT NULL, Last_issued_date DATE , Username VARCHAR(50) NOT NULL, Password VARCHAR(50) NOT NULL);