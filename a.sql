SELECT t.name, a.Title, g.name as tracks, p.name as Genero FROM artists t
JOIN albums a on t.ArtistId = a.ArtistId
JOIN tracks g on a.AlbumId = g.AlbumId
JOIN genres p on g.GenreId = p.GenreId