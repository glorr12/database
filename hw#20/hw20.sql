use sakila;

select title,
		rating,
case rating
	when 'G' then 'All ages admitted. Nothing that would offend parents for viewing by children'
    when 'PG' then 'Some material may not be suitable for children. Parents urged to give "parental guidance". May contain some material parents might not like for their young children.'
    when 'PG-13' then 'Some material may be inappropriate for children under 13. Parents are urged to be cautious. Some material may be inappropriate for pre-teenagers.'
    when 'R' then 'Under 17 requires accompanying parent or adult guardian. Contains some adult material. Parents are urged to learn more about the film before taking their young children with them'
    when 'NC-17' then 'No one 17 and under admitted. Clearly adult. Children are not admitted.'
end as rate_description
from film;


select rating,
	count(*) as total_count
from film
group by rating
order by total_count desc;


select title,
		rating,
        count(*) over(partition by rating) as films_in_rating
from film
order by rating,title;


select c.first_name,
		c.last_name,
        p.payment_date,
        p.amount
from payment p	
join customer c on p.customer_id = c.customer_id
order by p.payment_date;

SELECT
    c.first_name,
    c.last_name,
    DATE_FORMAT(p.payment_date, '%e %M %Y') AS payment_date,
    p.amount
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
ORDER BY p.payment_date;
