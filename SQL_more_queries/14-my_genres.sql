-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_shows
WHERE title = 'Dexter'
ORDER BY tv_genres.name ASC;
