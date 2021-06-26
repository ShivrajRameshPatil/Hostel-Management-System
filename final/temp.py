import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "28868755", database = "hostelsm")


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


