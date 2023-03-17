-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(rate) AS rating
	FROM tv_genres AS g
	INNER JOIN tv_show_genres AS t
	ON g.id = t.genre_id
	INNER JOIN tv_show_ratings AS s
	ON s.show_id = t.show_id
	GROUP BY g.name
ORDER BY rating DESC;
