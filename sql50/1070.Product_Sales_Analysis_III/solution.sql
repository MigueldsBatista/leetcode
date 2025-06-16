-- 1070. Product Sales Analysis III
-- LeetCode description:
-- Table: Sales
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | sale_id     | int     |
-- | product_id  | int     |
-- | year        | int     |
-- | quantity    | int     |
-- | price       | int     |
-- +-------------+---------+
-- sale_id is the primary key for this table.
-- Write an SQL query to find the product_id, first_year, quantity, and price for each product's first year of sales.
 -- Solution explanation:
-- This query finds the minimum year for each product, then joins to get the quantity and price for that year.

SELECT s1.product_id,
       s1.year AS first_year,
       quantity,
       price
FROM sales s1
JOIN
  (SELECT min(YEAR) AS YEAR,
          product_id
   FROM sales
   GROUP BY product_id) s2 ON s1.product_id = s2.product_id
AND s1.year = s2.year
GROUP BY sale_id;