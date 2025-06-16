-- 1148. Article Views I
-- LeetCode description:
-- Table: Views
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | article_id  | int     |
-- | author_id   | int     |
-- | viewer_id   | int     |
-- | view_date   | date    |
-- +-------------+---------+
-- (article_id, view_date) is the primary key for this table.
-- Each row of this table indicates that some viewer viewed an article (written by some author) on a certain date.
-- Write an SQL query to find all the authors that viewed at least one of their own articles.
 -- Solution explanation:
-- This query selects author_id as id from Views where viewer_id = author_id, groups by id, and orders by id.

SELECT author_id AS id
FROM VIEWS
WHERE viewer_id = author_id
GROUP BY id
ORDER BY id;