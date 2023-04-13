CREATE TABLE emp(
EMPNO NUMBER(4) NOT NULL,
ENAME VARCHAR2(10),
JOB VARCHAR2(9),
MGR NUMBER(4),
HIREDATE DATE,
SAL NUMBER(7,2),
COMM NUMBER(7,2),
DEPTNO NUMBER(2));

CREATE TABLE dept(
DEPTNO NUMBER(2) NOT NULL,
DNAME VARCHAR2(14),
LOC VARCHAR2(13));

INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7369 ,'SMITH','CLERK',7902,'17-DEC-1980',800,NULL,20);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7499 ,'ALLEN','SALESMAN',7698,'20-FEB-1981',1600,300,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7521 ,'WARD','SALESMAN',7698,' 22-FEB-1981',1250,500,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7566, 'JONES','MANAGER',7839,' 02-APR-1981',2975 ,NULL,20);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7654, 'MARTIN','SALESMAN',7698 ,'28-SEP-1981',1250,1400,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7698, 'BLAKE','MANAGER',7839,' 01-MAY-1981',2850,NULL,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7782, 'CLARK','MANAGER',7839 ,'09-JUN-1981' ,2450 ,NULL,10);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7788, 'SCOTT','ANALYST', 7566 ,' 19-APR-1987' ,3000 ,NULL,20);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7839, 'KING','PRESIDENT',NULL, '17-NOV-1981', 5000,NULL,10);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7844, 'TURNER','SALESMAN',7698,'08-SEP-1981',1500,0,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7876, 'ADAMS','CLERK',7788,'23-MAY-1987',1100 ,NULL,20);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7900, 'JAMES','CLERK',7698, '03-DEC-1981', 950 ,NULL,30);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7902, 'FORD','ANALYST',7566, '03-DEC-1981',3000 ,NULL,20);
INSERT INTO emp(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO) VALUES
(7934, 'MILLER','CLERK',7782, '23-JAN-1982',1300 ,NULL,10);

INSERT INTO dept VALUES
(10,'ACCOUNTIING','NEW YORK');
INSERT INTO dept VALUES
(20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES
(30,'SALES','CHICAGO');
INSERT INTO dept VALUES
(40,'OPERATIONS','BOSTON');

-- list the ename, job, sal of the employee who get minimum salary in the company
select ename, job, sal
from emp
where sal = (select min(sal) from emp)

-- list the name of the employees whose salary is greater than that of employee with empno 7566
select ename
from emp
where sal > (select sal from emp where empno = 7566)

-- displays employee whose job title is the same as that of employee 7369 and whose salary is greater than that of employee 7876
select ename, job, sal
from emp
where job = (select job from emp where empno = 7369) and sal > (select sal from emp where empno = 7876)

-- display the employee details whose salary is greater than the average salary of employees
select ename, job, sal
from emp
where sal > (select avg(sal) from emp)

-- display lowest paid employee details under each manager
select mgr, ename, job, sal
from emp e1
where sal = (select min(sal) from emp e2 group by mgr having e1.mgr = e2.mgr);

-- display the salary with increment of 10% for employees whose job title is the same as that of employee 7499
select ename, job, sal, sal * 1.1
from emp
where job = (select job from emp where empno = 7499)

-- list deptno and min(salary) dept wise, only if min(salary) is greater than the min(sal) of deptno 20
select deptno, min(sal)
from emp
group by deptno
having min(sal) > (select min(sal) from emp where deptno = 20)

-- list empno, ename, job of the employees whose salary is greater than the average salary of employees in each dept
select mgr, ename, job, sal
from emp e1
where sal > ALL(select avg(sal) from emp group by deptno)

-- display the name dept no, salary, and commission of any employee whose salary and commission matches both the commission and salary of any employee in department 30
select ename, deptno, sal, comm 
from emp 
where (sal, nvl(comm, -1)) in (select sal, nvl(comm, -1) from emp where deptno = 30);

-- list ename, job, deptno, sal of the employees whose job is same as 'Jones' and salary is greater than the employee 'ford'
select ename, job, deptno, sal
from emp
where job = (select job from emp where ename = 'JONES') and sal > (select sal from emp where ename = 'FORD')