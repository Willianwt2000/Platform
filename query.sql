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