-- 1141. User Activity for the Past 30 Days I
-- LeetCode description:
-- Table: Activity
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | session_id    | int     |
-- | activity_date | date    |
-- | activity_type | enum    |
-- +---------------+---------+
-- (user_id, session_id) is the primary key for this table.
-- Write an SQL query to find the number of active users for each day in the past 30 days.
 -- Solution explanation:
-- This query counts distinct user_id for each activity_date in the specified range.

SELECT activity_date AS DAY,
       count(DISTINCT user_id) AS active_users
FROM activity
WHERE activity_date BETWEEN date_add('2019-07-28', INTERVAL -30 DAY) AND '2019-07-27'
GROUP BY extract(DAY
                 FROM activity_date)
ORDER BY activity_date;