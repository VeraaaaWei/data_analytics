SELECT *
from customer
limit 5;

SELECT * FROM actor ;

SELECT first_name, last_name
FROM actor

select rating
from film

select distinct rating
from film

select title, rating 
from film 
order by rating;

SELECT first_name, last_name, email
FROM customer;

select first_name, last_name, email
from customer
limit 5;

SELECT *
FROM film
WHERE rating = 'PG-13'

select title, rating
from film
where rating = 'G' and rating = 'PG-13'
order by rating

select title, rating
from film
where rating = 'G' or rating = 'PG-13'
order by rating

select title, rating
from film
where not rating = 'G'
order by rating

SELECT email
FROM customer
where first_name = 'Vera' and last_name = 'Mccoy'
