-- 197. Rising Temperature
-- LeetCode description:
-- Table: Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the primary key for this table.
-- Each row of this table contains the id, recordDate, and temperature for a day.
-- Write an SQL query to find all dates' Id with higher temperatures compared to the previous day (yesterday).
 -- Solution explanation:
-- This query joins the Weather table to itself to compare each day's temperature to the previous day's, and selects the id where the temperature increased.

SELECT d2.id
FROM weather d1
INNER JOIN weather d2 ON datediff(d2.recorddate, d1.recorddate) = 1
AND d1.temperature < d2.temperature
GROUP BY d1.id;