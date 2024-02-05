use classicmodels;

# 고객 조회
select * from customers;

# 특정 제품 라인의 제품 조회: 'Classic Cars'제품 라인에 속하는 모든 제품의 이름과 가격을 조회
-- select * from products;
select productName, MSRP from products
where productLine = 'Classic Cars';

# 가장 최근에 주문된 10개의 주문을 주문날짜(orderDate)와 함께 조회
-- select * from orders;
SELECT 
    *
FROM
    orders
ORDER BY orderdate DESC
LIMIT 10;

# 최소 금액 이상의 결제: 100 달러 이상 결제된 거래(amount)만 조회
select * from payments where amount >= 100;

# join query
# 각 주문에 대한 주문번호와 주문한 고객의 이름을 조회
select orderNumber, customerName from orders as o join customers as c 
on o.customerNumber = c.customerNumber;

# 각 제품의 이름(products-productName)과 속한 제품라인의 설명(productlines - textDescription)을 조회
select productName, line.productLine, textDescription from products as item join productlines as line
on item.productLine = line.productLine; 

# 각 직원의 이름과 직속상사의 이름을 조회
 select * from employees;
 select sub.employeeNumber, sub.lastName, sub.firstName, sub.reportsTo, boss.lastName, boss.firstName from employees sub left join employees boss
 on sub.reportsTo = boss.employeeNumber;
 
 # 특정 사무실의 직원 목록: 'San Francisco'사무실에 근무하는 모든 직원들의 이름을 조회
-- select * from offices;
select e.lastName, e.firstName, o.city from employees e join offices o
on e.officeCode = o.officeCode
where o.city = 'San Francisco';

# Group by 
-- select * from products;
select productLine, count(*) from products 
group by productLine;

# 고객별 총 주문금액
# first method
select c.customerNumber, c.customerName, sum(d.quantityOrdered*d.priceEach) as total_amount
from customers as c join orders as o on c.customerNumber = o.customerNumber
join orderdetails as d on o.orderNumber = d.orderNumber
group by c.customerNumber;

# second method
select c.customerNumber, c.customerName, sum(p.amount) as total_amount
from payments p join customers c on c.customerNumber = p.customerNumber
group by c.customerNumber
order by total_amount desc;

# 가장 많이 팔린 제품의 이름과 판매 수량을 조회
select * from orderdetails;
select p.productCode, p.productName, sum(o.quantityOrdered) as productSale from products as p
join orderdetails as o on p.productCode = o.productCode
group by p.productCode
order by productSale desc
limit 1;

# 매출이 가장 높은 사무실의 위치와 매출액을 조회
select offices.officeCode, offices.city, sum(payments.amount) as totalSales
from offices 
join employees on offices.officeCode = employees.officeCode
join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
join payments on customers.customerNumber = payments.customerNumber
group by offices.officeCode
order by totalSales desc;
-- limit 1;

# sub-query
# 특정 금액 이상의 주문: 500달러 이상의 총 주문 금액을 기록한 주문들을 조회
select * from orderdetails;
select orderNumber, sum(quantityOrdered*priceEach) as total_price
from orderdetails
group by orderNumber
having total_price >= 500; # having: group으로 묶여있을때 조건을 준다

# 평균 이상 결제 고객: 평균 결제 금액보다 많은 금액을 결제한 고객들의 목록을 조회
select avg(amount) from payments;
select c.customerName, sum(p.amount) as totalPayment from customers c
join payments p on c.customerNumber = p.customerNumber
group by p.customerNumber
having totalPayment > (select avg(amount) from payments);

# 아직 주문을 하지 않은 고객의 목록
select customerNumber, customerName from customers
where customerNumber not in (select customerNumber from orders);

# 최대 매출 고객: 가장많은 금액을 지불한 고객의 이름과 총 결제 금액을 조회
select * from payments;
select c.customerName, sum(p.amount) as totalpay from customers c
join payments p on c.customerNumber = p.customerNumber
group by p.customerNumber
order by totalpay desc
limit 1;

# 데이터 수정 및 관리
# 신규 고객 추가
INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

-- select * from products;
# 제품 가격 변경: 'Classic Cars'제품 라인의 모든 제품 가격을 10% 인상하는 쿼리를 작성
update products
set MSRP = MSRP * 1.1
where productLine = 'Classic Cars';

select * from customers;
# 고객 업데이트: 특정 고객의 이메일 주소 변경하는 쿼리
update customers
set email = "aaa@examples.com"
where customerNumber = 100;

# 특정직원을 다른 사무실로 이동시키는 쿼리
update employees
set officeCode = '1'
where employeeNumber = 100;
