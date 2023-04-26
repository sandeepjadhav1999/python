-- mysql workbench is a client not a databse
-- to create a databse we use a query called "create"

create database `sandeepdb`;
-- to enter insde the database we use a query called "use"
use `sandeepdb`;

-- to create a table we user "create table"
create table `student`(
	-- <column_name>  <datatype>
    `roll_no` int,
    `name` varchar(10)
);


-- store the information of shop, which has shop_act_num, shop_name, address, road , phone
create table `shop_details`(
	shop_ac_num int,
    shop_name varchar(10),
    address varchar(50),
    road varchar(20),
    is_road boolean,
    phone varchar(10) primary key
);
-- to see all the tables present v use "show table"
show tables;

-- drop table  completely deletes the table from the databse
-- truncate table deletes the data inside the table but not the table


-- to delete a column from a table or to alter table we use "alter table `table_name` drop column `column_name`;
alter table `shop_details` drop column `is_road`;

-- to describe the table "desc `table_name`;
desc `shop_details`;

-- to add coulmns to the table we use alter table `table_name` add column `column_name` and datetype
alter table `shop_details` add column `toll` int;

-- to insert values in the table we use "inster into `table_name` values(data);

insert into `shop_details` value(1,'abc','pqr pqrpq','123pqr','1234567890',1);


-- to see the date in the table we use "select * from `table_name`;
select * from `shop_details`;
insert into `shop_details` value(2,'qwe','asd fghj','123per','1234567891',2);
insert into `shop_details` value(3,'rty','zxc vbnm','123ptr','1234567892',3);
insert into `shop_details` value(4,'uio','pqr qwe','123por','1234567894',4);

-- to update the table we use "update table_name set column=value where condition:
update `shop_details` set `shop_name` = 'klo' where `shop_ac_num` = 2;