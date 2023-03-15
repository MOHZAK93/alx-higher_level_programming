-- lists the number of records with the same score in table in MySQL server
SELECT score, COUNT(*) AS number FROM second_table ORDER BY number DESC;
