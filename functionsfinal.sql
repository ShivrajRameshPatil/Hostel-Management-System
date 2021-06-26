
#----------------------------------------FUNCTIONS PROCEDURE AND TRIGGERS---------------------------------------------------------------------------
use hostelsm;
delimiter $$
CREATE FUNCTION insert_stu ( id1 int ,fname varchar(30) ,lname varchar(30) ,gen varchar(30) , fr longblob , id_p longblob ,
							apt varchar(6), buildg varchar(30), street varchar(20) , city varchar(30) , state varchar(30) ) returns int deterministic
BEGIN 
	declare exit handler for 1062 
	begin 
		return -1;
	end;
	INSERT INTO Student(St_ID,Firstn,Lastn,Gender,Face,ID_Proof,Aptno,Buidg,Street,City,State) VALUES(id1, fname,lname, gen,fr,id_p,apt,buildg,street,city,state);
	return 1;
END $$
DELIMITER ;

delimiter //
CREATE PROCEDURE insertpay(IN hid INT,IN roomid INT,IN stid INT,IN jdate date,IN ptype varchar(30),IN pamount decimal(8,2),IN pdate date,IN pss LONGBLOB,OUT done INT)
BEGIN
DECLARE bid INT DEFAULT 0;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
SELECT booking_id INTO bid FROM books WHERE hostel_id=hid AND room_id=roomid AND joining_date=jdate;
IF done=1 THEN
	SELECT 'Booking Not Found';
ELSE
	INSERT INTO payment(Payment_Type,Payment_Amount,Payment_Date,PaymentSS,Booking_ID) VALUES (ptype,pamount,pdate,pss,bid);
END IF;
END//
delimiter ;

delimiter $$
CREATE FUNCTION add_room_check(hid int , rid int , bed int , rtype varchar(30) , price decimal(8,0)) RETURNS INT DETERMINISTIC
BEGIN 
	declare exit handler for 1602
    begin 
		return -1;
	end;
    insert into room values (hid,rid,bed,rtype,price);
    return 1;
END $$
delimiter $$
create procedure checkstudent (IN id1 int,IN phno varchar(11), OUT ret int) 
begin
declare stid int;
declare pno varchar(11);
declare done int default 0 ;
declare ver int default 0;
declare continue handler for not found set done =1;
select phoneno into pno from std_phone where st_id = id1 and PhoneNo = phno;
select st_id into stid from student where st_id = id1;
select verify into ver from student where st_id = id1;
	if ver = 1 then
		set ret = 1;
	elseif ver = 0 and done = 1 then 
		set ret = -1;
	elseif ver = 0 then 
		set ret = 0;
	end if;
END $$
delimiter ;

DELIMITER //
CREATE PROCEDURE sp_stubooking(IN hid int,IN bed int,IN rtype varchar(30),IN bdate date,OUT rdone int)
BEGIN
SELECT room_id FROM(SELECT r.room_id,r.beds,ifnull((SELECT count(room_id) FROM books b WHERE b.room_id=r.room_id AND r.beds=bed AND r.room_type=rtype AND r.Hostel_ID=hid
AND DATE_FORMAT(b.joining_date,"%Y")=DATE_FORMAT("2020-09-10","%Y")),0) 
bookbeds FROM room r WHERE r.beds=bed AND r.room_type=rtype AND r.Hostel_ID=hid)AS temp WHERE (beds-bookbeds)>0;
END//


CREATE PROCEDURE price(IN bed int,IN rtype varchar(30),IN hid int)
BEGIN
SELECT CAST((avg(Price)) AS DECIMAL(8.4)) Cost FROM room WHERE beds=bed AND room_type=rtype AND Hostel_id=hid;
END//

CREATE FUNCTION countroom(hid int,bed int,rtype varchar(30))RETURNS INT
DETERMINISTIC
BEGIN
DECLARE count_room INT DEFAULT 0;
SELECT count(room_id) INTO count_room FROM room WHERE beds=bed AND room_type=rtype AND Hostel_ID=hid;
return count_room;
END//

Delimiter $$
create procedure checkemployee (IN id1 int,OUT foundemp int) 
begin
declare empid int;
declare job varchar(30) default "";
declare exit handler for not found
BEGIN
	SET foundemp=-1;
END;
select e_role into job from employee where emp_id=id1;
select emp_id into empid from employee where emp_id=id1;
	if job = "manager" then 
		SET foundemp=1;
	else 
		set foundemp = 0;
	end if;
end $$
delimiter ;
