-- 620. Not Boring Movies
-- LeetCode description:
-- Table: Cinema
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | movie       | varchar |
-- | description | varchar |
-- | rating      | float   |
-- +-------------+---------+
-- id is the primary key for this table.
-- Each row of this table contains the id, movie name, description, and rating.
-- Write an SQL query to find the movies with odd IDs and a description that is not 'boring'. Return the result table ordered by rating in descending order.
 -- Solution explanation:
-- This query selects movies with odd IDs and non-boring descriptions, ordered by rating descending.

SELECT id,
       movie,
       description,
       rating
FROM cinema
WHERE description <> 'boring'
  AND id % 2 <> 0
ORDER BY rating DESC;