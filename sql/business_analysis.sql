USE supply_chain_db;

-- ============================================================
-- 1. TOTAL ORDERS
-- ============================================================

SELECT
    COUNT(*) AS Total_Orders
FROM supply_chain;


-- ============================================================
-- 2. TOTAL REVENUE
-- ============================================================

SELECT
    ROUND(SUM(Order_Value), 2) AS Total_Revenue
FROM supply_chain;


-- ============================================================
-- 3. TOTAL SHIPPING COST
-- ============================================================

SELECT
    ROUND(SUM(Shipping_Cost), 2) AS Total_Shipping_Cost
FROM supply_chain;


-- ============================================================
-- 4. AVERAGE ORDER VALUE
-- ============================================================

SELECT
    ROUND(AVG(Order_Value), 2) AS Average_Order_Value
FROM supply_chain;


-- ============================================================
-- 5. DELIVERY PERFORMANCE
-- ============================================================

SELECT
    Delivery_Status,
    COUNT(*) AS Total_Orders,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM supply_chain),
        2
    ) AS Percentage
FROM supply_chain
GROUP BY Delivery_Status;


-- ============================================================
-- 6. TOTAL DELAYED ORDERS
-- ============================================================

SELECT
    COUNT(*) AS Delayed_Orders
FROM supply_chain
WHERE Delivery_Status = 'Delayed';


-- ============================================================
-- 7. AVERAGE DELIVERY DELAY
-- ============================================================

SELECT
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay_Days
FROM supply_chain;


-- ============================================================
-- 8. SHIPPING MODE PERFORMANCE
-- ============================================================

SELECT
    Shipping_Mode,
    COUNT(*) AS Total_Shipments,
    ROUND(SUM(Shipping_Cost), 2) AS Total_Shipping_Cost,
    ROUND(AVG(Shipping_Cost), 2) AS Average_Shipping_Cost,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM supply_chain
GROUP BY Shipping_Mode
ORDER BY Total_Shipping_Cost DESC;


-- ============================================================
-- 9. SUPPLIER PERFORMANCE
-- ============================================================

SELECT
    Supplier_Name,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Supplier_Rating), 2) AS Average_Rating,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay,
    ROUND(SUM(Order_Value), 2) AS Total_Order_Value
FROM supply_chain
GROUP BY Supplier_Name
ORDER BY Average_Delay DESC;


-- ============================================================
-- 10. TOP PRODUCTS BY REVENUE
-- ============================================================

SELECT
    Product_Name,
    Product_Category,
    COUNT(*) AS Number_of_Orders,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Order_Value), 2) AS Total_Revenue
FROM supply_chain
GROUP BY Product_Name, Product_Category
ORDER BY Total_Revenue DESC
LIMIT 10;


-- ============================================================
-- 11. PRODUCT CATEGORY PERFORMANCE
-- ============================================================

SELECT
    Product_Category,
    COUNT(*) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Order_Value), 2) AS Total_Revenue
FROM supply_chain
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;


-- ============================================================
-- 12. INVENTORY STATUS
-- ============================================================

SELECT
    Inventory_Status,
    COUNT(*) AS Total_Products,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM supply_chain),
        2
    ) AS Percentage
FROM supply_chain
GROUP BY Inventory_Status;


-- ============================================================
-- 13. INVENTORY RISK
-- ============================================================

SELECT
    Inventory_Risk,
    COUNT(*) AS Total_Records
FROM supply_chain
GROUP BY Inventory_Risk
ORDER BY Total_Records DESC;


-- ============================================================
-- 14. WAREHOUSE PERFORMANCE
-- ============================================================

SELECT
    Warehouse_Name,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Warehouse_Utilization), 2) AS Average_Utilization,
    ROUND(SUM(Order_Value), 2) AS Total_Revenue,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM supply_chain
GROUP BY Warehouse_Name
ORDER BY Total_Revenue DESC;


-- ============================================================
-- 15. DESTINATION PERFORMANCE
-- ============================================================

SELECT
    Destination,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay,
    ROUND(SUM(Order_Value), 2) AS Total_Revenue
FROM supply_chain
GROUP BY Destination
ORDER BY Average_Delay DESC;


-- ============================================================
-- 16. MONTHLY REVENUE
-- ============================================================

SELECT
    Order_Year,
    Order_Month,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Order_Value), 2) AS Monthly_Revenue
FROM supply_chain
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;


-- ============================================================
-- 17. OVERALL RISK ANALYSIS
-- ============================================================

SELECT
    Overall_Risk,
    COUNT(*) AS Total_Orders,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM supply_chain),
        2
    ) AS Risk_Percentage
FROM supply_chain
GROUP BY Overall_Risk
ORDER BY Total_Orders DESC;


-- ============================================================
-- 18. DELAY CATEGORY ANALYSIS
-- ============================================================

SELECT
    Delay_Category,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM supply_chain
GROUP BY Delay_Category
ORDER BY Average_Delay DESC;