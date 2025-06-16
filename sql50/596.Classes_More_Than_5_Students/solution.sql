-- 596. Classes More Than 5 Students
-- LeetCode description:
-- Table: Courses
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student     | varchar |
-- | class       | varchar |
-- +-------------+---------+
-- (student, class) is the primary key for this table.
-- Each row of this table indicates the name of a student and the class in which they are enrolled.
-- Write an SQL query to report all the classes that have at least 5 students.
-- Return the result table in any order.
 -- Solution explanation:
-- This query groups the Courses table by class and counts the number of students in each class.
-- It then filters to only include classes with 5 or more students.

SELECT CLASS
FROM courses
GROUP BY CLASS
HAVING count(student) >= 5;