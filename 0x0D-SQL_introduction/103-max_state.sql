-- Displays the max temperature of each state
SELECT DISTINCT state, MAX(value) AS max_temp
	FROM temperatures
ORDER BY state;
