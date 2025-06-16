-- 1174. Immediate Food Delivery II
-- LeetCode description:
-- Table: Delivery
-- +-------------------------+---------+
-- | Column Name             | Type    |
-- +-------------------------+---------+
-- | delivery_id             | int     |
-- | customer_id             | int     |
-- | order_date              | date    |
-- | customer_pref_delivery_date | date |
-- +-------------------------+---------+
-- delivery_id is the primary key for this table.
-- Each row of this table contains the delivery id, customer id, order date, and preferred delivery date.
-- Write an SQL query to find the percentage of customers who received immediate food delivery on their first order, rounded to 2 decimal places.
 -- Solution explanation:
-- This query finds the first order for each customer, then checks if the order date matches the preferred delivery date, and calculates the percentage.

SELECT round(sum(d1.order_date = d1.customer_pref_delivery_date) / count(*) * 100, 2) AS immediate_percentage
FROM delivery d1
JOIN
  (SELECT customer_id,
          min(order_date) AS first_order_date
   FROM delivery
   GROUP BY customer_id) d2 ON d1.customer_id = d2.customer_id
AND d1.order_date = d2.first_order_date;