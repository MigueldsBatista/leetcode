-- 1757. Recyclable and Low Fat Products
-- LeetCode description:
-- Table: Products
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
-- product_id is the primary key for this table.
-- low_fats is an ENUM ("Y", "N") where "Y" means this product is low fat.
-- recyclable is an ENUM ("Y", "N") where "Y" means this product is recyclable.
-- Write an SQL query to find the ids of products that are both low fat and recyclable.
 -- Solution explanation:
-- This query selects product_id from Products where both low_fats and recyclable are 'Y'.

SELECT product_id
FROM products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';