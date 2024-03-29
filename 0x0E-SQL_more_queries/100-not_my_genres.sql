-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN
(
	SELECT tv_genres.id, tv_genres.name
	FROM tv_genres
	JOIN tv_shows_genres
		ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
		ON tv_shows_genres.id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
	ORDER BY tv_genres.id
) dexter_genres ON dexter_genres.id = tv_genres.id
WHERE dexter_genres.id = NULL
ORDER BY tv_genres.name;
