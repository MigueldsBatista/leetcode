-- 2356. Number of Unique Subjects Taught by Each Teacher
-- LeetCode description:
-- Table: Teacher
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | teacher_id  | int     |
-- | subject_id  | int     |
-- +-------------+---------+
-- (teacher_id, subject_id) is the primary key for this table.
-- Write an SQL query to find the number of unique subjects taught by each teacher.
 -- Solution explanation:
-- This query counts distinct subject_id for each teacher_id.

SELECT teacher_id,
       count(DISTINCT subject_id) AS cnt
FROM teacher
GROUP BY teacher_id;