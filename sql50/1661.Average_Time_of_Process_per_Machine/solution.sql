-- 1661. Average Time of Process per Machine
-- LeetCode description:
-- Table: Activity
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | int     |
-- +----------------+---------+
-- (machine_id, process_id, activity_type) is the primary key for this table.
-- activity_type is an ENUM ('start', 'end').
-- Each row in this table shows the activity of a machine with the process it was working on and the timestamp.
-- Write an SQL query to find the average time each machine takes to complete a process.
 -- Solution explanation:
-- This query joins Activity table to itself to pair start and end activities, then calculates the average processing time per machine.

SELECT t1.machine_id,
       round(avg(t2.timestamp - t1.timestamp), 3) AS processing_time
FROM activity t1
INNER JOIN activity t2 ON t1.machine_id = t2.machine_id
AND t1.process_id = t2.process_id
WHERE t1.activity_type = 'start'
  AND t2.activity_type = 'end'
GROUP BY t1.machine_id;