-- 595. Big Countries
-- LeetCode description:
-- Table: World
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | name        | varchar |
-- | continent   | varchar |
-- | area        | int     |
-- | population  | int     |
-- | gdp         | bigint  |
-- +-------------+---------+
-- name is the primary key for this table.
-- Each row of this table indicates the name of a country, its continent, area, population, and GDP value.
-- A country is big if:
--   - it has an area of at least three million (i.e., 3000000 km2), or
--   - it has a population of at least twenty-five million (i.e., 25000000).
-- Write an SQL query to output the name, population, and area of the big countries.
 -- Solution explanation:
-- This query selects name, population, and area from World where area >= 3000000 or population >= 25000000.

SELECT name,
       population,
       area
FROM world
WHERE area >= 3000000
  OR population >= 25000000;