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