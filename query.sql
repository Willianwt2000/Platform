select  * from film

-- SELECT DISTINCT school
-- FROM teachers;


SELECT DISTINCT school,teachers.salary
FROM teachers;



SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;