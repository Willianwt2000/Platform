select  * from film

-- SELECT DISTINCT school
-- FROM teachers;


SELECT DISTINCT school,teachers.salary
FROM teachers;



SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;


SELECT last_name,school,hire_date 
FROM teachers
ORDER BY school ASC , hire_date DESC;


SELECT last_name, school, hire_date
FROM teachers
WHERE school = 'Myers Middle School';




SELECT first_name, last_name, school, salary
FROM teachers
WHERE salary BETWEEN 40000 AND 65000;
SHOW ALL;

SELECT column_names
FROM table_name
WHERE criteria
ORDER BY column_names;


SELECT first_name, last_name, school, hire_date, salary
FROM teachersl
ORDER BY hire_date DESC;



COPY teachers
FROM '/home/enigma_wt/Documents/result_export.csv'
WITH (FORMAT CSV, HEADER);


--------------------------------------------------------------
-- Practical SQL: A Beginner's Guide to Storytelling with Data
-- by Anthony DeBarros

-- Chapter 1 Code Examples
--------------------------------------------------------------

-- Listing 1-1: Creating a database named analysis

CREATE DATABASE analysis;

-- Listing 1-2: Creating a table named teachers with six columns

CREATE TABLE teachers (
    id bigserial,
    first_name varchar(25),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);

-- This command will remove (drop) the table.
-- DROP TABLE teachers;

-- Listing 1-3 Inserting data into the teachers table

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
       ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
       ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
       ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
       ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
       ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);






CREATE TABLE us_counties_2010 (
    NAME varchar(90),
    STUSAB varchar(2),
    SUMLEV varchar(3),
    REGION smallint,
    DIVISION smallint,
    STATE varchar(2),
    COUNTY varchar(3),
    AREALAND bigint,
    AREAWATR bigint,
    POP100 integer,
    HU100 integer,
    INTPTLAT numeric(10,7),
    INTPTLON numeric(10,7),
    P0010001 integer,
    P0010002 integer,
    P0010003 integer,
    P0010004 integer,
    P0010005 integer,
    P0010006 integer,
    P0010007 integer,
    P0010008 integer,
    P0010009 integer,
    P0010010 integer,
    P0010011 integer,
    P0010012 integer,
    P0010013 integer,
    P0010014 integer,
    P0010015 integer,
    P0010016 integer,
    P0010017 integer,
    P0010018 integer,
    P0010019 integer,
    P0010020 integer,
    P0010021 integer,
    P0010022 integer,
    P0010023 integer,
    P0010024 integer,
    P0010025 integer,
    P0010026 integer,
    P0010047 integer,
    P0010063 integer,
    P0010070 integer,
    P0020001 integer,
    P0020002 integer,
    P0020003 integer,
    P0020004 integer,
    P0020005 integer,
    P0020006 integer,
    P0020007 integer,
    P0020008 integer,
    P0020009 integer,
    P0020010 integer,
    P0020011 integer,
    P0020012 integer,
    P0020028 integer,
    P0020049 integer,
    P0020065 integer,
    P0020072 integer,
    P0030001 integer,
    P0030002 integer,
    P0030003 integer,
    P0030004 integer,
    P0030005 integer,
    P0030006 integer,
    P0030007 integer,
    P0030008 integer,
    P0030009 integer,
    P0030010 integer,
    P0030026 integer,
    P0030047 integer,
    P0030063 integer,
    P0030070 integer,
    P0040001 integer,
    P0040002 integer,
    P0040003 integer,
    P0040004 integer,
    P0040005 integer,
    P0040006 integer,
    P0040007 integer,
    P0040008 integer,
    P0040009 integer,
    P0040010 integer,
    P0040011 integer,
    P0040012 integer,
    P0040028 integer,
    P0040049 integer,
    P0040065 integer,
    P0040072 integer,
    H0010001 integer,
    H0010002 integer,
    H0010003 integer
);


SELECT NAME, STUSAB, AREALAND
FROM us_counties_2010
ORDER BY AREALAND DESC
LIMIT 3;


SELECT NAME, STUSAB, INTPTLON
FROM us_counties_2010
ORDER BY INTPTLON DESC
LIMIT 5;




-- Importing a Subset of Columns with COPY

CREATE TABLE supervisor_salaries (
    town varchar(30),
    county varchar(30),
    supervisor varchar(30),
    start_date date,
    salary money,
    benefits money
);

SELECT * FROM supervisor_salaries_temp;

-- DELETE FROM supervisor_salaries;

CREATE TEMPORARY TABLE supervisor_salaries_temp (LIKE supervisor_salaries);


DROP TABLE us_counties_2010;

/home/enigma_wt/practical-sql/Chapter_04/us_counties_2010.csv


DROP TABLE us_counties_2010;

-- /home/enigma_wt/practical-sql/Chapter_04/us_counties_2010.csv

COPY us_counties_2010
TO "/home/enigma_wt/Documents/test_file | us_counties_2010_export.txt"
WITH(FORMAT CSV, HEADER, DELIMITER'|');

COPY us_counties_2010 (geo_name, internal_point_lat, internal_point_lon)
TO 'C:\YourDirectory\us_counties_latlon_export.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

-- psql -h localhost -p 5432 -U student -d analysis -c  TO "/home/enigma_wt/Documents/test_file | us_counties_2010_export.txt"



psql -h localhost -p 5432 -U student -d analysis -c 
"\copy (
SELECT name, state
FROM us_counties_2010
WHERE name ILIKE '%mill%'
) TO '/home/enigma_wt/Documents/test_file/us_counties_mill_export.txt' WITH CSV HEADER DELIMITER '|';"








-- -------------------------------------------------


-- --------------------------------------------------------------
-- -- Practical SQL: A Beginner's Guide to Storytelling with Data
-- -- by Anthony DeBarros

-- -- Chapter 1 Code Examples
-- --------------------------------------------------------------

-- -- Listing 1-1: Creating a database named analysis

-- CREATE DATABASE analysis;

-- -- Listing 1-2: Creating a table named teachers with six columns

-- CREATE TABLE teachers (
--     id bigserial,
--     first_name varchar(25),
--     last_name varchar(50),
--     school varchar(50),
--     hire_date date,
--     salary numeric
-- );

-- -- This command will remove (drop) the table.
-- -- DROP TABLE teachers;

-- -- Listing 1-3 Inserting data into the teachers table

-- INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
-- VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
--        ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
--        ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
--        ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
--        ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
--        ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);






-- CREATE TABLE us_counties_2010 (
--     NAME varchar(90),
--     STUSAB varchar(2),
--     SUMLEV varchar(3),
--     REGION smallint,
--     DIVISION smallint,
--     STATE varchar(2),
--     COUNTY varchar(3),
--     AREALAND bigint,
--     AREAWATR bigint,
--     POP100 integer,
--     HU100 integer,
--     INTPTLAT numeric(10,7),
--     INTPTLON numeric(10,7),
--     P0010001 integer,
--     P0010002 integer,
--     P0010003 integer,
--     P0010004 integer,
--     P0010005 integer,
--     P0010006 integer,
--     P0010007 integer,
--     P0010008 integer,
--     P0010009 integer,
--     P0010010 integer,
--     P0010011 integer,
--     P0010012 integer,
--     P0010013 integer,
--     P0010014 integer,
--     P0010015 integer,
--     P0010016 integer,
--     P0010017 integer,
--     P0010018 integer,
--     P0010019 integer,
--     P0010020 integer,
--     P0010021 integer,
--     P0010022 integer,
--     P0010023 integer,
--     P0010024 integer,
--     P0010025 integer,
--     P0010026 integer,
--     P0010047 integer,
--     P0010063 integer,
--     P0010070 integer,
--     P0020001 integer,
--     P0020002 integer,
--     P0020003 integer,
--     P0020004 integer,
--     P0020005 integer,
--     P0020006 integer,
--     P0020007 integer,
--     P0020008 integer,
--     P0020009 integer,
--     P0020010 integer,
--     P0020011 integer,
--     P0020012 integer,
--     P0020028 integer,
--     P0020049 integer,
--     P0020065 integer,
--     P0020072 integer,
--     P0030001 integer,
--     P0030002 integer,
--     P0030003 integer,
--     P0030004 integer,
--     P0030005 integer,
--     P0030006 integer,
--     P0030007 integer,
--     P0030008 integer,
--     P0030009 integer,
--     P0030010 integer,
--     P0030026 integer,
--     P0030047 integer,
--     P0030063 integer,
--     P0030070 integer,
--     P0040001 integer,
--     P0040002 integer,
--     P0040003 integer,
--     P0040004 integer,
--     P0040005 integer,
--     P0040006 integer,
--     P0040007 integer,
--     P0040008 integer,
--     P0040009 integer,
--     P0040010 integer,
--     P0040011 integer,
--     P0040012 integer,
--     P0040028 integer,
--     P0040049 integer,
--     P0040065 integer,
--     P0040072 integer,
--     H0010001 integer,
--     H0010002 integer,
--     H0010003 integer
-- );


-- SELECT NAME, STUSAB, AREALAND
-- FROM us_counties_2010
-- ORDER BY AREALAND DESC
-- LIMIT 3;


-- SELECT NAME, STUSAB, INTPTLON
-- FROM us_counties_2010
-- ORDER BY INTPTLON DESC
-- LIMIT 5;




-- -- Importing a Subset of Columns with COPY

-- CREATE TABLE supervisor_salaries (
--     town varchar(30),
--     county varchar(30),
--     supervisor varchar(30),
--     start_date date,
--     salary money,
--     benefits money
-- );

-- SELECT * FROM supervisor_salaries_temp;

-- -- DELETE FROM supervisor_salaries;

-- CREATE TEMPORARY TABLE supervisor_salaries_temp (LIKE supervisor_salaries);


-- DROP TABLE us_counties_2010;

-- -- /home/enigma_wt/practical-sql/Chapter_04/us_counties_2010.csv

-- COPY us_counties_2010
-- TO "/home/enigma_wt/Documents/test_file | us_counties_2010_export.txt"
-- WITH(FORMAT CSV, HEADER, DELIMITER'|');

-- COPY us_counties_2010 (geo_name, internal_point_lat, internal_point_lon)
-- TO 'C:\YourDirectory\us_counties_latlon_export.txt'
-- WITH (FORMAT CSV, HEADER, DELIMITER '|');

-- -- psql -h localhost -p 5432 -U student -d analysis -c  TO "/home/enigma_wt/Documents/test_file | us_counties_2010_export.txt"



-- psql -h localhost -p 5432 -U student -d analysis -c 
-- "\copy (
-- SELECT name, state
-- FROM us_counties_2010
-- WHERE name ILIKE '%mill%'
-- ) TO '/home/enigma_wt/Documents/test_file/us_counties_mill_export.txt' WITH CSV HEADER DELIMITER '|';"








-- SELECT * FROM animals;



-- SELECT 
--     name,
--     state AS "st",
--     p0010001 AS "Total Population",
--     p0010003 AS "White Alone",
--     p0010004 AS "Black or African American Alone",
--     p0010005 AS "Am Indian/Alaska Native Alone",
--     p0010006 AS "Asian Alone",
--     p0010007 AS "Native Hawaiian and Other Pacific Islander Alone",
--     p0010008 AS "Some Other Race Alone",
--     p0010009 AS "Two or More Races"
-- FROM us_counties_2010;



-- SELECT name,
--     state AS "st",
--     p0010003 AS "White Alone",
--     p0010004 AS "Black Alone",
--     p0010003 + p0010004 AS "Total White and Black"
-- FROM us_counties_2010;




-- SELECT name,
--     state AS "st",
--         p0010001 AS "Total",
--         p0010003 + p0010004 + p0010005 + p0010006 + p0010007
--         + p0010008 + p0010009 AS "All Races",
--         (p0010003 + p0010004 + p0010005 + p0010006 + p0010007
--         + p0010008 + p0010009) - p0010001 AS "Difference"
--     FROM us_counties_2010
-- ORDER BY "Difference" DESC;


-- ! percentages 
SELECT name,
    stusab AS "st",
    (CAST (p0010006 AS numeric(8,1)) / p0010001) * 100 AS "pct_asian"
FROM us_counties_2010
ORDER BY "pct_asian" DESC;


-- Creating a new table to store percent change in spending for different departments
CREATE TABLE percent_change (
    department varchar(20),
    spend_2014 numeric(10,2),
    spend_2017 numeric(10,2)
);
-- Inserting data into the percent_change table
INSERT INTO percent_change
VALUES
('Building', 250000, 289000),
('Assessor', 178556, 179500),
('Library', 87777, 90001),
('Clerk', 451980, 650000),
('Police', 250000, 223000),
('Recreation', 199000, 195000);


-- Calculating percent change in spending for each department   formula: (new - old) / old * 100 example: (73 - 59) / 59 * 100
-- SELECT department,
--     spend_2014,
--     spend_2017,
--     -- round to one decimal place
--     round( (spend_2017 - spend_2014) /
--     spend_2014 * 100, 1) AS "pct_change"
-- FROM percent_change;



-- * Aggregate Functions for Averages and Sums

-- SELECT sum(p0010001) AS "County Sum",
-- round(avg(p0010001), 0) AS "County Average"
-- FROM us_counties_2010;


-- select sum(region) as "Region Sum", round(avg(region), 0) as "Region Average" from us_counties_2010;


-- WITH numbers(value) AS (
--     VALUES
--     (12),(15),(18),(20),(21),(22),(22),(23),(24),(25),
--     (25),(26),(27),(28),(29),(30),(30),(31),(32),(33),
--     (34),(35),(36),(37),(38),(39),(40),(41),(42),(43),
--     (44),(45),(46),(47),(48),(49),(50),(52),(54),(56),
--     (58),(60),(62),(65),(70),(75),(80),(120),(300),(1000)
-- )

-- SELECT
--     AVG(value) AS average,
--     PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY value) AS p25,
--     PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY value) AS median,
--     PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY value) AS p75,
--     MIN(value),
--     MAX(value)
-- FROM numbers;


-- CREATE TABLE percentile_test (
--     numbers integer
-- );
-- INSERT INTO percentile_test (numbers) VALUES
--     (1), (2), (3), (4), (5), (6);


SELECT
 percentile_cont(.5)
WITHIN GROUP (ORDER BY numbers),
 percentile_disc(.5)
WITHIN GROUP (ORDER BY numbers)
    FROM percentile_test




SELECT sum(p0010001) AS "County Sum",round(avg(p0010001), 0) AS "County Average",
    percentile_cont(.5)
WITHIN GROUP (ORDER BY p0010001) AS "County Median"
    FROM us_counties_2010;