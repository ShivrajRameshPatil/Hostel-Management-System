import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

window  = tk.Tk()
window.title('HOSTEL MANAGEMENT SYSTEM')

id = Label(window, text = "ENTER STUDENT ID : ")
id.grid(row = 0 ,column = 0)
phone = Label(window , text = "ENTER PHONE NUMBER : ")
phone.grid(row = 1,column = 0)
in_id = IntVar()
in_phone = IntVar()
id_in = Entry(window , textvariable = in_id)
id_in.grid(row = 0 ,column = 1)
phone_in = Entry(window , textvariable = in_phone)
phone_in.grid(row = 1, column = 1)
def action():
    stu_phone = in_phone.get()
    stu_id = in_id.get()
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "28868755", database = "hostelmanagementsystem")
    ptr = mydb.cursor()
    ptr.execute("select checkstudent(%d , %d)" %(stu_id,stu_phone))
    result = ptr.fetchall()
    for rows in result :
        if rows[0] == 1:
            messagebox.showinfo("ERROR FOUND ", "INCORRECT ID OR PASSWORD , TRY AGAIN")
        elif rows[0] == 0 :
            messagebox.showinfo("REGISTRATION ", "OK CORRECT , PRESS SUBMIT !" ) 
        elif rows[0] == -1:
            messagebox.showinfo("ERROR FOUND ", "NOT REGISTERED ID , REGISTER FIRST !")

submit = Button(window , text = "submit " , command = action )
submit.grid(row=3,column = 0 )

window.mainloop()