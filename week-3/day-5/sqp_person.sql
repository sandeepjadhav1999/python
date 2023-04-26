-- thy are 2 ways to add constraints if u knw the constraints will creating the table add them there itself
create table `person`(
		`adhar_id` varchar(20),
        `official_name` varchar(10) default 'abc',
        `dob` date,
        `is_indian` boolean default true,
        `salary` int
);
desc `person`;
select *from `person`;
drop table `person`;

-- 2nd way of adding constraints 

alter table `person` add primary key(`adhar_id`);
alter table `person` modify `dob` date not null;

-- to insert values in a particulare oly
insert into `person`(`adhar_id`,`dob`) values('1234','2021-01-01');
insert into `person` values('1235','sandeep','2020-09-09',true);
