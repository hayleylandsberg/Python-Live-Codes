-- Comment each query with what you think the results will be, then run it to see if you were correct.

SELECT title, artistname FROM Song

SELECT s.title, a.artistname
FROM song s
JOIN Artist a ON s.artistid = a.artistid
WHERE a.artistname = "ZZTop"

SELECT s.title, a.artistname
FROM song s
JOIN Artist a ON s.artistid = a.artistid
WHERE a.artistname = "ZZTop"
AND s.songlength > 400
AND s.songlength < 900

SELECT count() as '# of songs', artist.artistname
FROM Song
JOIN Artist on song.artistid = artist.artistid
group by song.artistid
order by artist.artistname

SELECT artistname as name
FROM Artist
WHERE name LIKE '%top'

SELECT artistname as name
FROM Artist
WHERE name LIKE '%top%'

SELECT  al.title || " by " || ar.artistname
FROM Album al
JOIN Artist ar ON al.artistid = ar.artistid

SELECT  artist.artistname, al.title
FROM artist
JOIN album al ON al.artistid = artist.artistid

SELECT  artist.artistname, al.title
FROM artist  LEFT JOIN album al ON al.artistid = artist.artistid

INSERT into Artist (artistname, yearestablished)
values ("Kitty Purry", 2018)

INSERT into Artist
values (null, "The Kinks", 1964)

insert into Album
values (null, "Cat Scratch Fever 2018", 2018, 34567, "Desperate Kitty", 32, 7)

insert into Album
select null, "Remixes from Hell", 2018, 666, "Desperate Kitty", artist.artistid, genre.genreid
FROM Artist, Genre
WHERE artist.artistname = "Kitty Purry"
AND genre.label = "Pop"

