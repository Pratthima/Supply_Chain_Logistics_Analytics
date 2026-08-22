-- ============================================================
-- SUPPLY CHAIN & LOGISTICS ANALYTICS
-- DATABASE SETUP
-- ============================================================

-- Create database
CREATE DATABASE IF NOT EXISTS supply_chain_db;

-- Select database
USE supply_chain_db;


-- ============================================================
-- CREATE MAIN TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS supply_chain (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE,

    Product_ID VARCHAR(20),
    Product_Name VARCHAR(100),
    Product_Category VARCHAR(100),

    Supplier_ID VARCHAR(20),
    Supplier_Name VARCHAR(100),
    Supplier_Rating DECIMAL(3,2),

    Warehouse_ID VARCHAR(20),
    Warehouse_Name VARCHAR(100),
    Warehouse_Utilization DECIMAL(5,2),

    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Order_Value DECIMAL(15,2),

    Shipping_Mode VARCHAR(50),
    Shipping_Cost DECIMAL(12,2),

    Origin VARCHAR(100),
    Destination VARCHAR(100),

    Expected_Delivery_Date DATE,
    Actual_Delivery_Date DATE,

    Delivery_Status VARCHAR(50),
    Delivery_Delay_Days INT,

    Inventory_Level INT,
    Reorder_Level INT,
    Inventory_Status VARCHAR(50),

    Inventory_Risk VARCHAR(50),
    Overall_Risk VARCHAR(50),
    Delay_Category VARCHAR(50),

    Order_Year INT,
    Order_Month INT
);


-- ============================================================
-- VERIFY TABLE
-- ============================================================

DESCRIBE supply_chain;