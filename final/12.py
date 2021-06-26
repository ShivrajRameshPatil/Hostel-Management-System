from functools import reduce
import operator 
  
def unpackTuple(tup): 
      
    return (reduce(operator.add, tup)) 

import mysql.connector
from mysql.connector import Error
from tkinter import *

mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "28868755", database = "hostelsm")
def view_student_to_verify():
    try:
        temp = []
        ptr = mydb.cursor()
        ptr.execute("select st_id,firstn,lastn from student where verify = 0")
        result = ptr.fetchall()
        for i in result :
            temp.append(i[:])
        print(temp[:])
        return temp[:]
    except Error as e:
        return (e)
    finally :
        if(mydb.is_connected()):
            ptr.close()

root=Tk()

sizex = 600
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

labels = []

def myClick():
    del labels[:]
    myframe=Frame(root,width=400,height=300,bd=2,relief="groove")
    myframe.place(x=10,y=10)
    value = view_student_to_verify()
    val = unpackTuple(value)
    x = len(val)
    print(x)
    i = 0
    j = 0
    while i<x:
        labels.append(Label(myframe,text=" ID : {} ".format(val[i])))
        labels[i].place(x=0,y=10+(30*i))
        Button(myframe,text="Accept").place(x = 250,y=10+(30*j))
    else :
        print("done")
mybutton=Button(root,text="OK",command=myClick)
mybutton.place(x=420,y=10)


myvalue=Entry(root)
myvalue.place(x=450,y=10)

root.mainloop()