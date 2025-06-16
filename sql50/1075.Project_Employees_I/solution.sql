-- 1075. Project Employees I
-- LeetCode description:
-- Table: Employee
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | employee_id   | int     |
-- | experience_years | int  |
-- +---------------+---------+
-- employee_id is the primary key for this table.
-- Table: Project
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | project_id    | int     |
-- | employee_id   | int     |
-- +---------------+---------+
-- (project_id, employee_id) is the primary key for this table.
-- Write an SQL query to find the average experience years of all the employees for each project, rounded to 2 decimal places.
 -- Solution explanation:
-- This query joins Employee and Project, then calculates the average experience years per project.

SELECT project_id,
       round(avg(experience_years), 2) AS average_years
FROM employee e
JOIN project p ON p.employee_id = e.employee_id
GROUP BY project_id
ORDER BY project_id;