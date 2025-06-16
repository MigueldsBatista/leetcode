-- 570. Managers with at Least 5 Direct Reports
-- LeetCode description:
-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key for this table.
-- Each row of this table contains the id, name, and managerId of an employee.
-- Write an SQL query to find the names of managers with at least 5 direct reports.
 -- Solution explanation:
-- This query joins Employee to itself to count direct reports for each manager, then filters for those with at least 5.

SELECT e1.name
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerid
GROUP BY e1.id
HAVING count(e2.managerid) >= 5;