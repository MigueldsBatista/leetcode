-- 1280. Students and Examinations
-- LeetCode description:
-- Table: Students
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student_id  | int     |
-- | student_name| varchar |
-- +-------------+---------+
-- student_id is the primary key for this table.
-- Table: Subjects
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | subject_name| varchar |
-- +-------------+---------+
-- subject_name is the primary key for this table.
-- Table: Examinations
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student_id  | int     |
-- | subject_name| varchar |
-- +-------------+---------+
-- (student_id, subject_name) is the primary key for this table.
-- Write an SQL query to find the number of attended exams for each student and subject.
 -- Solution explanation:
-- This query cross joins Students and Subjects, then left joins Examinations to count attended exams for each student and subject.

SELECT s.student_id,
       s.student_name,
       j.subject_name,
       count(e.student_id) AS attended_exams
FROM students s
CROSS JOIN subjects j
LEFT JOIN examinations e ON e.student_id = s.student_id
AND j.subject_name = e.subject_name
GROUP BY s.student_name,
         j.subject_name
ORDER BY student_id,
         student_name,
         subject_name;