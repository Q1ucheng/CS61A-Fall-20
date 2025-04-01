.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
        FROM students AS a, students AS b
        WHERE a.pet = b.pet and a.song = b.song and a.time != b.time;


CREATE TABLE sevens AS
  SELECT seven 
  FROM students as a, numbers as b
  WHERE a.time = b.time and b.'7' = 'True' and a.number = 7;

