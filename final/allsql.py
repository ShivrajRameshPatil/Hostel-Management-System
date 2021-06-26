import mysql.connector
from mysql.connector import Error

import datetime
from functools import reduce
import operator 

mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "shweta", database = "hostelsm")

def paymentinsert(hid,roomid,stid,jdate,ptype,pamount,pdate,pss):
    try:
        paycursor = mydb.cursor()        
        parameters=(hid,roomid,stid,jdate,ptype,pamount,pdate,pss,None)
        result=paycursor.callproc("insertpay",parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            paycursor.close()
            # print("MySQL Cursor is closed")

def unpackTuple(tup):      
    return (reduce(operator.add, tup)) 

def number(inp):
    if inp.isdigit():
        return True
    elif inp=="":
        return True
    else:
        return False

def string(inp):
    if inp.isalpha():
        return True
    elif inp=="":
        return True
    else:
        return False    

def roomtypes(bedtype):
    if(bedtype=="B2N"):
        bed=2
        roomtype="Normal"
    elif(bedtype=="B3N"):
        bed=3
        roomtype="Normal"
    elif(bedtype=="B2A"):
        bed=2
        roomtype="AC"
    elif(bedtype=="B2B"):
        bed=2
        roomtype="Balcony"
    return bed,roomtype

def hostelinfo(id):
    try:
        hostelcursor = mydb.cursor()
        hostelquery="SELECT * FROM Hostel WHERE Hostel_id= %s"
        hostelcursor.execute(hostelquery,(id,))
        hostelresult = hostelcursor.fetchall()
        return hostelresult
    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            hostelcursor.close()
            # print("MySQL Cursor is closed")

def cost(hid,bedtype):
    bed,roomtype=roomtypes(bedtype)
    try:
        roomcursor = mydb.cursor()
        
        parameters=(bed,roomtype,hid)
        output=roomcursor.callproc('price',parameters)
        
        for roomresult in roomcursor.stored_results():
            final=roomresult.fetchall()
            return final

    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            roomcursor.close()
            # print("MySQL Cursor is closed")

def bookingstu(hid,bedtype,bdate):
    bed,roomtype=roomtypes(bedtype)
    try:
        bcursor = mydb.cursor()
        
        parameters=(hid,bed,roomtype,bdate,None)
        output=bcursor.callproc('sp_stubooking',parameters)
        
        for bresult in bcursor.stored_results():
            final=bresult.fetchall()
            return final
            # for x in final:
            #     print(x[0])
    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            bcursor.close()
            # print("MySQL Cursor is closed")

def countroom(hid,bedtype):
    bed,roomtype=roomtypes(bedtype)
    try:
        count_cursor = mydb.cursor()
        
        parameters=(hid,bed,roomtype)
        query="SELECT countroom(%s,%s,%s)"
        count_cursor.execute(query,parameters)
        cresult=count_cursor.fetchall()
        # print(cresult)
        return cresult
    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            count_cursor.close()

def bookingroom(hid,rid,stid,jdate):
    try:
        bookingcursor = mydb.cursor()
        insert_booking = "INSERT INTO books(Hostel_ID,Room_ID,St_ID,Joining_Date) VALUES(%s,%s,%s,%s)"
        parameters=(hid,rid,stid,jdate)
        bookingcursor.execute(insert_booking,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            bookingcursor.close()
            # print("MySQL Cursor is closed")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def studentinsert(stid,fname,lname,gender,face,idproof,apt,bldg,street,city,state):
    try:
        stucursor = mydb.cursor()
        insert_student = "select insert_stu(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        stuPicture = convertToBinaryData(face)
        stuproof = convertToBinaryData(idproof)
        
        parameters=(stid,fname,lname,gender,stuPicture,stuproof,apt,bldg,street,city,state)
        stucursor.execute(insert_student,parameters)

        result = stucursor.fetchall()
        return result[0]
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            stucursor.close()

def studentphone(stid,phone):
    try:
        phonecursor = mydb.cursor()
        insert_phone = "INSERT INTO Std_Phone(St_ID,PhoneNo) VALUES(%s,%s)"
        
        parameters=(stid,phone)
        phonecursor.execute(insert_phone,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            phonecursor.close()
            # print("MySQL Cursor is closed")

def guardian(stid,gid,gname,grole,gaddr,gphone):
    try:
        gcursor = mydb.cursor()
        insert_g = "INSERT INTO Guardian(St_ID,G_id,G_Name,G_Role,G_addr,G_phone) VALUES(%s,%s,%s,%s,%s,%s)"
        
        parameters=(stid,gid,gname,grole,gaddr,gphone)
        gcursor.execute(insert_g,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            gcursor.close()
            # print("MySQL Cursor is closed")

def checkstudent(id,phone):
    try:
        ptr = mydb.cursor()
        newid = (id,phone, None)
        result = ptr.callproc('checkstudent' ,newid)
        return (result[2])
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()

def student_info(id) :     
    try:    
        ptr = mydb.cursor()   
        ptr.execute("select * from display_student where st_id = %d " %(id))

        result = ptr.fetchall()

        return result
    except Error as e:
        return e
    finally :
        if(mydb.is_connected()):
            ptr.close()

def student_phone(id):
    try:    
        ptr = mydb.cursor()   
        ptr.execute("select *from display_sphone where st_id = %s" %(id))

        result = ptr.fetchall()

        return result
    except Error as e:
        return e
    finally :
        if(mydb.is_connected()):
            ptr.close()

def guradian_info(id):
    try:    
        ptr = mydb.cursor()   
        ptr.execute("select * from display_guardian where st_id = %d " %(id))

        result = ptr.fetchall()

        return result
    except Error as e:
        return e
    finally :
        if(mydb.is_connected()):
            ptr.close()

'''def guradian_phone(id):
    try:    
        ptr = mydb.cursor()   
        ptr.execute("select * from display_guphone where st_id = %d " %(id))

        result = ptr.fetchall()

        return result
    except Error as e:
        return e
    finally :
        if(mydb.is_connected()):
            ptr.close()'''

def hostel_info(id):
    try :
        ptr = mydb.cursor()
        ptr.execute("select *from display_hostel where st_id = %s"%(id))
        result = ptr.fetchall()
        return result
    except Error as e:
        return e
    finally :
        if(mydb.is_connected()):
            ptr.close()

def readBLOB(id):
    try:
        def write_file(data):
            file= open(r'abc.png', 'wb')
            file.write(data)
            file.close()
            return "abc.png"
        cursor = mydb.cursor()
        sql_fetch_blob_query = """SELECT * from student where st_id = %s"""

        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        for row in record:
            image = row[4]   
            i = write_file(image)
            return i
    except Error as error:
        return error
    finally:
        if (mydb.is_connected()):
            cursor.close()

def view_student_to_verify(hid):
    try:
        temp = []
        ptr = mydb.cursor()
        ptr.execute("select a.st_id,a.firstn,a.lastn from student a inner join books b using(st_id) where a.verify = 0 and b.verify = 0 and b.hostel_id = %s ",(hid,))
        result = ptr.fetchall()
        for i in result :
            temp.append(i[:])
        return temp[:]
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()

def verifystu(id):
    try:
        ucursor = mydb.cursor()
        update_stu = "UPDATE Student SET verify = 1 WHERE st_id=%s"    
        update_books = "UPDATE Books SET verify = 1 where st_id = %s"
        update_books_booking_date = "UPDATE books SET booking_date = curdate() where st_id = %s and verify = 1"
        update_end_date = "UPDATE books SET end_date = DATE_ADD(joining_date, INTERVAL 1 YEAR) where st_id = %s"
        parameters=(id,)
        ucursor.execute(update_stu,parameters)
        ucursor.execute(update_books,parameters)
        ucursor.execute(update_books_booking_date,parameters)
        ucursor.execute(update_end_date,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ucursor.close()

def addemps(ename,eaddr,role,hid):
    try:
        hdate=datetime.datetime.today().strftime ('%Y-%m-%d')
        ecursor = mydb.cursor()
        insert_e = "INSERT INTO Employee(Emp_Name,Emp_Addr,hire_date,E_Role,Hostel_ID) VALUES(%s,%s,%s,%s,%s)"    
        parameters=(ename,eaddr,hdate,role,hid)
        ecursor.execute(insert_e,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ecursor.close()

def price(hid,bed,roomtype):
    try:
        roomcursor = mydb.cursor()
        
        parameters=(bed,roomtype,hid)
        output=roomcursor.callproc('price',parameters)
        
        for roomresult in roomcursor.stored_results():
            final=roomresult.fetchall()
            return final[0][0]

    except Error as error:
        print("Failed to execute stored procedure: {}".format(error))
    finally:
        if (mydb.is_connected()):
            roomcursor.close()

def deletestu(id):
    try:
        ucursor = mydb.cursor()
        update_stu = "DELETE FROM Student where st_id=%s"    
        parameters=(id,)
        ucursor.execute(update_stu,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ucursor.close()

def addroom(hid,rid,bed,type):
    r=price(hid,bed,type)
    try:
        rcursor = mydb.cursor()
        insert_r = "Select add_room_check(%s,%s,%s,%s,%s)"
        
        parameters=(hid,rid,bed,type,r)
        rcursor.execute(insert_r,parameters)
        result = rcursor.fetchall()
        return result[0][0]
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            rcursor.close()

def existroom(hid):
    try:
        ptr = mydb.cursor()
        newid = (hid,)
        ptr.execute('SELECT room_id FROM existingroom where hostel_id=%s' ,newid)
        result = ptr.fetchall()
        return (result)
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()

def getemployee(id):
    try:
        ptr = mydb.cursor()
        ptr.execute("select emp_name from employee where emp_id = %s " ,(id,))
        result = ptr.fetchall()
        return result[0]
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()     
   
def checkemployee(id):
    try:
        ptr = mydb.cursor()
        newid = (id, None)
        result = ptr.callproc('checkemployee' ,newid)
        return (result[1])
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()

def add_com(id, complt):
    try:
        rcursor = mydb.cursor()
        curr_date=datetime.datetime.today().strftime ('%Y-%m-%d')
        insert_r = "insert into complaints(st_id,complaint,c_date) values (%s,%s,%s)"
        parameters=(id,complt,curr_date)
        rcursor.execute(insert_r,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            rcursor.close()

def verify_com():
    try :
        ptr = mydb.cursor()
        complaint = "select *from complaints where status = 0"
        ptr.execute(complaint)
        result = ptr.fetchall()
        return result
        print(result)
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def verifyc(id):
    try :
        ptr = mydb.cursor()
        complaint = "UPDATE complaints SET status = 1 where st_id = %s"
        parameters = (id,)
        ptr.execute(complaint,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def deletec(id):
    try :
        ptr = mydb.cursor()
        complaint = "DELETE FROM complaints where st_id = %s"
        parameters = (id,)
        ptr.execute(complaint,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def existprice(id):
    try :
        ptr = mydb.cursor()
        com = "SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"
        query = "select price,beds,room_type from room where hostel_id = %s group by room_type,beds"
        parameters = (id,)
        ptr.execute(com)
        ptr.execute(query,parameters)
        result = ptr.fetchall()
        return result
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()    

def updateprice(price,rtype,bed): 
    try :
        ptr = mydb.cursor()
        s = "UPDATE room SET price = %s where room_type = %s and beds = %s"
        parameters = (price,rtype,bed)
        ptr.execute(s,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def view_comp(id):
    try:
        ptr = mydb.cursor()
        s = "select complaint from complaints where st_id = %s and `status` = 0 order by c_date desc; "
        parameters = (id,)
        ptr.execute(s,parameters)
        result = ptr.fetchall()
        return result
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def view_payment(bid):
    try:
        ptr = mydb.cursor()
        s = "select balance from paybalance where booking_id = %s"
        parameters = (bid,)
        ptr.execute(s,parameters)
        result = ptr.fetchall()
        return result 
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def insert_payment(ptype,pamount,pdate,pss,bid):
    try:
        ptr = mydb.cursor()
        s = "insert into payment(Payment_Type,Payment_Amount,Payment_Date,PaymentSS,Booking_ID) values (%s,%s,%s,%s,%s)"
        parameters = (ptype,pamount,pdate,pss,bid,)
        ptr.execute(s,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

def getgender(id):
    try:
        ptr = mydb.cursor()
        s = "select gender from student where st_id = %s"
        parameters = (id,)
        ptr.execute(s,parameters)
        result = ptr.fetchall()
        return result[0][0]
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()
