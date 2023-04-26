-- show me offical name and nationality for all person
select `official_name`,`is_indian` from person;

-- show me all person
select * from `person`;

-- show me all persons whos salary is greater than 30000
select * from `person` where `salary`>30000;
-- to see the count
select count(*) from `person` where `salary`>30000;

-- tell what is average salary of all employees
select avg(`salary`) from `person`;

-- tell what is sum of salary of all employees
select sum(`salary`) from `person`;

-- show all employees who born after 12 april 2018
select * from `person` where `dob`>'2018-04-12';
-- how many employees are there who born after 12 april 2018
select count(*) from `person` where `dob`>'2018-04-12';


-- how employees are there who age is between 20 to 60
select count(*) from `person` where timestampdiff(year,`dob`,curdate()) between 5 and 60;

-- print age of all employees
select `official_name` as `Name` , TIMESTAMPDIFF(YEAR, `dob`, CURDATE()) as `Age` from `person`; 

-- between
select 1000 between 5 and 100;

-- here 1 represents truth
select * from `person` where 1; 

desc `person`;

-- give me all the emp who name start with a or A
select * from `person` where `official_name` like 'a%';
select count(*) from `person` where `official_name` like 'a%';

-- give me all the emp who name ends with a or A
select * from `person` where `official_name` like '%a';
select count(*) from `person` where `official_name` like '%a';

-- give emp whose age is between 3 to 10
select count(*) from `person` where timestampdiff(year,`dob`,curdate()) between 3 and 10;

-- show me all emp in desc order
select * from `person` order by `official_name` desc;

alter table `person` add column `country` varchar(20);
