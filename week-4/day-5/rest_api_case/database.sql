create database `bankcasestudy`;
use `bankcasestudy`;

create table `app_user` (
	`user_id` bigint primary key,
    `user_name` varchar(20) unique,
    `password` varchar(20),
    `role` varchar(10)
);

create table `bank_account`(
	`ac_num` varchar(16),
    `ac_id` bigint,
    `ac_sts` bool default false,
    `balance` int default 0
);

alter table `bank_account` add constraint primary key(`ac_num`);
alter table `bank_account` add constraint foreign key(`ac_id`) references `app_user`(`user_id`);


-- create trigger
delimiter $$
create trigger `bank_acc_num`
after insert
on `app_user`
for each row
begin

if (new.`role`='user')then
	insert into `bank_account` values(new.`user_id`+19990000,new.`user_id`,false,0);
end if;
end $$

-- end trigger

create table `account_transactions`(
	`txn_id` bigint,
    `txn_dt` date,
    `txn_type` int,
    `amt` decimal,
    `acc_num` varchar(20)
);

alter table `account_transactions` add constraint primary key(`txn_id`);
alter table `account_transactions` add constraint foreign key(`acc_num`) references `bank_account` (`ac_num`);


create table `deposit`(
	`acc_num_deposit` varchar(16),
    `amt` decimal,
    `txn_type` int default 1
);
alter table `deposit` add constraint foreign key (`acc_num_deposit`) references `bank_account`(`ac_num`); 
 
 
 drop trigger `update_balance_for_deposite`;
delimiter $$
create trigger `update_balance_for_deposite`

after insert on `deposit`
for each row 
begin
declare dt date;
declare last_txn_id integer;

	set @dt :=(select curdate());
    set @last_txn_id := (select `txn_id` from `account_transactions` order by `txn_id` desc limit 1);
	if (@last_txn_id is NULL) then
		set @last_txn_id:= 0;
	end if;
	insert into `account_transactions` values (@last_txn_id + 1 , @dt, 1, new.`amt`, new.`acc_num_deposit`);

update `bank_account`
set `balance` = `balance`  + new.`amt`
where `ac_num` = new.`acc_num_deposit`;
       
end $$






create table `withdraw`(
	`acc_num_withdraw` varchar(16),
    `amt` decimal,
    `txn_type` int default 1
);
alter table `withdraw` add constraint foreign key (`acc_num_withdraw`) references `bank_account`(`ac_num`); 
 
 

delimiter $$
create trigger `update_balance_for_withdraw`

after insert on `withdraw`
for each row 
begin
declare dt date;
declare last_txn_id integer;

	set @dt :=(select curdate());
    set @last_txn_id := (select `txn_id` from `account_transactions` order by `txn_id` desc limit 1);
	if (@last_txn_id is NULL) then
		set @last_txn_id:= 0;
	end if;
	insert into `account_transactions` values (@last_txn_id + 1 , @dt, 1, new.`amt`, new.`acc_num_withdraw`);

update `bank_account`
set `balance` = `balance` - new.`amt`
where `ac_num` = new.`acc_num_withdraw`;
       
end $$








-- transfer table
create table `transfer`(
	`src_acc` varchar(16),
    `tar_acc` varchar(16),
    `amt` decimal,
    `txn_type` int default 3
);
alter table `transfer` add constraint foreign key(`src_acc`) references `bank_account`(`ac_num`);
alter table `transfer` add constraint foreign key(`tar_acc`) references `bank_account`(`ac_num`);


-- start of trigger function

delimiter $$
create trigger `update_balance_for_transfer`
after insert 
on `transfer`
for each row 
begin
declare at date;
declare last_txn_id integer;
	set @dt :=(select curdate());
    set @last_txn_id := (select `txn_id` from `account_transactions` order by `txn_id` desc limit 1);
	
    if (@last_txn_id is NULL) then
		set @last_txn_id:= 0;
        end if;
    
    insert into `account_transactions` values (@last_txn_id + 1 , @dt, 1, new.`amt`, new.`src_acc`);

update `bank_account`
set `balance` = `balance`  - new.`amt`
where `ac_num` = new.`src_acc`;

update `bank_account`
set `balance` = `balance`  + new.`amt`
where `ac_num` = new.`tar_acc`;
       
end $$




-- operation 
select * from `app_user`;
select * from `bank_account`;
select * from `account_transactions`;
select * from `deposit`;
select * from `withdraw`;

insert into `app_user` values(1,'sandeepjadhav','123456789','user');
insert into `app_user` values(2,'asdfghjklqw','123456780','user');
insert into `deposit` values (19990001,100,1);
insert into `withdraw` values(19990001,50,2);
insert into `transfer` values(19990001,19990002,25,3);



