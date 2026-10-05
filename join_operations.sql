use shop;
-- create table product (pid int primary key,pname varchar(20),price int);
-- create table order_details(order_id int primary key,p_id int,quatity int,date date,foreign key(p_id) references product(pid));
-- insert into product(pid,pname,price) values(1,'poda',1000),(2,'podb',500),(3,'podc',400),(4,'podd',580),(5,'pode',200);
-- insert into order_details(order_id,p_id,quatity,date)values(1,2,2,"2026-08-12"),(2,3,1,"2026-08-13"); 
-- select * from product;
-- select * from order_details;
-- select * from product
-- inner join order_details
-- on product.pid=order_details.p_id;
-- select pname,price,order_id from product
-- inner join order_details
-- on product.pid=order_details.p_id;
-- select * from product
-- left join order_details
-- on product.pid=order_details.p_id;
select * from product
cross join order_details;
