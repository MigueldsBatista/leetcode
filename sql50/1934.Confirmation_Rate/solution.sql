-- 1934. Confirmation Rate
-- LeetCode description:
-- Table: Signups
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | time_stamp  | datetime|
-- +-------------+---------+
-- user_id is the primary key for this table.
-- Table: Confirmations
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | time_stamp  | datetime|
-- | action      | enum    |
-- +-------------+---------+
-- (user_id, time_stamp) is the primary key for this table.
-- action is an ENUM of the type ('confirmed', 'timeout').
-- Write an SQL query to find the confirmation rate for each user.
 -- Solution explanation:
-- This query calculates the confirmation rate as the number of 'confirmed' actions divided by the total number of confirmation messages for each user.
-- It uses subqueries to count confirmed and timeout actions, then computes the rate.

SELECT s.user_id,
       round(coalesce(coalesce(c.confirmed, 0) * 1.0 / nullif(coalesce(c.confirmed, 0) + coalesce(t.timed_out, 0), 0), 0), 2) AS confirmation_rate
FROM signups s
LEFT JOIN
  (SELECT user_id,
          count(*) AS confirmed
   FROM confirmations
   WHERE action = 'confirmed'
   GROUP BY user_id) c ON s.user_id = c.user_id
LEFT JOIN
  (SELECT user_id,
          count(*) AS timed_out
   FROM confirmations
   WHERE action = 'timeout'
   GROUP BY user_id) t ON s.user_id = t.user_id;