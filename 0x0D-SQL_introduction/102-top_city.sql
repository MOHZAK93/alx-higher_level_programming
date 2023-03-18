-- Displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	WHERE month >= 7 AND month <=8
	LIMIT 3
	GROUP BY city
ORDER BY avg_temp DESC;
