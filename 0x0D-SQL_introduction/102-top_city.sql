-- Displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city
	LIMIT 3
ORDER BY state;
