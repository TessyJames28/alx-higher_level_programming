-- script that lists all records of the table in descending order
-- don't list rows without a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
