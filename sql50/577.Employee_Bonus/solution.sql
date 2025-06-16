-- 577. Employee Bonus
-- LeetCode description:
-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | empId       | int     |
-- | name        | varchar |
-- +-------------+---------+
-- empId is the primary key for this table.
-- Table: Bonus
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | empId       | int     |
-- | bonus       | int     |
-- +-------------+---------+
-- empId is the primary key for this table.
-- Each row of Employee contains the employee ID and their name. Each row of Bonus contains the empId and their bonus amount.
-- Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000 or no bonus at all.
 -- Solution explanation:
-- This query left joins Employee and Bonus, then filters for bonus < 1000 or bonus is null.

SELECT name,
       bonus
FROM employee e
LEFT JOIN bonus b ON b.empid = e.empid
WHERE bonus < 1000
  OR bonus IS NULL;