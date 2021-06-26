import mysql.connector
from mysql.connector import Error
from tkinter import *
import tkinter
from PIL import Image,ImageTk
window=tkinter.Tk()

def write_file(data):
    # Convert binary data to proper format and write it on Hard Disk
    file= open(r'E:\STUDY\TY sem - 7\DBMS\abc.png', 'wb')
    file.write(data)
    file.close()

def readBLOB(emp_id):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hostelsm',
                                             user='root',
                                             password='28868755')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from student where st_id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[4]
            
            
            print("Storing employee image and bio-data on disk \n")
            write_file(image)
            

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

readBLOB(20200201)
img=ImageTk.PhotoImage(Image.open(r'E:\STUDY\TY sem - 7\DBMS\abc.png').resize((200,200)))
myLabel=Label(window,image=img)
myLabel.place(x=0,y=0)
window.mainloop()

