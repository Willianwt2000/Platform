onnection FROM users WHERE last_connection LIKE '221%' order by id DESC;


-- SELECT
--     first_name,
--     last_name,
--     followers
-- from
--     users
-- where
-- --     followers >= 4600
-- --     and followers <= 4700
-- 	followers BETWEEN 4600 and 4700
-- order by
--     followers ASC;


-- * Funciones agregadas

-- SELECT
--     COUNT(*) AS total_users,
--     MIN(followers) as min_followers,
--     MAX(followers) as max_followers,
--     ROUND(AVG(followers)) as avg_followers_redondeado,
--     AVG(followers) as avg_followers,
--     SUM(followers) / count(*) as avg_manual
-- FROM
--     users;



-- * Group by

SELECT count(*),followers
    FROM users
WHERE followers = 4 OR followers = 4999
    GROUP BY followers
    ORDER BY followers DESC


SELECT * from public.actor where first_name like '%M'

SELECT customer_id,COUNT(rental_id) AS total_rentas FROM rental GROUP by customer_id HAVING COUNT(rental_id)>25;




select * from public.actor;


SELECT customer_id,COUNT(rental_id) AS total_rentas FROM rental GROUP by customer_id HAVING COUNT(rental_id)>25;



-- Generar mi nueva tabla

create table review (
	review_id SERIAL PRIMARY KEY,
	film_id INT,
	customer_id INT,
	rating INT CHECk (rating BETWEEN 1 AND 5),
	review_text TEXT,
	review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	
);


select * from review

insert into review 
(film_id,customer_id,rating,review_text,review_date)
values
(134, 25, 4, 'Initial performance check', NOW()),
(135, 26, 4, 'System optimization', NOW()),
(136, 27, 4, 'Network latency test', NOW()),
(137, 28, 4, 'Database indexing', NOW()),
(138, 29, 4, 'Cache clearance', NOW()),
(139, 30, 4, 'CPU load analysis', NOW()),
(140, 31, 4, 'Memory leak detection', NOW()),
(141, 32, 4, 'API response timing', NOW()),
(142, 33, 4, 'Security protocol audit', NOW()),
(143, 34, 4, 'UI rendering speed', NOW()),
(144, 35, 4, 'Background process task', NOW()),
(145, 36, 4, 'Disk I/O monitoring', NOW()),
(146, 37, 4, 'Load balancer tweak', NOW()),
(147, 38, 4, 'Error rate reduction', NOW()),
(148, 39, 4, 'Throughput measurement', NOW()),
(149, 40, 4, 'Connection pool resize', NOW()),
(150, 41, 4, 'Query execution plan', NOW()),
(151, 42, 4, 'Docker container health', NOW()),
(152, 43, 4, 'Frontend bundle size', NOW()),
(153, 44, 4, 'Backend stress test', NOW()),
(154, 45, 4, 'Concurrency handling', NOW()),
(155, 46, 4, 'SSL handshake speed', NOW()),
(156, 47, 4, 'Asset compression check', NOW()),
(157, 48, 4, 'DNS lookup timing', NOW()),
(158, 49, 4, 'Session timeout log', NOW()),
(159, 50, 4, 'Websocket heartbeat', NOW()),
(160, 51, 4, 'Image lazy load check', NOW()),
(161, 52, 4, 'Garbage collection log', NOW()),
(162, 53, 4, 'Encryption overhead', NOW()),
(163, 54, 4, 'SLA compliance check', NOW()),
(164, 55, 4, 'Script execution delay', NOW()),
(165, 56, 4, 'Third party API lag', NOW()),
(166, 57, 4, 'Database lock audit', NOW()),
(167, 58, 4, 'Redundant data removal', NOW()),
(168, 59, 4, 'Hotfix performance verify', NOW()),
(169, 60, 4, 'Scaling event trigger', NOW()),
(170, 61, 4, 'Metric collection sync', NOW()),
(171, 62, 4, 'Mobile responsiveness', NOW()),
(172, 63, 4, 'Hydration time test', NOW()),
(173, 64, 4, 'Worker thread activity', NOW()),
(174, 65, 4, 'Log rotation status', NOW()),
(175, 66, 4, 'Critical path analysis', NOW()),
(176, 67, 4, 'Hardware interrupt log', NOW()),
(177, 68, 4, 'Cluster node rebalance', NOW()),
(178, 69, 4, 'Virtual memory swap', NOW()),
(179, 70, 4, 'Transaction commit rate', NOW()),
(180, 71, 4, 'Buffer hit ratio', NOW()),
(181, 72, 4, 'Payload size audit', NOW()),
(182, 73, 4, 'Uptime verification', NOW()),
(183, 74, 4, 'Resource allocation', NOW());


select customer.first_name,customer.last_name,rental.rental_date from customer
join rental on customer.customer_id =  rental.customer_id

select * from cust

select review.review_text,customer.first_name from review
join customer on customer.customer_id = review.customer_id



-- right and left join


SELECT
    customer.first_name,
    rental.rental_date
from
    customer

right join rental on customer.customer_id = rental.customer_id;

-- operator union.
SELECT first_name,last_name, 'Cliente' as tipo from customer
UNION
select first_name,last_name, 'Empleado' as tipo  from staff

ORDER BY tipo ASC
-- fusionar las dos partes con el UNION operator

SELECT * from rental
SELECT CURRENT_TIMESTAMP;

-- Disctict Method
-- https://leetcode.com/problems/article-views-i/
-- Write your PostgreSQL query statement below
SELECT DISTINCT  author_id as id FROM Views where author_id = viewer_id ORDER BY id ASC;

-- https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/1943495779/
-- # Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = 'Y';



-- LENGTH() Method
-- Write your PostgreSQL query statement below
SELECT tweet_id
from Tweets
where length (content) >15;