create table demo(
    tid int,
    u_id varchar2 (20),
    created_date date,
    p_id varchar2 (20),
    quantity number(10)
)

    
insert into Demo values(1, 'U1', '16-DEC-20', 'P1', 2)
insert into Demo values(2, 'U2', '16-DEC-20', 'P2', 1)
insert into Demo values(3, 'U1', '16-DEC-20', 'P3', 1)
insert into Demo values(4, 'U4', '16-DEC-20', 'P4', 4)
insert into Demo values(5, 'U2', '17-DEC-20', 'P5', 3)
insert into Demo values(6, 'U2', '17-DEC-20', 'P6', 2)
insert into Demo values(7, 'U4', '18-DEC-20', 'P7', 1)
insert into Demo values(8, 'U3', '19-DEC-20', 'P8', 2)
insert into Demo values(9, 'U3', '19-DEC-20', 'P9', 8)

select * from demo

-- Find the number of users who purchased product on multiple days (note that user can purchase multiple products on a day)
select u_id, count(distinct created_date) as days
from Demo
group by u_id
having count(distinct created_date) > 1

create table Demo2(
    U_id int,
    start_date date,
    end_date date
)

insert into Demo2 values('U1', '1-Jan-20', '31-JAN-20')
insert into Demo2 values('U2', '12-Dec-20', '26-JAN-20')
insert into Demo2 values('U3', '28-Jan-20', '06-FEB-20')
insert into Demo2 values('U4', '16-Feb-20', '26-FEB-20')

select * from Demo2
-- Write a query that returns true or false for user based on the overlapping dates with other users. If U1's subscription period overlaps with any other user's subscription period, then return true, else return false.

select a.u_id, 
case 
    when exists (select 1 from Demo2 b where a.u_id <> b.u_id and a.start_date <= b.end_date and a.end_date >= b.start_date) then 'true' 
    else 'false' 
end 
as overlap
from Demo2 a

Question 3

create table input(
    id int,
    name varchar2(20),
    profession varchar2(20)
)

insert into input values(1, 'Sam', 'Doctor')
insert into input values(2, 'Shyam', 'Actor')
insert into input values(3, 'Samuel', 'Cricketer')
insert into input values(4, 'Sammy', 'Singer')

select * from input

-- Query all the names immediately followed by the first letter in the profession column enclosed in parathesis. For example, if the profession is "Actor", then the output should be "Actor (A)".

Method 1
select name || '(' || substr(profession, 1, 1) || ')' as Output from Input

Method 2 Using Concat
select concat(name, concat('(', concat(substr(profession, 1, 1), ')'))) as Output from Input