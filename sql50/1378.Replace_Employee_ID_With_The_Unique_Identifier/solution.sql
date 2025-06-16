-- 1378. Replace Employee ID With The Unique Identifier
-- LeetCode description:
-- Table: Employees
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key for this table.
-- Table: EmployeeUNI
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | unique_id   | int     |
-- +-------------+---------+
-- id is the primary key for this table.
-- Each row in Employees contains the id and name of an employee. Each row in EmployeeUNI contains the id and unique_id of an employee.
-- Write an SQL query to show the unique ID and name of each employee.
 -- Solution explanation:
-- This query joins Employees and EmployeeUNI on id and selects unique_id and name.

SELECT unique_id,
       name
FROM employees e
LEFT JOIN employeeuni u ON e.id = u.id;