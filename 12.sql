
#-------------------------------------------------------------VIEWS---------------------------------------------------------------------------------------------------------------
create table gd_phone(St_ID	int,G_ID int,PhoneNo varchar(10) , foreign key (st_id,g_id) references guardian(st_id,g_id));	
create view display_student as (select *from student where verify =1);
create view display_guardian as (select * from guardian where verify = 1);
create view display_sphone as (select *from std_phone where st_id in (select St_ID from student where verify = 1));
create view display_guphone as select * from gd_phone where g_id in (select g_id from guardian where verify = 1)
								and st_id in (select st_id from guardian where verify = 1);

create view display_hostel as select hostel_id,room_id,st_id from books where verify = 1;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------