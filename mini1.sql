create view display_student as select * from student a inner join guardian b using(st_id) ;

select * from display_student;
drop view display_student;

