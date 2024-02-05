USE yes24;

# 기본 조회 및 필터링
SELECT title, author FROM Books;
select * from Books where rating >= 8; 
select title, review from Books where review >= 100;
select title, price from Books where price < 20000;
select * from Books where author = "최태성 저";
select * from Books where ranking_weeks >=4 order by ranking_weeks DESC;
select * from Books where publisher = "YBM(와이비엠)";

# 조인 및 관계
select author, count(title) from Books group by author;  
select publisher, count(title) from Books group by publisher order by count(title) desc limit 1;
select author, avg(rating) from Books group by author order by avg(rating) desc;
select title, author from Books where ranking = 1;
select * from Books order by sales desc, review desc limit 10;
select * from Books order by publishing desc limit 5;

# 집계 그룹화
select author, avg(rating) from Books group by author order by avg(rating) desc;
select publishing, count(title) from Books group by publishing order by publishing desc;
select title, avg(price) from Books group by title;
select * from Books order by review desc limit 5;
select ranking, avg(review) from books group by ranking order by ranking;

# 서브쿼리 및 고급기능
select * from Books where rating >= (select avg(rating) from Books);
select * from Books where price >= (select avg(price) from Books);
select * from Books where review > (select max(review) from Books);
select * from Books where sales < (select avg(sales) from Books);

# 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회하세요.
select * from Books where author = (select author from Books group by author order by count(title) desc limit 1) order by publishing desc;

Insert into Books(title, author, publisher, rating, sales)
values ('aaa', 'ara', 'UofA', 8.0, 10);
set SQL_SAFE_UPDATES = 0;  # disable safe mode

# 특정 책의 가격을 업데이트하세요.
update Books set price = 20000 where author = 'ara';

# 특정 저자의 책 제목을 변경하세요.
update Books set title = "집으로" where author = "ara";

#판매지수가 가장 낮은 책을 데이터베이스에서 삭제하세요.
# 밑의 문장은 문법상 문제가 없으나 에러 발생: MySQL의 특징으로 데이터를 추가나 갱신할 경우 동일한 테이블로 서브쿼리를 사용할 수 없도록 되어 있기 때문이다.
DELETE FROM Books WHERE sales = (select sales from (SELECT MIN(sales) FROM Books) as sub);

# 특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요.
Update Books set rating = rating + 1 where publisher = "UofA";

