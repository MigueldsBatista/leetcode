-- 584. Find Customer Referee
-- LeetCode description:
-- Table: Customer
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | referee_id  | int     |
-- +-------------+---------+
-- id is the primary key for this table.
-- Each row of this table indicates the id and name of a customer, and the id of the customer who referred them.
-- Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
 -- Solution explanation:
-- This query selects names from Customer where referee_id is not 2 or is NULL.

SELECT c1.name
FROM customer c1
WHERE c1.referee_id != 2
  OR c1.referee_id IS NULL;