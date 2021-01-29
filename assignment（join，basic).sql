SELECT *
FROM customer;

SELECT first_name, last_name, email
FROM customer;

SELECT *
FROM film;

SELECT DISTINCT release_year
FROM film;

SELECT DISTINCT rental_rate
FROM film;

SELECT email
FROM customer
WHERE first_name = 'Nancy' AND last_name = 'Thomas'

SELECT *
FROM address;

SELECT phone 
FROM address
WHERE address = '259 Ipoh Drive';

SELECT *
FROM customer
WHERE store_id = 1 AND address_id > 150;

SELECT *
FROM payment
WHERE amount = 4.99 OR amount = 1.99;

SELECT payment_id
FROM payment
WHERE amount >5;

SELECT*
FROM film_actor
JOIN film
ON film_actor.film_id = film.film_id;

SELECT *
FROM actor;

SELECT*
FROM film_actor
JOIN actor
ON film_actor.actor_id = actor.actor_id;

SELECT*
FROM film_actor
JOIN film
ON film_actor.film_id = film.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id;


