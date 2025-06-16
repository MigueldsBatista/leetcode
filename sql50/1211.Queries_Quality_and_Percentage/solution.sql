-- 1211. Queries Quality and Percentage
-- LeetCode description:
-- Table: Queries
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | query_name  | varchar |
-- | result      | varchar |
-- | position    | int     |
-- | rating      | int     |
-- +-------------+---------+
-- (query_name, result) is the primary key for this table.
-- Write an SQL query to find the quality and poor query percentage for each query name.
 -- Solution explanation:
-- This query calculates the average quality and the percentage of poor queries (rating < 3) for each query name.

SELECT query_name,
       round(avg(rating / POSITION), 2) AS quality,
       round(sum(rating < 3) / count(*) * 100, 2) AS poor_query_percentage
FROM queries q
GROUP BY query_name;