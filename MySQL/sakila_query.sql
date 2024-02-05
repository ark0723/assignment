use sakila;

# 특정 배우가 출연한 영화 목록 조회
select film.film_id, film.title from film join film_actor on film.film_id =  film_actor.film_id
where film_actor.actor_id = (select actor_id from actor where (first_name = "JOHNNY" and last_name = "LOLLOBRIGIDA"))
order by actor_id;

# 모든 카테고리와 해당 카테고리의 영화 수 조회
select count(f.film_id), c.name from film_category f join category c
on f.category_id = c.category_id group by c.category_id;

# 특정 고객의 대여 기록 조회
select rental_id, rental_date, inventory_id, r.customer_id, return_date, staff_id from rental r 
inner join customer c on r.customer_id = c.customer_id where c.customer_id = 5;

# 가장 최근에 추가된 10개의 영화 조회
select * from film order by release_year desc limit 10;

# 특정 영화에 출연한 배우 목록 조회
select a.actor_id, a.first_name, a.last_name from actor a join film_actor f 
on a.actor_id = f.actor_id where film_id = (select film_id from film where title = "ACADEMY DINOSAUR");

# 특정 영화를 대여한 고객 목록 조회
select c.customer_id, c.first_name, c.last_name from customer c join rental r 
on r.customer_id = c.customer_id 
where r.inventory_id in (select i.inventory_id from inventory i join film f
on i.film_id = f.film_id where f.title = "ACADEMY DINOSAUR");

# 모든 고객과 그들이 가장 최근에 대여한 영화 조회
-- select * from rental; # rental_date, inventory_id, customer_id
-- select * from inventory; # film_id, inventory_id
-- select * from film; # film_id, 

select f.title, r.customer_id, max(r.rental_date) as latest_date from film f 
join inventory i on f.film_id = i.film_id
join rental r on r.inventory_id = i.inventory_id group by r.customer_id, r.title order by customer_id, latest_date desc;

#각 영화별 평균 대여 기간 조회
-- select * from rental; # inventory_id, customer_id, rental_id, return_date - rental_date
-- select * from inventory; # inventory_id, film_id
-- select * from film; # film_id, rental_duration

select i.film_id, avg(Datediff(r.return_date,r.rental_date)) as rent_period 
from rental r join inventory i on r.inventory_id = i.inventory_id group by i.film_id;

# 가장 많이 대여된 영화의 제목과 대여 횟수를 조회
select f.film_id, f.title, count(*) as rent_count
from rental r join inventory i on r.inventory_id = i.inventory_id 
join film f on f.film_id = i.film_id
group by i.film_id
order by rent_count desc limit 1;

# 각 카테고리별 평균 대여 요금 조회
-- select * from category;# category_id, name(genre)
-- select * from film_category; # film_id, category_id
-- select * from film; # film_id, title, rental_rate

select fc.category_id, c.name, avg(f.rental_rate) from film f
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
group by c.category_id;

# 각 월별 총 매출 
-- select * from payment;
select month(payment_date), sum(amount) from payment group by month(payment_date);

# 각 배우별 출연한 영화 수 조회
-- select * from actor; # actor_id, first_name, last_name
-- select * from film_actor; # actor_id, film_id
select a.first_name, a.last_name, count(film_id) from actor a
join film_actor f on a.actor_id = f.actor_id group by a.actor_id;

# 가장 수익이 많은 영화의 제목과 수익을 조회
-- select * from payment; # rental_id, amount
-- select * from rental; # rental_id, inventory_id
-- select * from inventory; # inventory_id, film_id
-- select * from film; # film_id, title

select f.title, sum(p.amount) as movie_revenue from payment p join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id group by f.film_id order by movie_revenue desc;

# 평균 대여 요금보다 높은 요금의 영화 조회
-- select * from film; #rental_rate
select film_id, title from film 
where rental_rate > (select avg(rental_rate) from film);

# 가장 활동적인 고객 조회: 가장 많은 영화를 대여한 고객의 이름과 대여 횟수
select * from rental; # rental_id, customer_id
select * from customer; #customer_id, fist_name, last_name
select c.first_name, c.last_name, count(r.rental_id) from rental r 
join customer c on r.customer_id = c.customer_id
group by c.customer_id order by count(r.rental_id) desc;

# 특정 배우가 출연한 영화 중 가장 대여된 영화의 제목과 대여횟수 조회
# rental: rental_id, inventory_id
-- select * from inventory; # film_id, inventory_id
-- select * from film; # film_id, title
-- select * from film_actor; # actor_id, film_id
-- select * from actor; # actor_id, first_name, last_name

select f.title, count(r.rental_id) as total_count from rental r
join inventory i on r.inventory_id = i.inventory_id
join film f on f.film_id = i.film_id 
join film_actor fa on fa.film_id = f.film_id
where fa.actor_id = (select actor_id from actor where first_name = "PENELOPE" and last_name ="GUINESS")
group by f.film_id order by total_count desc;

# 'film' 테이블에 'New Adventure Movie'라는 새로운 영화를 추가하시오.
INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries');

# 고객 ID가 5인 고객의 주소를 '47 MySakila Drive, Alberta'로 변경하시오.
update customer set address_id = (select address_id from address where address = "47 MySakila Drive" and district = "Alberta")
where customer_id = 5;

# 영화 대여 상태 변경: rental_ID가 200인 대여 기록의 상태를 'returned'으로 변경하시오
update rental set return_date = now() where rental_id = 200;

# 배우 id가 10인 배우의 정보를 삭제하시오
delete from film_actor where actor_id = 10; # foreign key - delete first
delete from actor where actor_id = 10;
