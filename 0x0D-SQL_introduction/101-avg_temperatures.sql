-- displays the average temperature by city oredered by temperature in MySQL server
SELECT city, AVG(value) AS avg_temp FROM `temperatures` ORDER BY city DESC;
