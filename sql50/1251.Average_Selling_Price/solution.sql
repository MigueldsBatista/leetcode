-- 1251. Average Selling Price
-- LeetCode description:
-- Table: Prices
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | start_date  | date    |
-- | end_date    | date    |
-- | price       | int     |
-- +-------------+---------+
-- (product_id, start_date, end_date) is the primary key for this table.
-- Table: UnitsSold
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | purchase_date| date   |
-- | units       | int     |
-- +-------------+---------+
-- (product_id, purchase_date) is the primary key for this table.
-- Write an SQL query to find the average selling price for each product.
 -- Solution explanation:
-- This query left joins Prices and UnitsSold on product_id and purchase_date between start_date and end_date, then calculates the average price weighted by units sold.

SELECT p.product_id,
       ifnull(round(sum(price * units) / sum(units), 2), 0) AS average_price
FROM prices p
LEFT JOIN unitssold u ON u.product_id = p.product_id
AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id;