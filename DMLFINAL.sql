
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
insert into employee(Emp_Name,Emp_Addr,hire_date,E_Role,Hostel_ID) values("Ishani Panchal","Kothrud,Pune","2018-08-12","Manager",1),
																			("Anuj Khanna","Kothrud,Pune","2018-08-12","Manager",2),
                                                                            ("Saumya Parekh","Kothrud,Pune","2018-08-12","Manager",3),
                                                                            ("Pranav Bajaj","Kothrud,Pune","2018-08-12","Manager",4),
                                                                            ("Shaurya Pillay","Bavdhan,Pune","2018-08-12","Chef",1),
                                                                            ("Nikhil Parmar","Kothrud,Pune","2018-08-12","Chef",2),
                                                                            ("Parth Rawat","Bavdhan,Pune","2018-08-12","Chef",3),
                                                                            ("Raghav Sinha","Kothrud,Pune","2018-08-12","Chef",4),
                                                                            ("Sunita Salvi","Bavdhan,Pune","2018-08-12","House Keeper",1),
                                                                            ("Tanvi Rawat","Kothrud,Pune","2018-08-12","House Keeper",2),
                                                                            ("Nilima Sane","Bavdhan,Pune","2018-08-12","House Keeper",3),
                                                                            ("Ananya Pandey","Kothrud,Pune","2018-08-12","House Keeper",4);
select *from employee;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	

	SELECT * FROM Hostel WHERE Hostel_id=1;

--
	#INSERT INTO books(Hostel_ID,Room_ID,St_ID,Joining_Date) VALUES(%s,%s,%s,%s);

-- 
	#INSERT INTO Std_Phone(St_ID,PhoneNo) VALUES(%s,%s);

-- 
	#INSERT INTO Guardian(St_ID,G_id,G_Name,G_Role,G_addr,G_phone) VALUES(%s,%s,%s,%s,%s,%s);

--
	#select * from display_student where st_id = %d  (VIEW )

-- 
	#select * from display_guardian where st_id = %d (VIEW)
    
--
	#select *from display_hostel where st_id = (%d)

--
	#select a.st_id,a.firstn,a.lastn from student a inner join books b using(st_id) where a.verify = 0 and b.verify = 0 and b.hostel_id = %s 
    
--
/*	UPDATE Student SET verify=1 WHERE st_id=%s"    
	UPDATE Books SET verify = 1 where st_id = %s"
    UPDATE books SET booking_date = curdate() where st_id = %s and verify = 1"
	UPDATE books SET end_date = DATE_ADD(joining_date, 1 year interval) where st_id = %s

--
	INSERT INTO Employee(Emp_Name,Emp_Addr,hire_date,E_Role,Hostel_ID) VALUES(%s,%s,%s,%s,%s)

-- 
	DELETE FROM Student where st_id=%s
    
--
	SELECT room_id FROM existingroom where hostel_id=%s
    
--
	select emp_name from employee where emp_id = %s 
    
--
	insert into complaints values (%s,%s)
    
-- 
	select *from complaints where verify = 0
    
--
	UPDATE complaints SET verify = 1 where st_id = %s
    
--
	DELETE FROM complaints where st_id = %s

--
	SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"
	select price,beds,room_type from room where hostel_id = %s group by price
    
--
	UPDATE room SET price = %s where room_type = %s and beds = %s
    
*/