-- 1683. Invalid Tweets
-- LeetCode description:
-- Table: Tweets
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | tweet_id    | int     |
-- | content     | varchar |
-- +-------------+---------+
-- tweet_id is the primary key for this table.
-- Each row of this table contains the ID and the content of a tweet.
-- Write an SQL query to find the IDs of tweets with content longer than 15 characters.
 -- Solution explanation:
-- This query selects tweet_id from Tweets where the length of content is greater than 15.

SELECT tweet_id
FROM tweets
WHERE length(content) > 15;