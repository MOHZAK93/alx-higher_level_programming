-- lists the number of records with the same score in table in MySQL server
SELECT DISTINCT score, COUNT(score) AS number FROM second_table ORDER BY number DESC;