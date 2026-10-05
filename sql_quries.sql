-- SELECT * FROM mydb2.employee;
use mydb2;
-- select name,age from employee;
-- select * from employee where (empid!= 102)
-- update employee set age=28 where empid=102;
-- select * from employee limit 1;
-- select * from employee limit 2;
-- select * from employee limit 1 offset 1;
-- select * from employee limit 2 offset 2;
-- select count(*) from employee;
-- select sum(salary) from employee;
-- select max(salary) from employee;
-- select min(age) from employee;
-- select sum(salary),max(salary),min(age) from employee;
-- select gender,sum(salary)
-- from employee
-- group by  gender;
-- select gender ,count(gender) from employee group by gender;
-- select place,max(salary) from employee group by place
-- select place,sum(salary)
--  from employee
--  group by  place; 
select place ,sum(salary) 
from  employee
 group by place
 having place="kochi"