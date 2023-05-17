-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- list is sorted in descending order
SELECT Â`score`, `name`
FROM `second_table`
WHERE `name` != Â""
ORDER BY `score` DESC;