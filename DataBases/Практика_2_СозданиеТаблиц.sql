USE `seschool_06`;

CREATE TABLE Movies (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    release_year YEAR,
    genre VARCHAR(255),
    rating DECIMAL(3,1)
);


CREATE TABLE Actors (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    birth_year YEAR,
    nationality VARCHAR(255)
);


CREATE TABLE Movie_Actors (
    movie_id INT,
    actor_id INT,
    role VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (actor_id) REFERENCES Actors(id)
);

