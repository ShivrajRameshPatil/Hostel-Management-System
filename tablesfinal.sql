
#----------------------------------------------------------------------HOSTEL MANAGEMENT SYSTEM ---------------------------------------------------------------------------------
#DDL STATEMENTS :-
create database hostelsm;

use hostelsm;

#HOSTEL TABLE :-
	create table Hostel(Hostel_ID int primary key,Hostel_Name varchar(30) not null,Hostel_Addr varchar(50),HostelType varchar(30) not null);

#ROOM TABLE :-
	create table Room(Hostel_ID int,Room_ID int,Beds int Default 3,check(Beds<=3 and Beds>0),
					Room_type varchar(30) default "Normal",Price decimal(8.2) not null default 75000.00,primary key(Hostel_ID,Room_ID),
					foreign key(Hostel_ID) references Hostel(Hostel_ID) ON DELETE CASCADE ON UPDATE CASCADE);

#EMPLOYEE TABLE:-
	create table Employee(Emp_Id int primary key auto_increment,Emp_Name varchar(30) not null,Emp_Addr varchar(50) not null,hire_date date not null,
					E_Role varchar(30),Hostel_ID int,foreign key(Hostel_ID) references Hostel(Hostel_ID) ON DELETE CASCADE ON UPDATE CASCADE );

#STUDENT TABLE :-
	create table Student(St_ID int primary key,Firstn varchar(30) not null,Lastn varchar(30) not null,Gender varchar(30),Face longblob,ID_Proof longblob not null,
	Aptno varchar(6),Buidg varchar(30),Street varchar(20),City varchar(30),State varchar(30),verify int default 0);

#GUARDIAN TABLE :-
	create table Guardian(St_ID int,G_ID int,G_Name varchar(30) not null,G_Role varchar(30) Default "Guardian",
	G_Addr varchar(50),G_phone varchar(10) not null,primary key(St_ID,G_ID),foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE);

#STUDENT PHONE TABLE :-
	create table Std_Phone(St_ID int,PhoneNo varchar(11) not null,foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE);

#ROOM TABLE :-
	create table books(Hostel_ID int,Room_ID int,St_ID int,Booking_ID int auto_increment ,
		Booking_Date date,Joining_Date date,UNIQUE(Booking_ID), verify int default 0,
		primary key(Hostel_ID,Room_ID,St_ID,Booking_ID),
		foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE,
		foreign key(Hostel_ID,Room_ID) references Room(Hostel_ID,Room_ID)ON DELETE CASCADE ON UPDATE CASCADE);
	
#PAYMENT IN INSTALLATIONS :-
	create table payment(Payment_ID int primary key auto_increment,Payment_Type varchar(30) not null,Payment_Amount decimal(8,2),
			Payment_Date date ,PaymentSS longblob ,Booking_ID int,foreign key(Booking_ID) references Books(Booking_ID) ON DELETE CASCADE ON UPDATE CASCADE);
        
#TEMPORARY TABLES :-
	CREATE TABLE bookingrem(countr int,roomid int);
	CREATE TABLE complaints(st_id int , complaint varchar(100) , foreign key (st_id) references student(st_id) ON DELETE CASCADE ON UPDATE CASCADE);

    alter table employee auto_increment=1001;
	alter table books add end_date date ;
    alter table student modify face longblob not null;
	alter table complaints add `status` int default 0;
	alter table complaints drop verify ;
    alter table complaints add `c_date` date;
    desc complaints;
    