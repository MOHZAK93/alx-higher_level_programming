-- lists all genres not linked to the show Dexter.
SELECT DISTINCT g.name
	FROM tv_genres AS g 
	INNER JOIN tv_show_genres AS t 
	ON g.id = t.genre_id 
	INNER JOIN tv_shows AS s 
	ON t.show_id = s.id 
	WHERE g.name NOT IN (SELECT name 
		FROM tv_genres AS g
		INNER JOIN tv_show_genres AS t 
		ON g.id = t.genre_id
		INNER JOIN tv_shows AS s
		ON t.show_id = s.id
		WHERE s.title = 'Dexter')
ORDER BY g.name ASC;
