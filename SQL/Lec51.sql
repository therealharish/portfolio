create table employee (
    id int, 
    name varchar(20)
)

alter table employee add address varchar(20)
desc employee


-- change length of varchar of id
alter table employee modify id varchar(30);

-- rename column id to rollno
alter table employee rename column id to rollno

-- rename table to emp
alter table employee rename to emp
desc emp
    
-- make rollno the primary key
alter table emp add primary key(rollno)

