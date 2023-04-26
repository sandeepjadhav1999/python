use `crm_case_study`;
create database `crm_case_study`;
show tables;



-- CREATING TABLE FOR CRM USER
create table `crm_user`(
    `mobile` varchar(15),
    `password` varchar(20) not null,
    `doj` date not null,
    `role` varchar(10) not null,
    `status` boolean default 0
 );
alter table `crm_user` add constraint primary key(`mobile`);
-- END OF CRM USER TABLE





select * from `crm_user`;
-- CREATING TABLE FOR CUSTOMER
create table `crm_customer`(
    `mobile` varchar(15),
    `name` varchar(20),
    `email` varchar(15) unique,
    `dob` date,
    `location` varchar(20) not null,
    `status` boolean default 1
 );
alter table `crm_customer` add constraint primary key(`mobile`);
alter table `crm_customer` add `coupon_code` varchar(10);
-- END OF CUSTOMER

insert into `crm_customer`(`mobile`,`name`,`email`,`dob`,`location`,`status`) values ('7760847076','sandeepjadh','san@gmail.com','2020-01-01','dubai',1);






-- CREATING TABLE FOR KITCHEN 
create table `kitchen` (
    `kitchen_id`  int auto_increment primary key,
    `name` varchar(20),
    `price` int,
    `location` varchar(20)
 ); 
-- END OF KITCHEN

insert into `kitchen`(`name`,`price`,`location`) values('briyani',250,'bangalore');






-- CREATING TABLE FOR ORDER 
create table `orders` (
    `order_id` int auto_increment primary key,
    `customer_id_mobile` varchar(15) not null,
    `total_quantities` int not null,
    `total_price` int not null,
    `ordered_date` datetime default now()
);
alter table `orders` add constraint foreign key(`customer_id_mobile`) references `crm_customer`(`mobile`);
alter table `orders` add constraint foreign key(`kitchen_id`) references `kitchen`(`kitchen_id`);
-- END OF ORDERS

drop table `orders`;

select * from `orders`;






-- CREATING MENU TABLE
create table `menu`(
    `item_id` int auto_increment primary key,
    `item_name` varchar(50) not null,
    `price` float,
    `quantity` int default 1,
    `count` int default 0,
    `kitchen_id` int
);
alter table `menu` add constraint foreign key(`kitchen_id`) references `kitchen`(`kitchen_id`) on delete cascade;
-- END OF MENU

select * from `menu`;







-- CREATING CART TABLE
create table `cart` (
    `menu_item_id` int,
    `qty` int,
    `order_id` int
);
alter table `cart` add constraint foreign key(`order_id`) references `orders`(`order_id`);
alter table `cart` add constraint foreign key(`menu_item_id`) references `menu`(`item_id`);

-- END OF CART











-- CREATING PROMOTION TABLE
create table `promotion`(
    `promotion_id` varchar(10),
    `title` varchar(20),
    `text` varchar(20) not null,
    `st_dt` date,
    `end_dt` date
    
);

alter table `promotion` add constraint primary key(`promotion_id`);


drop table `promotion`;
-- END OF PROMOTION

insert into `promotion` values ('24SAS','25%OFF','sankranti offer','2022-02-01','2022-05-01');
insert into `promotion` values ('24AAA','30%OFF','Youth offer','2022-02-01','2022-05-01');
insert into `promotion` values ('24DDD','50%OFF','New Year offer','2022-02-01','2022-05-01');

select * from `promotion`;








-- CREATING PROMOTION AGE

create table `promotion_age`(
    `promotion_id` int,
    `st_ag` int,
    `ed_ag` int
);
alter table `promotion_age` add constraint foreign key(`promotion_id`) references `promotion`(`promotion_id`);

-- END OF PROMOTION AGE











-- CREATING PROMOTION LOCATION

create table `promotion_location`(
    `promotion_id` int,
    `location` varchar(10)
);
alter table `promotion_location` add constraint foreign key(`promotion_id`) references `promotion`(`promotion_id`);

-- END OF PROMOTION LOCATION






insert into `crm_user` values ('1234567887', '1234567876', '2020-01-01', 'admin', 1 );








delimiter $$
create trigger `create_menu`
after insert
on `kitchen`
for each row
begin 
	insert into `menu`(`item_name`,`price`,`kitchen_id`) values(new.`name`, new.`price`, new.`kitchen_id`);
end $$

select * from kitchen;

show tables;

delimiter $$
create trigger `promotion_insert`
after insert 
on `promotion`
for each row
begin 
	if (new.`title`='25%OFF') then
		update `crm_customer` set `coupon_code`=new.`promotion_id` where `location` in ('bangalore','chennai','mumbai');
	elseif (new.`title`='50%OFF') then
		update `crm_customer` set `coupon_code`=new.`promotion_id` where `dob` between '1972-01-01' and '1982-01-01';
	elseif (new.`title`='30%OFF') then
		update `crm_customer` set `coupon_code`=new.`promotion_id` where `dob` between '1999-01-01' and '2005-01-01';
    
    end if ;
    
end $$

drop trigger `promotion_insert`;

select * from `crm_customer`;

