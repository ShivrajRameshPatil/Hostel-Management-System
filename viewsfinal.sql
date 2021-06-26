select *from room where hostel_id = 1;
use hostelsm;
select *from student;
delete from std_phone where st_id = 1032180381;
delete from student where st_id = 1032180381;
insert into std_phone values (1032180381,'8454907639');
#-------------------------------------------------------------VIEWS---------------------------------------------------------------------------------------------------------------
create table gd_phone(St_ID	int,G_ID int,PhoneNo varchar(10) , foreign key (st_id,g_id) references guardian(st_id,g_id));	
create view display_student as (select *from student where verify =1);
create view display_guardian as (select * from guardian);
create view display_sphone as (select *from std_phone where st_id in (select St_ID from student where verify = 1));
drop view display_hostel;
create view display_hostel as select hostel_id,room_id,st_id,booking_id from books where DATE_FORMAT(joining_date,'%Y') = DATE_FORMAT(curdate(),'%Y');
CREATE VIEW existingroom AS SELECT * FROM room where hostel_id = 1;
SELECT * FROM existingroom where Hostel_ID=1;
select *from display_hostel;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE VIEW paybalance AS
SELECT (price-sum(p.payment_amount)) balance,p.booking_id,temp.st_id FROM 
	(SELECT r.price,b.booking_id,b.room_id,b.hostel_id,b.st_id FROM room r 
		LEFT JOIN books b ON r.room_id=b.room_id where r.hostel_id=b.hostel_id group by b.booking_id) temp 
			INNER JOIN payment p ON temp.booking_id=p.booking_id group by p.booking_id;

SELECT * FROM paybalance WHERE booking_id=3;