create database HSM;							#hotel management system
use HSM;									

create table hotel(hotelno int primary key,hotelname varchar(30) not null, city varchar(30));
insert into hotel values(100,'Taj','Pune');
insert into hotel values(101,'Taj','Mumbai');
insert into hotel values(200,'Hyatt','Mumbai');
insert into hotel values(201,'Hyatt','Delhi');
insert into hotel(hotelno,hotelname) values (202,'Hyatt');
select *from hotel;

create table room(roomno int,roomtype varchar(30) Default "Double",price decimal(6,2),hotelno int,check (price>1500.00), primary key (hotelno,roomno), foreign key (hotelno) references hotel(hotelno));
insert into room(roomno,price,hotelno) values (101,1550.00,100);
insert into room values (201,"single",1550.00,101);
insert into room(roomno,price,hotelno) values (302,2000.00,101);
insert into room(roomno,price,hotelno) values (202,1700.00,202);
insert into room(roomno,price,hotelno) values (204,2000.00,100);
insert into room(roomno,price,hotelno) values (306,2000.00,101);
insert into room values (305,"single",1550.00,101);
insert into room values (203,"single",2000.00,100);
insert into room(roomno,price,hotelno) values (603,2000.00,100);
insert into room(roomno,price,hotelno) values (402,2000.00,202);
insert into room(roomno,price,hotelno) values (208,2000.00,202);
select *from room;


desc hotel;															#describe table columns
desc room;
show tables;														#to show all tables created
drop table guest;
drop table bookings;
create table guest(guestno varchar(5) primary key,guestname varchar(30),guestaddr varchar(30));
create table bookings(hotelno int,roomno int,guestno varchar(5), foreign key(guestno) references guest(guestno), datefrom date,dateto date, primary key(hotelno,roomno,guestno,datefrom), foreign key (hotelno,roomno) references room(hotelno,roomno)); 
insert into guest values("P01","Shweta","pune");
insert into guest values("P02","Vedant","Mumbai");
insert into guest values("P03","Shweta","Mumbai");
insert into guest values("P04","Shweta","Delhi");
insert into guest values("P05","bharati","Pune");
insert into guest values("P11","Rajesh","Mumbai");
insert into guest values("P07","Vidhi","Mumbai");
insert into guest values("P12","Roma","Mumbai");

-- Alter command 

alter table hotel add rating char(5);

alter table hotel drop column rating;

-- USE OF DISTINT KEYWORD 
select distinct hotelname from hotel;

-- CALCULATED FIELDS 
select hotelname,length(hotelname) size from hotel;
select *from hotel;
select curdate();          #current date

#select datediff(curdate(),dob) age from student ; 			#derived attribute

-- WHERE CLAUSE 
select *from room;
select roomno,roomtype from room where price>1600;
