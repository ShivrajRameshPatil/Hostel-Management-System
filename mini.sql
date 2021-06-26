
#----------------------------------------------------------------------HOSTEL MANAGEMENT SYSTEM ---------------------------------------------------------------------------------
#DDL STATEMENTS :-
create database hostelmanagementsystem;

use hostelmanagementsystem;

#HOSTEL TABLE :-
	create table Hostel(Hostel_ID int primary key,Hostel_Name varchar(30) not null,Hostel_Addr varchar(50),HostelType varchar(30) not null);

#ROOM TABLE :-
	create table Room(Hostel_ID int,Room_ID int,Beds int Default 3,check(Beds<=3 and Beds>0),
					Room_type varchar(30) default "Normal",Price decimal(8.2) not null default 75000.00,primary key(Hostel_ID,Room_ID),
					foreign key(Hostel_ID) references Hostel(Hostel_ID) ON DELETE CASCADE ON UPDATE CASCADE);

#EMPLOYEE TABLE :-
	create table Employee(Emp_Id int primary key,Emp_Name varchar(30) not null,Emp_Addr varchar(50) not null,hire_date date not null,
	E_Role varchar(30),Hostel_ID int,foreign key(Hostel_ID) references Hostel(Hostel_ID) ON DELETE CASCADE ON UPDATE CASCADE );


#STUDENT TABLE :-
	create table Student(St_ID int primary key,Firstn varchar(30) not null,Lastn varchar(30) not null,Gender varchar(30),Face longblob,ID_Proof longblob not null,
	Aptno varchar(6),Buidg varchar(30),Street varchar(20),City varchar(30),State varchar(30),verify int default 0);
	/*create table Student(St_ID int primary key,Firstn varchar(30) not null,Lastn varchar(30) not null,Gender varchar(30),
	Street varchar(20),City varchar(30),State varchar(30));*/
#Guardian Table
	create table Guardian(St_ID int,G_ID int,G_Name varchar(30) not null,G_Role varchar(30) Default "Guardian",
	G_Addr varchar(50),G_phone varchar(10) not null,primary key(St_ID,G_ID),foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE);

#STUDENT PHONE TABLE :-
	create table Std_Phone(St_ID int,PhoneNo varchar(11) not null,foreign key(St_ID) references Student1(St_ID) ON DELETE CASCADE ON UPDATE CASCADE);

/*#GUARDAIAN TABLE :-
	create table Guardian(St_ID int,G_ID int,G_Name varchar(30) not null,G_Role varchar(30) Default "Guardian",
	G_Addr varchar(50),primary key(St_ID,G_ID),foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE);*/

#ROOM TABLE :-
	create table books(Hostel_ID int,Room_ID int,St_ID int,Booking_ID int,
		Booking_Date date,Joining_Date date,UNIQUE(Booking_ID),
		primary key(Hostel_ID,Room_ID,St_ID,Booking_ID),
		foreign key(St_ID) references Student(St_ID) ON DELETE CASCADE ON UPDATE CASCADE,
		foreign key(Hostel_ID,Room_ID) references Room(Hostel_ID,Room_ID)ON DELETE CASCADE ON UPDATE CASCADE);


#PAYMENT IN INSTALLATIONS :-
	create table payment(Payment_ID int primary key,Payment_Type varchar(30) not null,
		Payment_Date date not null,Booking_ID int,foreign key(Booking_ID) references Books(Booking_ID) ON DELETE CASCADE ON UPDATE CASCADE);


#--------------------------------------------HOSTEL RECORDS-----------------------------------------------------------------------------------------------
insert into Hostel values(1,"Vishwaraj","Kothrud,Pune","Female");
insert into Hostel values(2,"Vidyaniketan","Karve Nagar,Pune","Male");
insert into Hostel values(3,"Leelawati Hostel","Warje naka,Pune","Female");
insert into Hostel values(4,"Youthville","Badhvan,Pune","Male");


#-------------------------------------------ROOM RECORDS-------------------------------------------------------------------------------------------------
#Hostel 1
#1st floor
insert into room(hostel_ID,Room_ID,Beds) values (1,101,3);
insert into room(hostel_ID,Room_ID,Beds) values (1,102,3);
insert into room values(1,103,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(1,104,2,100000.00);
insert into room values(1,105,2,"Balcony",125000.00);
#2nd floor
insert into room(hostel_ID,Room_ID,Beds) values (1,201,3);
insert into room(hostel_ID,Room_ID,Beds) values (1,202,3);
insert into room values(1,203,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(1,204,2,100000.00);
insert into room values(1,205,2,"Balcony",125000.00);
#3rd Floor
insert into room(hostel_ID,Room_ID,Beds) values (1,301,3);
insert into room(hostel_ID,Room_ID,Beds) values (1,302,3);
insert into room values(1,303,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(1,304,2,100000.00);
insert into room values(1,305,2,"Balcony",125000.00);

#hostel 2
#1st floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,101,3,70000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,102,3,70000);
insert into room values(2,103,2,"Balcony",120000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,104,2,90000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,105,2,90000.00);
insert into room values(2,106,2,"Balcony",120000.00);
#2nd floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,201,3,70000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,202,3,70000);
insert into room values(2,203,2,"Balcony",120000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,204,2,90000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,205,2,90000.00);
insert into room values(2,206,2,"Balcony",120000.00);
#3rd floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,301,3,70000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (2,302,3,70000);
insert into room values(2,303,2,"Balcony",120000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,304,2,90000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(2,305,2,90000.00);
insert into room values(2,306,2,"Balcony",120000.00);

#hostel 3
#1st floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,101,2,120000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,102,2,120000);
insert into room values(3,103,2,"Balcony",125000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,104,90000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,105,90000.00);
insert into room values(3,106,2,"Balcony",125000.00);
#2nd floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,201,2,120000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,202,2,120000);
insert into room values(3,203,2,"Balcony",125000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,204,90000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,205,90000.00);
insert into room values(3,206,2,"Balcony",125000.00);
#3rd floor
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,301,2,120000);
insert into room(hostel_ID,Room_ID,Beds,Price) values (3,302,2,120000);
insert into room values(3,303,2,"Balcony",125000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,304,90000.00);
insert into room(hostel_ID,Room_ID,Price)values(3,305,90000.00);
insert into room values(3,306,2,"Balcony",125000.00);


#Hostel 4
#1st floor
insert into room(hostel_ID,Room_ID,Beds) values (4,101,3);
insert into room(hostel_ID,Room_ID,Beds) values (4,102,3);
insert into room values(4,103,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(4,104,2,100000.00);
insert into room values(4,105,2,"Balcony",125000.00);
#2nd floor
insert into room(hostel_ID,Room_ID,Beds) values (4,201,3);
insert into room(hostel_ID,Room_ID,Beds) values (4,202,3);
insert into room values(4,203,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(4,204,2,100000.00);
insert into room values(4,205,2,"Balcony",125000.00);
#3rd floor
insert into room(hostel_ID,Room_ID,Beds) values (4,301,3);
insert into room(hostel_ID,Room_ID,Beds) values (4,302,3);
insert into room values(4,303,2,"AC",125000.00);
insert into room(hostel_ID,Room_ID,Beds,Price)values(4,304,2,100000.00);
insert into room values(4,305,2,"Balcony",125000.00);


#-------------------------------------------------------------------EMPLOYEE RECORDS---------------------------------------------------------------------------------------------
select * from employee;
insert into employee values(101,"Ishani Panchal","Kothrud,Pune","2018-08-12","Manager",1);
insert into employee values(201,"Anuj Khanna","Kothrud,Pune","2018-08-12","Manager",2);
insert into employee values(301,"Saumya Parekh","Kothrud,Pune","2018-08-12","Manager",3);
insert into employee values(401,"Pranav Bajaj","Kothrud,Pune","2018-08-12","Manager",4);
#Chef
insert into employee values(102,"Shaurya Pillay","Bavdhan,Pune","2018-08-12","Chef",1);
insert into employee values(202,"Nikhil Parmar","Kothrud,Pune","2018-08-12","Chef",2);
insert into employee values(302,"Parth Rawat","Bavdhan,Pune","2018-08-12","Chef",3);
insert into employee values(402,"Raghav Sinha","Kothrud,Pune","2018-08-12","Chef",4);
#House Keeping
insert into employee values(103,"Sunita Salvi","Bavdhan,Pune","2018-08-12","House Keeper",1);
insert into employee values(203,"Tanvi Rawat","Kothrud,Pune","2018-08-12","House Keeper",2);
insert into employee values(303,"Nilima Sane","Bavdhan,Pune","2018-08-12","House Keeper",3);
insert into employee values(403,"AnanyaPandey","Kothrud,Pune","2018-08-12","House Keeper",4);
select *from employee;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------