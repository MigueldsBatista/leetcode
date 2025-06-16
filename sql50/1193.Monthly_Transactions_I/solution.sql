-- 1193. Monthly Transactions I
-- LeetCode description:
-- Table: Transactions
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | trans_id    | int     |
-- | trans_date  | date    |
-- | country     | varchar |
-- | state       | enum    |
-- | amount      | int     |
-- +-------------+---------+
-- trans_id is the primary key for this table.
-- state is an ENUM of the type ('approved', 'declined').
-- Write an SQL query to find the monthly transaction count, approved count, total amount, and approved total amount for each country.
 -- Solution explanation:
-- This query groups transactions by country and month, and calculates the required aggregates.

SELECT date_format(trans_date, "%Y-%m") AS MONTH,
       country,
       count(*) AS trans_count,
       sum(`state` = 'approved') AS approved_count,
       sum(amount) AS trans_total_amount,
       sum((`state` = 'approved') * amount) AS approved_total_amount
FROM transactions t
GROUP BY country,
         date_format(trans_date, "%Y-%m");