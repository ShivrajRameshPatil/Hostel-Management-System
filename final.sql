select *from student;
select *from std_phone;
truncate table std_phone;
update student set verify = 1 where st_id = 20200202;
#-------------------------------------------------------------------FUNCTIONS PROCEDURE AND TRIGGERS---------------------------------------------------------------------------

DELIMITER //
CREATE PROCEDURE sp_stubooking(IN hid int,IN bed int,IN rtype varchar(30),IN bdate date,OUT rdone int)
BEGIN
DECLARE done int default 0;
DECLARE countroom INT DEFAULT 0;
DECLARE rid INT;
DECLARE C1 CURSOR FOR SELECT r.room_id,ifnull((SELECT count(room_id) FROM books b WHERE b.room_id=r.room_id AND r.beds=bed AND r.room_type=rtype AND r.Hostel_ID=hid
AND DATE_FORMAT(b.joining_date,"%Y")=DATE_FORMAT("2020-09-10","%Y")),0) 
Beds FROM room r WHERE r.beds=bed AND r.room_type=rtype AND r.Hostel_ID=hid;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
OPEN C1;
LABEL:LOOP
		FETCH C1 INTO rid,countroom;
        IF done=1 THEN
			LEAVE LABEL;
		END IF;
		IF countroom<bed THEN
			INSERT INTO bookingrem VALUES(countroom,rid);
		END IF;
	END LOOP LABEL;
	CLOSE C1;
    SELECT roomid FROM bookingrem;
	TRUNCATE TABLE bookingrem;
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
create function  checkstudent (id1 int,phno varchar(11)) returns int deterministic  
begin
declare stid int;
declare pno varchar(11);
declare done int default 0 ;
declare continue handler for not found set done =1;
select st_id into stid from student;
select phoneno into pno from std_phone where St_Id  = id1;
 
	if done then 
		return -1;
	end if;
	if stid=id1 and pno = phno then
		return 0 ;
	else
		return 1;
	end if;
end $$
delimiter ;

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


