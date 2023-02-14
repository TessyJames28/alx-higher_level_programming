-- script that lists the number of records with the same scire in a table
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
