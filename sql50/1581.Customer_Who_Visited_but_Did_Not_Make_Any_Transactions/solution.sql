-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- LeetCode description:
-- Table: Visits
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | visit_id    | int     |
-- | customer_id | int     |
-- +-------------+---------+
-- visit_id is the primary key for this table.
-- Table: Transactions
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | transaction_id | int  |
-- | visit_id       | int  |
-- +---------------------+--+
-- transaction_id is the primary key for this table.
-- Each row of Visits indicates a visit by a customer. Each row of Transactions indicates a transaction made during a visit.
-- Write an SQL query to find the IDs and visit counts of customers who visited but did not make any transactions.
 -- Solution explanation:
-- This query selects customer_id and counts visits from Visits where visit_id is not in Transactions, grouped by customer_id.

SELECT customer_id,
       count(*) AS count_no_trans
FROM visits v
WHERE v.visit_id NOT IN
    (SELECT visit_id
     FROM transactions)
GROUP BY customer_id;