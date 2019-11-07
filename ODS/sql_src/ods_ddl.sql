-- Drop database CMS if exists

CREATE DATABASE ODS;
USE ODS;

-- Delete the schemas

DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Cart;
DROP TABLE IF EXISTS Delivery;
DROP TABLE IF EXISTS Delivery_Executive;

-- Create the schemas

CREATE TABLE Customer (
    Customer_ID     CHAR(6),
    First_name      VARCHAR(20),
    Last_name       VARCHAR(20),
    Email           VARCHAR(40),
    Password        VARCHAR(20),
    Phone1          CHAR(10),
    Phone2          CHAR(10),
    CONSTRAINT Customer_ID_FMT CHECK (Customer_ID REGEXP "^C[0-9]{5}$"),
	CONSTRAINT Customer_Email_FMT CHECK (Email REGEXP "^[a-zA-Z0-9_]{1,20}\.?[a-zA-Z0-9_]{0,5}@[a-z]{1,7}(\.com|\.ac\.in)$"),
    CONSTRAINT Customer_Password_FMT CHECK (Password REGEXP "^[a-zA-Z0-9@#&!\$]{8,20}$"),
    CONSTRAINT Customer_Phone1_FMT CHECK (Phone1 REGEXP "^[0-9]{10}$"),
    CONSTRAINT Customer_Phone2_FMT CHECK (Phone2 REGEXP "^[0-9]{10}$"),
    CONSTRAINT Customer_PK PRIMARY KEY (Customer_ID)
);

CREATE TABLE Address (
    Customer_ID     CHAR(6),
    Address_ID      CHAR(6),
    Pincode         CHAR(6),
    Street          VARCHAR(20),
    Landmark        VARCHAR(20),
    City            VARCHAR(20),
    State           VARCHAR(20),
    Type            ENUM ("Work", "Home"),
    CONSTRAINT Address_ID_FMT CHECK (Address_ID REGEXP "^[0-9]{6}$"),
    CONSTRAINT Pincode_FMT CHECK (Pincode REGEXP "^[0-9]{6}$"),
    CONSTRAINT Address_FK FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID) ON DELETE CASCADE,
    CONSTRAINT Address_PK PRIMARY KEY (Customer_ID, Address_ID)
);

CREATE TABLE Orders (
    Order_ID            CHAR(10),
    Customer_ID         CHAR(6),
    Address_ID          CHAR(6),
    Total_Price         NUMERIC(6, 0) UNSIGNED DEFAULT 0,
    Payment_Method      ENUM ("Cash On Delivery", "Debit Card", "Credit Card", "Net Banking"),
    Status              ENUM ("Delivered", "Not Delivered"),
    Order_Date          TIMESTAMP, 
    CONSTRAINT Orders_ID_FMT CHECK (Order_ID REGEXP "^[A-Z]{2}-[0-9]{7}$"),
    CONSTRAINT Orders_Total_Price CHECK (Total_Price >= 0),
    CONSTRAINT Orders_PK PRIMARY KEY (Order_ID),
    CONSTRAINT Orders_FK FOREIGN KEY (Customer_ID, Address_ID) REFERENCES Address (Customer_ID, Address_ID) ON DELETE CASCADE
);

CREATE TABLE Delivery_Executive (
    ID              CHAR(6),
    First_name      VARCHAR(20),
    Last_name       VARCHAR(20),
    Email           VARCHAR(40),
    Password        VARCHAR(20),
    WorkTime        ENUM ("Full-Time", "Part-Time"),
    Salary          NUMERIC(6, 0) UNSIGNED DEFAULT 0,
    Phone1          CHAR(10),
    Phone2          CHAR(10),
    CONSTRAINT Delivery_Executive_ID_FMT CHECK (ID REGEXP "^D[0-9]{5}$"),
    CONSTRAINT Delivery_Executive_Email_FMT CHECK (Email REGEXP "^[a-zA-Z0-9_]{1,20}\.?[a-zA-Z0-9_]{0,5}@[a-z]{1,7}(\.com|\.ac\.in)$"),
    CONSTRAINT Delivery_Executive_Password_FMT CHECK (Password REGEXP "^[a-zA-Z0-9@#&!\$]{8, 20}$"),
    CONSTRAINT Delivery_Executive_Salary CHECK (Salary >= 0),
    CONSTRAINT Delivery_Executive_Phone1_FMT CHECK (Phone1 REGEXP "^[0-9]{10}$"),
    CONSTRAINT Delivery_Executive_Phone2_FMT CHECK (Phone2 REGEXP "^[0-9]{10}$"),
    CONSTRAINT Delivery_Executive_PK PRIMARY KEY (ID)
);

CREATE TABLE Delivery (
    Order_ID        CHAR(10), 
    ID              CHAR(6),
    CONSTRAINT Delivery_FK_1 FOREIGN KEY (Order_ID) REFERENCES Orders (Order_ID) ON DELETE CASCADE,
    CONSTRAINT Delivery_FK_2 FOREIGN KEY (ID) REFERENCES Delivery_Executive (ID) ON DELETE CASCADE,
    CONSTRAINT Delivery_PK PRIMARY KEY (Order_ID, ID)
);

CREATE TABLE Product (
    Product_ID      CHAR(10),
    Name            VARCHAR(20),
    Category        VARCHAR(20),
    Price           NUMERIC(6, 0) UNSIGNED DEFAULT 0,
    Rating          NUMERIC(2, 1) UNSIGNED DEFAULT 0,
    Seller          VARCHAR(20),
    Availability    ENUM ("In-Stock", "Out-Of-Stock"),
    CONSTRAINT Product_ID_FMT CHECK (Product_ID REGEXP "^[A-Z]{3}-[0-9]{6}$"),
    CONSTRAINT Product_Price CHECK (Price >= 0),
    CONSTRAINT Product_Rating CHECK (Rating >= 0 and Rating <= 5),
    CONSTRAINT Product_PK PRIMARY KEY (Product_ID)
);

CREATE TABLE Cart (
    Customer_ID     CHAR(6),
    Prod_ID1        CHAR(6),
    Prod_ID2        CHAR(6),
    Prod_ID3        CHAR(6),
    Prod_ID4        CHAR(6),
    Prod_ID5        CHAR(6),
    CONSTRAINT Cart_Customer_ID_FK FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID) ON DELETE CASCADE,
    CONSTRAINT Cart_Prod_ID1_FK FOREIGN KEY (Prod_ID1) REFERENCES Product (Product_ID) ON DELETE SET NULL,
    CONSTRAINT Cart_Prod_ID2_FK FOREIGN KEY (Prod_ID2) REFERENCES Product (Product_ID) ON DELETE SET NULL,
    CONSTRAINT Cart_Prod_ID3_FK FOREIGN KEY (Prod_ID3) REFERENCES Product (Product_ID) ON DELETE SET NULL,
    CONSTRAINT Cart_Prod_ID4_FK FOREIGN KEY (Prod_ID4) REFERENCES Product (Product_ID) ON DELETE SET NULL,
    CONSTRAINT Cart_Prod_ID5_FK FOREIGN KEY (Prod_ID5) REFERENCES Product (Product_ID) ON DELETE SET NULL,
    CONSTRAINT Customer_PK PRIMARY KEY (Customer_ID)
);
