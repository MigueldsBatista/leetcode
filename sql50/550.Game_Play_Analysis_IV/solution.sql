-- 550. Game Play Analysis IV
-- LeetCode description:
-- Table: Activity
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | player_id     | int     |
-- | device_id     | int     |
-- | event_date    | date    |
-- | games_played  | int     |
-- +---------------+---------+
-- (player_id, event_date) is the primary key for this table.
-- Write an SQL query to find the fraction of players who logged in again the day after their first login, rounded to 2 decimal places.
 -- Solution explanation:
-- This query finds the first login for each player, then checks if the player logged in again the next day, and calculates the fraction.

SELECT round(count(a.player_id) /
               (SELECT count(DISTINCT player_id)
                FROM activity), 2) AS fraction
FROM activity a
JOIN
  (SELECT min(event_date) AS first_login,
          player_id
   FROM activity
   GROUP BY player_id) a2 ON a.event_date = date_add(first_login, INTERVAL 1 DAY)
AND a2.player_id = a.player_id;