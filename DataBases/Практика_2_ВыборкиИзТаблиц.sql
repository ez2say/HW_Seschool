USE `seschool_06`;

/*1.1*/

SELECT * FROM Movies
	WHERE release_year > 2010 AND rating > 8.0
	ORDER BY rating DESC;
	
/*1.2*/

SELECT DISTINCT genre FROM Movies
	ORDER BY genre ASC;

/*1.3*/

SELECT * FROM Movies
	ORDER BY rating DESC
	LIMIT 10 
	OFFSET 10;

/*1.4*/

SELECT * FROM Actors
	WHERE birth_year < 1980
	ORDER BY birth_year ASC;
	
/*1.5*/

SELECT * FROM Movies
	WHERE genre = 'Sci-Fi'
	ORDER BY title ASC;

/*1.6*/

SELECT DISTINCT nationality FROM Actors
	ORDER BY nationality DESC;

/*1.7*/

SELECT title, rating FROM Movies
	WHERE rating < 5.0
	ORDER BY rating ASC;

/*1.8*/

SELECT * FROM Movies
	ORDER BY release_year DESC
	LIMIT 5;

/*1.9*/

SELECT * FROM Actors
	ORDER BY birth_year ASC
	LIMIT 3;

/*-------------------------------------------------------------------------------------------------------------*/
/*2.1*/

SELECT genre, AVG(rating) AS avg_rating FROM Movies
	GROUP BY genre
	ORDER BY avg_rating DESC;

/*2.2*/

SELECT release_year, COUNT(*) AS movie_count FROM Movies
	GROUP BY release_year
	ORDER BY release_year ASC;

/*2.3*/

SELECT genre, COUNT(*) AS movie_count FROM Movies
	GROUP BY genre
	HAVING COUNT(*) > 5
	ORDER BY movie_count DESC;

/*2.4*/

SELECT genre, SUM(rating) AS total_rating FROM Movies
	GROUP BY genre
	HAVING SUM(rating) > 50
	ORDER BY total_rating DESC;

/*2.5*/

SELECT release_year, COUNT(*) AS movie_count FROM Movies
	WHERE rating > 7.0
	GROUP BY release_year
	HAVING COUNT(*) > 5
	ORDER BY movie_count DESC;

/*2.6*/



/*2.7*/



/*-------------------------------------------------------------------------------------------------------------*/
/*3.1*/

SELECT genre, AVG(rating) AS avg_rating, COUNT(*) AS movie_count FROM Movies
	GROUP BY genre
	HAVING AVG(rating) > 6.5 AND COUNT(*) > 10
	ORDER BY avg_rating DESC;

/*3.2*/

SELECT release_year, MIN(rating) AS min_rating FROM Movies
	GROUP BY release_year
	HAVING COUNT(*) > 3
	ORDER BY release_year ASC;

/*3.3*/

SELECT a.name, MAX(r.role_count) AS max_roles FROM Actors a
JOIN (
    SELECT actor_id, movie_id, COUNT(*) AS role_count
    FROM Movie_Actors
    GROUP BY actor_id, movie_id
) r ON a.id = r.actor_id
	GROUP BY a.id
	HAVING COUNT(DISTINCT r.movie_id) >= 5
	ORDER BY max_roles DESC;

/*3.4*/

SELECT genre, AVG(rating) AS avg_rating FROM Movies
	WHERE release_year < 2000
	GROUP BY genre
	HAVING COUNT(*) > 3
	ORDER BY avg_rating DESC;

/*3.5*/
SELECT genre, MIN(rating) AS min_rating FROM Movies
	GROUP BY genre
	HAVING COUNT(*) > 8
	ORDER BY min_rating ASC;