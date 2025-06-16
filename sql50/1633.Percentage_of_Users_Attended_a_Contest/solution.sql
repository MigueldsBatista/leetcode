-- 1633. Percentage of Users Attended a Contest
-- LeetCode description:
-- Table: Users
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- +-------------+---------+
-- user_id is the primary key for this table.
-- Table: Register
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | contest_id  | int     |
-- | user_id     | int     |
-- +-------------+---------+
-- (contest_id, user_id) is the primary key for this table.
-- Write an SQL query to find the percentage of users registered for each contest, rounded to 2 decimal places.
 -- Solution explanation:
-- This query joins Users and Register, counts users per contest, and divides by the total number of users to get the percentage.

SELECT r.contest_id,
       coalesce(round(count(r.user_id) /
                        (SELECT count(*)
                         FROM users) * 100, 2), 0) AS percentage
FROM users u
JOIN register r ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC,
         contest_id ASC;