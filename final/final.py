
#------------------------------------------------------------------------------------------------------------
import tkinter as tk
import math
import random
import requests
import os
from allsql import * 
from scroll import ScrollableFrame
import mysql.connector
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
from tkcalendar import Calendar,DateEntry
#------------------------------------------------------------------------------------------------------------
window1 = tk.Tk()
window1.iconbitmap(r"icon.ico")
window1.title('HOSTEL MANAGEMENT SYSTEM')
window1.geometry("1350x720+0+0")
window1.config(bg = "#efefef")
window_frame = Frame(window1, bg = "#efefef")
window_frame.place(x = 0, y = 0, height = 1350, width = 1350)
window1.resizable(False, False)
regint = window1.register(number)
regstr = window1.register(string)
global file 
file = ""
# ----------------------------------------------------------------------#
# FIRST WINDOW FOR STUDENT DETAILS#
# ----------------------------------------------------IMAGE CREATIONS------------------------------------------------------------------------
global mainlogo
mainlogo = ImageTk.PhotoImage(Image.open(r"logo.jpeg").resize((600, 600)))
global edit
edit = ImageTk.PhotoImage(Image.open(r"edit.jpeg").resize((25, 25)))
# global edit2
# edit2 = ImageTk.PhotoImage(Image.open(r"edit2.jpg").resize((25, 25)))
global logo
logo2 = ImageTk.PhotoImage(Image.open(r"logo2.jpeg").resize((200, 200)))
'''
*************************************************************************************************************
MINI PROJECT - HOSTEL MANAGEMENT SYSTEM 
ROLL NO - 18,23,62,63
*************************************************************************************************************
'''

#--------------------------------------------------REGISTRATION PAGE---------------------------------------------------------------------------
class Booking:
    hid=0
    rid=0
    jdate=""
    stid=0
    hostel=0
    gender = ""
    roomtype=""
    ptype=""
    pamount=float(0)
    pdate=""
    price=0
    paymentss=""
    hostels = []
    la1 = ImageTk.PhotoImage(Image.open(r"label.png").resize((95, 45)))
    def __init__(self,st_id):
        self.stid=st_id
        self.gender = getgender(self.stid)
        window1.title("Booking")
        self.B2N = ImageTk.PhotoImage(Image.open(r"B2N.png").resize((150,150)))
        self.B3N = ImageTk.PhotoImage(Image.open(r"B3N.png").resize((150,150)))
        self.B2A = ImageTk.PhotoImage(Image.open(r"B2A.png").resize((150,150)))
        self.B2B = ImageTk.PhotoImage(Image.open(r"B2B.png").resize((150,150)))    
        self.WL = ImageTk.PhotoImage(Image.open(r"WL.png").resize((60,40)))
        self.CC = ImageTk.PhotoImage(Image.open(r"CC.png").resize((60,40))) 
        self.DC = ImageTk.PhotoImage(Image.open(r"DC.png").resize((60,40)))    
        self.NB = ImageTk.PhotoImage(Image.open(r"NB.png").resize((60,40)))  
        self.hostel()

    def booking(self):
        self.rid=self.room_var.get()
        self.jdate=self.cal.get_date()
        
        bookingroom(self.hid,self.rid,self.stid,self.jdate)
        answer = messagebox.askokcancel("Booking","Booking Will be Confirmed Only\n If Security Deposit Is paid!!")
        if answer:
            self.payment()

    
    def room(self,hostel_id):
        self.white_frame2 = Frame(window1, bg = "#efefef")
        self.white_frame2.place(x = 0, y = 0, height = 1350, width = 1350)

        self.up2_label = Label(self.white_frame2, bg = "#1daf9b")
        self.up2_label.place(x = 0, y = 0, height = 330, width = 1350)
        self.bottom2_label = Label(self.white_frame2, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b")
        self.bottom2_label.place(x = 0, y = 680, height = 30, width = 1350)
        
        
        self.room_label= Label(self.white_frame2, bg = "white", borderwidth = 4, relief = "raised")      
        self.room_label.place(x = 275, y = 100, height = 500, width = 775)
        r_label=Label(self.room_label,bg="white",fg ="#33414f",text="Select Room",font="georgia 18 bold")
        r_label.place(x=295,y=0)
        #room type 1 label
        c1=cost(hostel_id,"B2N")
        count=countroom(hostel_id,"B2N")
        self.B2Ncost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
        self.B2Ncost_label.place(x=55,y=225)
        self.B2Ncount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
        self.B2Ncount_label.place(x=55,y=300)
        self.B2Nbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
        self.B2Nbed_label.place(x=80,y=250)
        self.B2Ntype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Normal Room",font="georgia 12 bold")
        self.B2Ntype_label.place(x=55,y=275)
        #room type 2 label
        c1=cost(hostel_id,"B3N")
        count=countroom(hostel_id,"B3N")
        self.B3Ncost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
        self.B3Ncost_label.place(x=240,y=225)
        self.B3Ncount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
        self.B3Ncount_label.place(x=240,y=300)
        self.B3Nbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="3 BEDS",font="georgia 12 bold")
        self.B3Nbed_label.place(x=265,y=250)
        self.B3Ntype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Normal Room",font="georgia 12 bold")
        self.B3Ntype_label.place(x=240,y=275)
        #room type 3 label
        c1=cost(hostel_id,"B2A")
        count=countroom(hostel_id,"B2A")
        self.B2Acost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
        self.B2Acost_label.place(x=415,y=225)
        self.B2Acount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
        self.B2Acount_label.place(x=415,y=300)
        self.B2Abed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
        self.B2Abed_label.place(x=450,y=250)
        self.B2Atype_label=Label(self.room_label,bg="white",fg = "#33414f",text="AC Room",font="georgia 12 bold")
        self.B2Atype_label.place(x=443,y=275)
        #room type 4 label
        c1=cost(hostel_id,"B2B")
        count=countroom(hostel_id,"B2B")
        self.B2Bcost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
        self.B2Bcost_label.place(x=600,y=225)
        self.B2Bcount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
        self.B2Bcount_label.place(x=600,y=300)
        self.B2Bbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
        self.B2Bbed_label.place(x=633,y=250)
        self.B2Btype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Balcony Room",font="georgia 12 bold")
        self.B2Btype_label.place(x=610,y=275)

        def which_room(roomtype,hostel_id):
            self.roomtype=roomtype
            # self.price=
            #room type 1 label
            r_label=Label(self.room_label,bg="white",fg ="#33414f",text="Select Room",font="georgia 18 bold")
            r_label.place(x=295,y=0)
            c1=cost(hostel_id,"B2N")
            count=countroom(hostel_id,"B2N")
            self.B2Ncost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
            self.B2Ncost_label.place(x=55,y=225)
            self.B2Ncount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
            self.B2Ncount_label.place(x=55,y=300)
            self.B2Nbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
            self.B2Nbed_label.place(x=80,y=250)
            self.B2Ntype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Normal Room",font="georgia 12 bold")
            self.B2Ntype_label.place(x=55,y=275)
            #room type 2 label
            c1=cost(hostel_id,"B3N")
            count=countroom(hostel_id,"B3N")
            self.B3Ncost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
            self.B3Ncost_label.place(x=240,y=225)
            self.B3Ncount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
            self.B3Ncount_label.place(x=240,y=300)
            self.B3Nbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="3 BEDS",font="georgia 12 bold")
            self.B3Nbed_label.place(x=265,y=250)
            self.B3Ntype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Normal Room",font="georgia 12 bold")
            self.B3Ntype_label.place(x=240,y=275)
            #room type 3 label
            c1=cost(hostel_id,"B2A")
            count=countroom(hostel_id,"B2A")
            self.B2Acost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
            self.B2Acost_label.place(x=415,y=225)
            self.B2Acount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
            self.B2Acount_label.place(x=415,y=300)
            self.B2Abed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
            self.B2Abed_label.place(x=450,y=250)
            self.B2Atype_label=Label(self.room_label,bg="white",fg = "#33414f",text="AC Room",font="georgia 12 bold")
            self.B2Atype_label.place(x=443,y=275)
            #room type 4 label
            c1=cost(hostel_id,"B2B")
            count=countroom(hostel_id,"B2B")
            self.B2Bcost_label=Label(self.room_label,bg="white",fg = "#33414f",text="Rs {}.00".format(c1[0][0]),font="georgia 12 bold")
            self.B2Bcost_label.place(x=600,y=225)
            self.B2Bcount_label=Label(self.room_label,bg="white",fg = "#33414f",text="Total Rooms {}".format(count[0][0]),font="georgia 12 bold")
            self.B2Bcount_label.place(x=600,y=300)
            self.B2Bbed_label=Label(self.room_label,bg="white",fg = "#33414f",text="2 BEDS",font="georgia 12 bold")
            self.B2Bbed_label.place(x=633,y=250)
            self.B2Btype_label=Label(self.room_label,bg="white",fg = "#33414f",text="Balcony Room",font="georgia 12 bold")
            self.B2Btype_label.place(x=610,y=275)
            #combobox with room no and joining date
            self.avlrooms= Label(self.room_label,bg="white",fg ="#33414f",text="Available Room No",font="georgia 12 bold")
            self.avlrooms.place(x=200,y=365)
            self.room_var = StringVar()
            self.room_combobox = ttk.Combobox(self.room_label, width = 14,font="georgia 12 bold",textvariable = self.room_var, state = 'readonly')
            self.room_combobox.place(x = 400, y = 365)
            self.cal_label=Label(self.room_label,bg="white",fg ="#33414f",text="Joining Date",font="georgia 12 bold")
            self.cal_label.place(x = 200, y = 395)
            self.cal = DateEntry(self.room_label, width=23, background="#33414f",foreground='white',activebackground="#33414f", borderwidth=2,year=datetime.datetime.today().year)
            self.cal.place(x = 400, y = 395)
            self.hid=hostel_id
            curr_date=datetime.datetime.today().strftime ('%Y-%m-%d')
            room1=bookingstu(hostel_id,roomtype,str(curr_date))
            x=len(room1)
            i=0
            combo=[]
            for i in range(x):
                y=room1[i][0]
                combo.append(y)
                self.room_combobox['values']=combo
            self.room_combobox.set(combo[0])

            self.B2N_button=Button(self.room_label,cursor = "hand2",bg="white",image=self.B2N,borderwidth=0,activebackground="white",command=lambda:which_room("B2N",hostel_id))
            self.B2N_button.place(x=35,y=45)

            self.B3N_button=Button(self.room_label,bg="white",cursor = "hand2",image=self.B3N,borderwidth=0,activebackground="white",command=lambda:which_room("B3N",hostel_id))
            self.B3N_button.place(x=220,y=45) 
            
            self.B2A_button=Button(self.room_label,bg="white",cursor = "hand2",image=self.B2A,borderwidth=0,activebackground="white",command=lambda:which_room("B2A",hostel_id))
            self.B2A_button.place(x=405,y=45)        

            self.B2B_button=Button(self.room_label,bg="white",cursor = "hand2",image=self.B2B,borderwidth=0,activebackground="white",command=lambda:which_room("B2B",hostel_id))
            self.B2B_button.place(x=590,y=45)
            self.labelr = Label(self.room_label, image = self.la1, borderwidth = 0, bg = "white")
            self.labelr.place(x = 335, y = 435)
            self.submitroom=Button(self.labelr,fg="#33414f",bg = "#1daf9b",relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                            highlightcolor = "#1dafb9",text="SUBMIT",font="georgia 10 bold",cursor = "hand2",command=self.booking)
            self.submitroom.place(x=12,y=8)    
           
        #placing room images as button
        self.B2N_button=Button(self.room_label,cursor = "hand2",bg="white",image=self.B2N,borderwidth=0,activebackground="white",command=lambda:which_room("B2N",hostel_id))
        self.B2N_button.place(x=35,y=45)

        self.B3N_button=Button(self.room_label,cursor = "hand2",bg="white",image=self.B3N,borderwidth=0,activebackground="white",command=lambda:which_room("B3N",hostel_id))
        self.B3N_button.place(x=220,y=45) 

        self.B2A_button=Button(self.room_label,cursor = "hand2",bg="white",image=self.B2A,borderwidth=0,activebackground="white",command=lambda:which_room("B2A",hostel_id))
        self.B2A_button.place(x=405,y=45)        
 
        self.B2B_button=Button(self.room_label,cursor = "hand2",bg="white",image=self.B2B,borderwidth=0,activebackground="white",command=lambda:which_room("B2B",hostel_id))
        self.B2B_button.place(x=590,y=45)
        

    def hostel(self):
        white_frame1 = Frame(window1, bg = "#efefef")
        white_frame1.place(x = 0, y = 0, height = 1350, width = 1350)

        up_label = Label(white_frame1, bg = "#1daf9b")
        up_label.place(x = 0, y = 0, height = 330, width = 1350)
        main_label= Label(white_frame1, bg = "white", borderwidth = 4, relief = "raised")
        main_label.place(x = 275, y = 100, height = 500, width = 775)
        bottom_label = Label(white_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b")
        bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        hostel_label=Label(main_label,bg="white",fg ="#33414f",text="Select Hostel",font="georgia 18 bold")
        hostel_label.place(x=295,y=0)
        self.h1 = ImageTk.PhotoImage(Image.open(r"h1.png").resize((150,150)))
        self.h2 = ImageTk.PhotoImage(Image.open(r"h2.png").resize((150,150)))
        self.h3 = ImageTk.PhotoImage(Image.open(r"h3.png").resize((150,150)))
        self.h4 = ImageTk.PhotoImage(Image.open(r"h4.png").resize((150,150)))

        def gendercheck(hid,g):
            print(self.gender)
            print(g)
            if g == self.gender:
                self.room(hid)
            else :
                messagebox.showerror("ERROR FOUND ","Select hostel for your own gender ")
                self.hostel()
        h1_button=Button(main_label,bg="white",image=self.h1,borderwidth=0,cursor = "hand2",command=lambda :gendercheck(1,self.gen1))
        h1_button.place(x=35,y=45)

        self.hostels=hostelinfo(1)
        for x in self.hostels:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=35,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=35,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=35,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=35,y=370)
            self.gen1 = x[3]

        h2_button=Button(main_label,bg="white",image=self.h2,cursor = "hand2",borderwidth=0,command=lambda :gendercheck(2,self.gen2))
        h2_button.place(x=220,y=45)
        self.hostels=hostelinfo(2)
        for x in self.hostels:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=220,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=220,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=220,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=220,y=370)
            self.gen2 = x[3]

        h3_button=Button(main_label,bg="white",image=self.h3,borderwidth=0,cursor = "hand2",command=lambda :gendercheck(3,self.gen3))
        h3_button.place(x=405,y=45)
        self.hostels=hostelinfo(3)
        for x in self.hostels:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=405,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=405,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=405,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=405,y=370)
            self.gen3 = x[3]

        h4_button=Button(main_label,bg="white",image=self.h4,cursor = "hand2",borderwidth=0,command=lambda :gendercheck(4,self.gen4))
        h4_button.place(x=590,y=45)
        self.hostels=hostelinfo(4)
        for x in self.hostels:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=590,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=590,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=590,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=590,y=370)
            self.gen4 = x[3]

    def payment(self):
        self.price=cost(self.hid,self.roomtype)
        self.white_frame1 = Frame(window1, bg = "#efefef")
        self.white_frame1.place(x = 0, y = 0, height = 1350, width = 1350)

        self.up_label = Label(self.white_frame1, bg = "#1daf9b")
        self.up_label.place(x = 0, y = 0, height = 330, width = 1350)
        self.pay_label= Label(self.white_frame1, bg = "white", borderwidth = 4, relief = "raised")
        self.pay_label.place(x = 450, y = 100, height= 500, width =400)
        self.bottom_label = Label(self.white_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b")
        self.bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        #payment methods
        inst1=float(20000)
        inst2=(float(self.price[0][0])-inst1)/2
        inst3=(float(self.price[0][0])-inst1)/2
        inst4=float(self.price[0][0])
        self.select=Label(self.pay_label,text="Select Payment Method",font = "georgia 18 bold",fg = "#33414f",bg="white")
        self.select.place(x=45,y=0)
        if(self.roomtype=="B2N"):
            self.roomtype="2 Beds Normal Room"
        elif(self.roomtype=="B3N"):
            self.roomtype="3 Beds Normal Room"
        elif(self.roomtype=="B2A"):
            self.roomtype="2 Beds AC Room"
        elif(self.roomtype=="B2B"):
            self.roomtype="2 Beds Balcony Room"
        inst1=float(20000)
        self.hostellabel=Label(self.pay_label,text="{} Hostel,{}".format(self.hostels[0][1],self.hostels[0][2]),font = "georgia 12",fg = "#33414f",bg="white")
        self.hostellabel.place(x=5,y=100)
        self.room=Label(self.pay_label,text="Room No. {}".format(self.rid),font = "georgia 12",fg = "#33414f",bg="white")
        self.room.place(x=5,y=130)  
        self.type=Label(self.pay_label,text="Room Type {}".format(self.roomtype),font = "georgia 12",fg = "#33414f",bg="white")
        self.type.place(x=5,y=160)
        self.cost=Label(self.pay_label,text="Room Cost Rs.{}".format(self.price[0][0]),font = "georgia 12",fg = "#33414f",bg="white")
        self.cost.place(x=5,y=190)
        self.jdate_label=Label(self.pay_label,text="Joining Date {}".format(self.jdate),font = "georgia 12",fg = "#33414f",bg="white")
        self.jdate_label.place(x=5,y=220)    
        self.sdeposit_label=Label(self.pay_label,text="Security Deposit Rs.{}*".format(inst1),font = "georgia 12",fg = "#33414f",bg="white")
        self.sdeposit_label.place(x=5,y=250)
        def payment_det(ptype):
            self.ptype=ptype
            self.select=Label(self.pay_label,text="Select Payment Method",font = "georgia 18 bold",fg = "#33414f",bg="white")
            self.select.place(x=45,y=0)
            self.hostellabel=Label(self.pay_label,text="{} Hostel,{}".format(self.hostels[0][1],self.hostels[0][2]),font = "georgia 12",fg = "#33414f",bg="white")
            self.hostellabel.place(x=5,y=100)
            self.room=Label(self.pay_label,text="Room No. {}".format(self.rid),font = "georgia 12",fg = "#33414f",bg="white")
            self.room.place(x=5,y=130)  
            self.type=Label(self.pay_label,text="Room Type {}".format(self.roomtype),font = "georgia 12",fg = "#33414f",bg="white")
            self.type.place(x=5,y=160)
            self.cost=Label(self.pay_label,text="Room Cost Rs.{}".format(inst4),font = "georgia 12",fg = "#33414f",bg="white")
            self.cost.place(x=5,y=190)  
            self.jdate_label=Label(self.pay_label,text="Joining Date {}".format(self.jdate),font = "georgia 12",fg = "#33414f",bg="white")
            self.jdate_label.place(x=5,y=220)
            self.sdeposit_label=Label(self.pay_label,text="Security Deposit Rs.{}*".format(inst1),font = "georgia 12",fg = "#33414f",bg="white")
            self.sdeposit_label.place(x=5,y=250)

            self.CCbutton= Button(self.pay_label, bg = "white",image=self.CC,relief="flat",cursor="hand2",command=lambda:payment_det("Credit Card"))
            self.CCbutton.place(x=7,y=40)
            self.NBbutton= Button(self.pay_label, bg = "white",image=self.NB,relief="flat",cursor="hand2",command=lambda:payment_det("Net Banking"))
            self.NBbutton.place(x=110,y=40)
            self.DCbutton= Button(self.pay_label, bg = "white",image=self.DC,relief="flat",cursor="hand2",command=lambda:payment_det("Debit Card"))
            self.DCbutton.place(x=210,y=40)
            self.WLbutton= Button(self.pay_label, bg = "white",image=self.WL,relief="flat",cursor="hand2",command=lambda:payment_det("UPI Wallet"))
            self.WLbutton.place(x=315,y=40)

            self.inst=Label(self.pay_label,text="Installment(Rs)",font = "georgia 12",fg = "#33414f",bg="white")
            self.inst.place(x=5,y=280)
            self.inst_var=StringVar()
            self.price_combobox = ttk.Combobox(self.pay_label, width = 14,font="georgia 12",foreground = "#33414f",textvariable = self.inst_var, state = 'readonly')
            self.price_combobox.place(x = 8, y = 300,width=375)
            self.price_combobox['values']=[inst1,inst4]
            self.price_combobox.set(inst1)
            self.date=Label(self.pay_label,text="Payment Date",font = "georgia 12",fg = "#33414f",bg="white")
            self.date.place(x=5,y=330)
            self.cal = DateEntry(self.pay_label, background="#33414f",foreground="white",activebackground="#33414f", borderwidth=2,year=datetime.datetime.today().year)
            self.cal.place(x = 8, y = 350,width=375)
            self.sslabel=Label(self.pay_label,bg="white")
            self.sslabel.place(x =8, y = 420,width=350)
            def uploadss():
                ss = filedialog.askopenfilename(initialdir = "/", title = "Select Image",            
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            
                g="""\\\\"""            
                self.paymentss=str(ss.replace('/',g))
                print(self.paymentss)
                self.sslabel['text']=ss
            self.pss=Label(self.pay_label,text="Payment Screenshot",font = "georgia 12",fg = "#33414f",bg="white")
            self.pss.place(x=5,y=375)
            self.pssbutton= Button(self.pay_label,text="upload" ,bg = "#efefef",cursor="hand2",command=uploadss)
            self.pssbutton.place(x=5,y=395,width=375)
            def payment_done():
                self.pamount=self.inst_var.get()
                self.pdate=self.cal.get_date()
                print(self.pamount)
                if(self.paymentss==""):
                    messagebox.showwarning("Screenshot","Payment Screenshot Necessary!!")
                else:
                    messagebox.showinfo("Registration","Booking Request Sent")
                    paymentinsert(self.hid,self.rid,self.stid,self.jdate,self.ptype,self.pamount,self.pdate,self.paymentss)
                    window1.destroy()


            self.slabel = Label(self.pay_label, image = self.la1, borderwidth = 0, bg = "white")
            self.slabel.place(x = 148, y = 440)
            self.submit = Button(self.slabel, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                                relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                                highlightcolor = "#1dafb9", command = payment_done)
            self.submit.place(x = 12, y = 8)


        self.CCbutton= Button(self.pay_label, bg = "white",image=self.CC,relief="flat",cursor="hand2",command=lambda:payment_det("Credit Card"))
        self.CCbutton.place(x=7,y=40)
        self.CClabel= Label(self.pay_label, text="Credit Card",font = "georgia 7",fg = "#33414f", bg= "white",relief="flat")
        self.CClabel.place(x=10,y=83)
        self.NBbutton= Button(self.pay_label, bg = "white",image=self.NB,relief="flat",cursor="hand2",command=lambda:payment_det("Net Banking"))
        self.NBbutton.place(x=110,y=40)
        self.NBlabel= Label(self.pay_label,text="Net Banking",font = "georgia 7",fg = "#33414f", bg = "white",relief="flat")
        self.NBlabel.place(x=113,y=83)
        self.DCbutton= Button(self.pay_label, bg = "white",image=self.DC,relief="flat",cursor="hand2",command=lambda:payment_det("Debit Card"))
        self.DCbutton.place(x=210,y=40)
        self.DClabel= Label(self.pay_label,text="Debit Card",font = "georgia 7",fg = "#33414f", bg = "white",relief="flat")
        self.DClabel.place(x=215,y=83)
        self.WLbutton= Button(self.pay_label, bg = "white",image=self.WL,relief="flat",cursor="hand2",command=lambda:payment_det("UPI Wallet"))
        self.WLbutton.place(x=315,y=40)
        self.WLlabel= Label(self.pay_label,text="UPI Wallet",font = "georgia 7",fg = "#33414f", bg = "white",relief="flat")
        self.WLlabel.place(x=318,y=83)

class RegisterStudent(Booking):
    # STUDENT VARIABLES
    st_id = 0
    fname = ""
    lname = ""
    apt=""
    bldg=""
    state = ""
    city = ""
    street = ""
    face = ""
    idproof = ""
    gender = ""
    sphoneno1 = ""
    sphoneno2 = ""
    face=""
    idproof=""
    # GUARDIAN VARIABLES
    g_id = 1
    gname = ""
    gphone=0
    gaddr=""
    gphone=0
    grole=""
    sgid=0
    newface = ""
    newproof = ""


    def __init__(self):
        # -------------------------------------REGISTRATION PAGE----------------------------------------------
            window1.title('REGISTRATION')
            window1.resizable(False, False)

               
            self.student()

    def guardian(self,st_id):
        self.sgid=st_id
        self.g_frame = Frame(window1,bg = "#efefef")
        self.g_frame.place(x=0,y=0,height=1350,width=1350)
        self.background_label21 = Label(self.g_frame, bg = "#1daf9b")
        self.background_label21.place(x = 0, y = 0, height = 330, width = 1350)
        self.bottom_label = Label(self.g_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b", anchor = "n")
        self.bottom_label.place(x = 0, y = 680, height = 100, width = 1350)
        self.label_2 = Label(self.g_frame, bg = "white", borderwidth = 3, relief = "raised")
        self.label_2.place(x = 450, y = 100, height = 500, width = 400)

        # ----------------------------------------------------------------------#
        # LABELS FOR GUARDIAN DETAILS#

        guardian_label = Label(self.g_frame, text = "GUARDIAN DETAIL", background = "white", foreground = "#33414f",
                               font = "georgia 20 bold ", anchor = 's')
        guardian_label.place(x = 490, y = 130)

        guardianname_label = Label(self.g_frame, text = "Enter Name * ", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianname_label.place(x = 460, y = 220)

        guardianphone_label = Label(self.g_frame, text = "Enter Phone * ", background = "white", foreground = "#33414f",
                                    font = "georgia 12", anchor = 's')
        guardianphone_label.place(x = 460, y = 260)

        guardianrole_label = Label(self.g_frame, text = "Enter Role", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianrole_label.place(x = 460, y = 300)

        guardianaddr_label = Label(self.g_frame, text = "Enter Address", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianaddr_label.place(x = 460, y = 340)

        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR GUARDIAN DETAILS#
        gname_var = StringVar()
        gname_entrybox = Entry(self.g_frame, width = 13,borderwidth = 1 ,bg="#efefef",font = "georgia 12 ",  textvariable = gname_var 
                            , relief = "groove",validate="key",validatecommand=(regstr,"%P"))
        gname_entrybox.place(x = 650, y = 227)

        gphone_var = IntVar()
        gphone_entrybox = Entry(self.g_frame,width = 13,borderwidth = 1 ,bg="#efefef",font = "georgia 12 ",  textvariable = gphone_var 
                            , relief = "groove",validate="key",validatecommand=(regint,"%P"))
        gphone_entrybox.place(x = 650, y = 267)

        grole_var = StringVar()
        grole_combobox = ttk.Combobox(self.g_frame, width = 16, textvariable = grole_var, state = 'readonly')
        grole_combobox['values'] = ('GUARDIAN', 'FATHER', 'MOTHER')
        grole_combobox.place(x = 650, y = 307,width=135)

        gaddr_var = StringVar()
        gaddr_entrybox = Entry(self.g_frame, width = 13,borderwidth = 1 ,bg="#efefef",font = "georgia 12 ",  textvariable = gaddr_var 
                            , relief = "groove")
        gaddr_entrybox.place(x = 650, y = 347)
        def saveg():
            self.gname=gname_var.get()
            self.gphone=gphone_var.get()
            self.grole=grole_var.get()
            self.gaddr=gaddr_var.get()
            if(self.gname=="" or self.gphone==""):
                messagebox.showerror("ERROR","Compulsory Values Cannot Be NUll")
                self.guardian()
            else:
                guardian(self.st_id,self.g_id,self.gname,self.grole,self.gaddr,self.gphone)
                answer=messagebox.askokcancel("Confirm","Add more guardians?")  
                if answer:
                    self.guardian(self.sgid)
                    self.g_id = self.g_id + 1    
                else:
                    self.g_frame.destroy()
                    b=Booking(self.st_id)

        label = Label(self.label_2, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 150, y = 440)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = saveg)
        submit.place(x = 14, y = 8)

    # ======================================================================#
    # END MAINLOOP FOR SECOND WINDOW#
    def contact(self,stid):
        self.stu_frame = Frame(window1,bg = "#efefef")
        self.stu_frame.place(x=0,y=0,height=1350,width=1350)
        self.background_label2 = Label(self.stu_frame, bg = "#1daf9b")
        self.background_label2.place(x = 0, y = 0, height = 330, width = 1350)

        self.bottom_label = Label(self.stu_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b", anchor = "n")
        self.bottom_label.place(x = 0, y = 680, height = 100, width = 1350)

        self.label_1 = Label(self.stu_frame, bg = "white", borderwidth = 3, relief = "raised")
        self.label_1.place(x = 450, y = 100, height = 500, width = 400) 
        tablename_label = ttk.Label(self.label_1, text = "Contact Details", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 20 bold ")
        tablename_label.place(x =90, y =5)
        apt_label = ttk.Label(self.label_1, text = "AptNo", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        apt_label.place(x = 20, y = 70)
        buildg_label = ttk.Label(self.label_1, text = "Building Name", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        buildg_label.place(x = 20, y = 120)
        state_label = ttk.Label(self.label_1, text = "State", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        state_label.place(x = 20, y = 170)

        city_label = ttk.Label(self.label_1, text = "City", background = "white", foreground = "#33414f",
                               font = "georgia 12", anchor = 's')
        city_label.place(x = 20, y = 220)

        street_label = ttk.Label(self.label_1, text = "Street", background = "white", foreground = "#33414f",
                                 font = "georgia 12", anchor = 's')
        street_label.place(x = 20, y = 270)
        phone_label = ttk.Label(self.label_1, text = "Phone no", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        phone_label.place(x = 20, y = 320)
        alt_label = ttk.Label(self.label_1, text = "Alternative Phone no", background = "white", foreground = "#33414f",
                              font = "georgia 12", anchor = 's')
        alt_label.place(x = 20, y = 370)
        #entry boxes for contact
        apt_var=StringVar()
        apt_entrybox = Entry(self.label_1, width = 13, borderwidth = 1, bg="#efefef",font = "georgia 12"
                            ,relief = "groove", textvariable = apt_var)
        apt_entrybox.place(x = 20 , y = 95,width=325)
        bldg_var=StringVar()
        bldg_entrybox = Entry(self.label_1, width = 13, borderwidth = 1 ,bg="#efefef" ,font = "georgia 12"
                            ,relief = "groove", textvariable = bldg_var)
        bldg_entrybox.place(x = 20 , y = 140,width=325)
        state_var = StringVar()
        state_entrybox = Entry(self.label_1, width = 13, borderwidth = 1 ,bg="#efefef", font = "georgia 12"
                            ,relief = "groove", textvariable = state_var)
        state_entrybox.place(x = 20 , y = 190,width=325)

        city_var = StringVar()
        city_entrybox = Entry(self.label_1, width = 13,  borderwidth = 1 ,bg="#efefef", font = "georgia 12 "
                            ,relief = "groove",textvariable = city_var)
        city_entrybox.place(x = 20, y = 240,width=325)

        street_var = StringVar()
        street_entrybox = Entry(self.label_1, width = 13, borderwidth = 1 ,bg="#efefef", font = "georgia 12 ",relief = "groove", textvariable = street_var)
        street_entrybox.place(x = 20 , y = 290,width=325)
        
        phone_var = StringVar()
        phone_entrybox = Entry(self.label_1, width = 13,borderwidth = 1 ,bg="#efefef", font = "georgia 12",textvariable = phone_var ,
                               relief = "groove",validate="key",validatecommand=(regint,"%P"))
        phone_entrybox.place(x = 20, y = 340,width=325)

        alt_var = StringVar()
        alt_entrybox = Entry(self.label_1, width = 13,borderwidth = 1 ,bg="#efefef",font = "georgia 12 ",  textvariable = alt_var 
                            , relief = "groove",validate="key",validatecommand=(regint,"%P"))
        alt_entrybox.place(x = 20 , y = 390,width=325)
        def save():        
            answer=messagebox.askokcancel("Confirm","Do you want to continue with registration ?")  
            if answer :
                self.sphoneno1 = phone_var.get()
                self.sphoneno2 = alt_var.get()
                self.state = state_entrybox.get()
                self.city = city_entrybox.get()
                self.street = street_entrybox.get()                
                self.apt = apt_entrybox.get()
                self.bldg = bldg_entrybox.get()
                re = studentinsert(self.st_id,self.fname,self.lname,self.gender,self.newface,self.newproof,self.apt,self.bldg,self.street,self.city,self.state)
                if re[0] == -1 :
                    messagebox.showerror("ERROR FOUND", "ALREADY REGISTERED ERP ID ")
                    self.student()
                if re[0] == 1:
                    messagebox.showinfo("REGISTERED ", "CONTINUE")
                    studentphone(self.st_id,self.sphoneno1)
                    studentphone(self.st_id,self.sphoneno2)
                    self.guardian(self.st_id)
            else :
                window1.destroy()            
        label = Label(self.label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 150, y = 440)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = lambda:[save(),self.stu_frame.destroy])
        submit.place(x = 14, y = 8)
    def student(self):
        self.stu_frame = Frame(window1,bg = "#efefef")
        self.stu_frame.place(x=0,y=0,height=1350,width=1350)
        self.background_label2 = Label(self.stu_frame, bg = "#1daf9b")
        self.background_label2.place(x = 0, y = 0, height = 330, width = 1350)

        self.bottom_label = Label(self.stu_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b", anchor = "n")
        self.bottom_label.place(x = 0, y = 680, height = 100, width = 1350)

        self.label_1 = Label(self.stu_frame, bg = "white", borderwidth = 3, relief = "raised")
        self.label_1.place(x = 450, y = 100, height = 500, width = 400) 
        tablename_label = ttk.Label(self.label_1, text = "Student Details", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 20 bold ")
        tablename_label.place(x =90, y =5)

        studentid_label = ttk.Label(self.label_1, text = "ERP ID * ", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 12")
        studentid_label.place(x = 20, y = 70 )

        firstname_label = ttk.Label(self.label_1, text = "First name * ", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 12")
        firstname_label.place(x = 20, y = 130)

        lastname_label = ttk.Label(self.label_1, text = "Last name *", background = "white",
                                   foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        lastname_label.place(x = 20, y = 180)
        gender_label = ttk.Label(self.label_1, text = "Gender", background = "white",
                                 foreground = "#33414f",
                                 font = "georgia 12", anchor = 's')
        gender_label.place(x = 20, y = 230)

        face_label = ttk.Label(self.label_1, text = "Face photo * ", background = "white", foreground = "#33414f",
                               font = "georgia 12", anchor = 's')
        face_label.place(x = 20, y = 280)

        idproof_label = ttk.Label(self.label_1, text = "ID Proof * ", background = "white",
                                  foreground = "#33414f",
                                  font = "georgia 12", anchor = 's')
        idproof_label.place(x = 20, y = 350)




        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR STUDENT DETAILS#

        stid_var = IntVar()
        stid_entrybox = Entry(self.label_1, width = 13, textvariable = stid_var , font = "georgia 12"
                                , borderwidth = 1 ,bg="#efefef", relief = "groove",validate="key",validatecommand=(regint,"%P") )
        stid_entrybox.place(x = 20, y = 95,width=350)
        stid_entrybox.focus()

        firstname_var = StringVar()
        firstname_entrybox = Entry(self.label_1, width = 13, font = "georgia 12 ",borderwidth = 1 ,bg="#efefef",
                            relief = "groove", textvariable = firstname_var,validate="key",validatecommand=(regstr,"%P"))
        firstname_entrybox.place(x = 20, y = 150,width=350)

        lastname_var = StringVar()
        lastname_entrybox = Entry(self.label_1, width = 13, borderwidth = 1,bg="#efefef", font = "georgia 12"
                            ,relief = "groove", textvariable = lastname_var,validate="key",validatecommand=(regstr,"%P"))
        lastname_entrybox.place(x = 20 , y = 200,width=350)
        gender_var = StringVar()
        gender_combobox = ttk.Combobox(self.label_1, width = 14,background="#efefef", textvariable = gender_var, state = 'readonly')
        gender_combobox['values'] = ('Male', 'Female')
        gender_combobox.place(x = 20, y = 250,width=350)
        facelabel=Label(self.label_1,bg="white")
        facelabel.place(x = 20, y = 330,width=350)
        prooflabel=Label(self.label_1,bg="white")  
        prooflabel.place(x = 20, y = 400,width=350)
        # ----------------------------------------------------------------------#
        # BUTTONS FOR STUDENT DETAILS#
        
        def filed():
            face = filedialog.askopenfilename(initialdir = "/", title = "Select Image",            
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            
            g="""\\\\"""            
            self.newface=str(face.replace('/',g))
            facelabel['text']=face
                                               
            
            
        def filedi():
            idproof = filedialog.askopenfilename(initialdir = "/", title = "Select Image",
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            g="""\\\\"""            
            #self.newface=str(face.replace('/',g))
            self.newproof=str(idproof.replace('/',g))            
            self.idproof=str(idproof)                                   
            prooflabel['text']=idproof                                  
            

        uploadface_button = Button(self.label_1, text = 'upload', command = lambda: filed(),cursor = "hand2")
        uploadproof_button = Button(self.label_1, text = 'upload', command = lambda: filedi(),cursor = "hand2")
        uploadface_button.place(x =20, y = 300,width=350)        
        uploadproof_button.place(x = 20, y = 375,width=350)

        # ----------------------------------------------------------------------#
        # DESTROY THE WINDOW 1#

        def save(): 
            self.st_id = stid_entrybox.get()
            self.fname = firstname_entrybox.get()
            self.lname = lastname_entrybox.get()
            self.gender = gender_combobox.get()
            if (self.st_id=="" or self.fname=="" or self.lname=="" or self.newproof=="" or self.newface == "") :
                messagebox.showerror("ERROR","Compulsory Values Cannot Be NUll")
                self.student()
            else :
                if (self.st_id < str(1032000000)):
                    messagebox.showerror("ERROR","ERP ID should be greater than 1032000000")
                    self.student()
                else :
                    self.contact(self.st_id)

        label = Label(self.label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 150, y = 440)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = lambda:[save(),self.stu_frame.destroy])
        submit.place(x = 14, y = 8)

#------------------------------------------END OF REGISTRATION-----------------------------------------------
#------------------------------------------STUDENT PAGE------------------------------------------------------

class Student():
    la1 = ImageTk.PhotoImage(Image.open(r"label.png").resize((100, 40)))
    submit_logo = ImageTk.PhotoImage(Image.open(r"label.png").resize((100, 35)))
    add = ImageTk.PhotoImage(Image.open(r'add.jpeg').resize((35,40)))
    #grd = ImageTk.PhotoImage(Image.open(r'grad.png').resize((1350,1350)))
    photo = ImageTk.PhotoImage(Image.open(r'abc.png').resize((200,200)))
    stu_id = 0
    stu_phone = ""
    bid = 0
    rid = 0
    paymentss =""
    def stu_page(self):
        window1.title("STUDENT PAGE")
        stu_frame1 = Label(window1, bg = "#f6f6f6" )
        stu_frame1.place(x= 0 , y= 0 , height = 1350 , width = 1350)
        top_label = Label(stu_frame1, bg = "#1daf9b")
        top_label.place(x = 0, y = 0, height = 30, width = 1350)
        bottom_label = Label(stu_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b")
        bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        vertical_frame = Frame(stu_frame1, bg = "#33414f" , borderwidth = 0.6)
        vertical_frame.place(x = 0, y = 30, height = 650, width = 280)
        s_frame = Frame(stu_frame1, bg = "white" , borderwidth = 0.6 , relief = "raised")
        s_frame.place(x = 350, y = 60, height = 300, width = 300)
        s_detail = Label(s_frame, text = "Student Details",
                         font = "georgia 18 bold", fg = "#33414f", bg = "white")
        s_detail.place(x = 0, y = 0)
        guard_frame = Frame(stu_frame1, bg = "white" , borderwidth = 0.6 , relief = "raised")
        guard_frame.place(x = 780, y = 60, height = 300, width = 490)

        pay_frame = Frame(stu_frame1 , bg = "white" , borderwidth = 0.6 , relief = "raised")
        pay_frame.place(x=780,y=400 , height = 250 , width = 490)

        c_frame = Frame(stu_frame1, bg = "white" , borderwidth = 0.6 , relief = "raised")
        c_frame.place(x = 350, y = 400, height = 250, width = 300)

        payment_detail = Label(pay_frame, text = "Payment Details",
                         font = "georgia 18 bold", fg = "#33414f", bg = "white")
        payment_detail.place(x = 0, y = 0)
        
        g_detail = Label(guard_frame, text = "Guardian Details  "
                           ,font = "georgia 18 bold", fg = "#33414f", bg = "white")
        g_detail.place(x = 0, y = 0)

        image = readBLOB(self.stu_id)
        g="""\\\\""" 
        i =str(image.replace('/',g))
        self.photo = ImageTk.PhotoImage(Image.open(r"abc.png").resize((200,200)))
        photo_label = Label(vertical_frame, image = self.photo , bg = "#33414f")
        photo_label.place(x=30,y=30 , height = 200 , width = 200)

        student = student_info(self.stu_id)
        for i in student : 
            sidl = Label(vertical_frame, text = "ID :                      {}\n".format(i[0]), fg = "#efefef", bg = "#33414f",
                     font = "Georgia 12")
            sidl.place(x = 0, y = 300)
            snamel = Label(vertical_frame, text = "Name :                {}\n".format(i[1] + " " + i[2]), fg = "#efefef", bg = "#33414f",
                       font = "Georgia 12")
            snamel.place(x = 0, y = 330)
            sphone = Label(s_frame, text = "Phone number :           {}".format(self.stu_phone), fg = "#33414f", bg = "white", 
                       font = "Georgia 12")
            sphone.place(x = 0, y = 60)   
            saddr = Label(s_frame, text = "Student Address :           {}, ".format(i[6]),
                         bg = "white", fg = "#33414f", font = "Georgia 12")
            saddr.place(x = 0, y = 90)
            saddr4 = Label(s_frame, text = "                                    {}, ".format(i[7]),
                         bg = "white", fg = "#33414f", font = "Georgia 12")
            saddr4.place(x = 0, y = 120)
            saddr1 = Label(s_frame, text = "                                    {}, ".format(i[8]),
                         bg = "white", fg = "#33414f", font = "Georgia 12")
            saddr1.place(x = 0, y = 150)
            saddr2 = Label(s_frame, text = "                                    {},".format(i[9]),
                         bg = "white", fg = "#33414f", font = "Georgia 12")
            saddr2.place(x = 0, y = 180)
            saddr3 = Label(s_frame, text = "                                    {}.".format(i[10]),
                         bg = "white", fg = "#33414f", font = "Georgia 12")
            saddr3.place(x = 0, y = 210)
            sgen = Label(vertical_frame, text = "Gender :               {}\n".format(i[3]), fg = "#efefef", bg = "#33414f",
                       font = "Georgia 12")
            sgen.place(x = 0, y = 360)
        
        hostel = hostel_info(self.stu_id)
        for j in hostel :
            hostel_detail = Label(vertical_frame, text = "Hostel :               {}\n".format(j[0]),fg = "#efefef", bg = "#33414f",
                           font = "Georgia 12")
            hostel_detail.place(x = 0, y = 390)
            hostel_detail = Label(vertical_frame, text = "Room :               {}\n".format(j[1]),fg = "#efefef", bg = "#33414f",
                           font = "Georgia 12")
            hostel_detail.place(x = 0, y = 420)
            self.bid = j[3]
            self.rid = j[1]
        guardian = guradian_info(self.stu_id)
        frame = Frame(guard_frame , bg ="white" , borderwidth = 0)
        frame.place(x = 5, y= 40 , height = 250 , width = 470)
        g_frame = ScrollableFrame(frame)
        g_frame.place(x = 0, y= 0 , height = 250 , width = 470)
        g_name = []
        g_role = []
        g_addr = []
        x = len(guardian)
        for i in range(x):
            g_name.append(tk.Label(g_frame.scrollable_frame, text = "Guardian Name :         {} \n".format(guardian[i][2]) ,
                         font = "georgia 12", fg = "#33414f", bg = "white").pack(anchor = "nw"))
            g_name.append(Label(g_frame.scrollable_frame, text = "Guardian Role :           {}\n".format(guardian[i][3]),
                         font = "georgia 12", fg = "#33414f", bg = "white").pack(anchor = "nw"))
            g_name.append(Label(g_frame.scrollable_frame, text = "Guardian Address :     {}\n".format(guardian[i][4]),
                         font = "georgia 12", fg = "#33414f", bg = "white").pack())

        '''def edit_student_info():
            sphone_var = IntVar()
            sphone_entrybox = Entry(s_frame, textvariable = sphone_var , font = "georgia 12 " ,bg = "#EFEFEF",validate="key",validatecommand=(regint,"%P"))
            sphone_entrybox.place(x = 130 , y = 60 , width = 150)

            sadd1_var = StringVar()
            sadd_entrybox = Entry(s_frame, textvariable = sadd_var , font = "georgia 12 ", bg = "#efefef")
            sadd_entrybox.place(x=130 , y = 95 , width = 150)



            label = Label(s_frame, image = self.submit_logo, borderwidth = 0, bg = "white")
            label.place(x = 100, y = 240)
            def callsubmit():
                messagebox.showinfo("UPDATE REQUEST ", "Request for updation is sent to the administration")    
                sphone_entrybox.destroy()
                sadd_entrybox.destroy()
                label.destroy()
                submit.destroy()
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9" , command = callsubmit)
            submit.place(x = 12, y = 5)

        edit_info = Button(s_frame, image = edit, fg = "#F6F6F6" , borderwidth = 0 , command = edit_student_info)
        edit_info.place(x = 270, y = 0)'''

        add_complaint = Label(c_frame , text = "Complaint box" 
                         ,font = "georgia 18 bold", fg = "#33414f", bg = "white" )
        add_complaint.place(x=0,y=0)

        c = view_comp(self.stu_id)
        for i in c:
            co = Label(c_frame , text = i[0]
                         ,font = "georgia 12", fg = "#33414f", bg = "white")
            co.place(x=30,y=60)

        def add_compt() : 
            add_entrybox = Entry(c_frame ,font = "georgia 12 " ,bg = "#efefef")
            add_entrybox.place(x=30 , y = 60 , height = 80 , width = 240)

            label = Label(c_frame, image = self.submit_logo, borderwidth = 0, bg = "white")
            label.place(x = 110, y = 160)
            def callsubmit():
                messagebox.showinfo("COMPLAINT ", "Your complaint has been sent to the administration")   
                complt = add_entrybox.get()
                add_com(self.stu_id,complt) 
                add_entrybox.destroy()
                label.destroy()
                submit.destroy()
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9" , command = callsubmit)
            submit.place(x = 12, y = 5)
        
        edit_complaint = Button(c_frame , image = self.add , fg = "#f6f6f6" , borderwidth = 0 , command = add_compt,cursor = "hand2")
        edit_complaint.place(x= 260 , y=0)

        pay = view_payment(self.bid)
        for x in pay :
            display = Label(pay_frame,text = "Balance : Rs {}".format(x[0]),font = "georgia 12", fg = "#33414f", bg = "white" )
            display.place(x=30,y=30)
        def edit_pay():
            pay_type = StringVar()
            disp = Label(pay_frame,text="Payment Type",font = "georgia 12",fg = "#33414f",bg="white")
            disp.place(x=30,y=60)
            price_combobox = ttk.Combobox(pay_frame, width = 14,font="georgia 12",foreground = "#33414f",textvariable = pay_type, state = 'readonly')
            price_combobox.place(x = 30, y = 80,width=200)
            price_combobox['values']=['Credit Card ', 'Debit Card','UPI Wallet','Net Banking']
            price_combobox.set('Net Banking')
            self.date=Label(pay_frame,text="Payment Date",font = "georgia 12",fg = "#33414f",bg="white")
            self.date.place(x=30,y=110)
            self.cal = DateEntry(pay_frame, background="#33414f",foreground="white",activebackground="#33414f", borderwidth=2,year=datetime.datetime.today().year)
            self.cal.place(x = 30, y = 140,width=200)
            self.sslabel=Label(pay_frame,bg="white")
            self.sslabel.place(x =0, y = 210,width=375)
            def uploadss():
                ss = filedialog.askopenfilename(initialdir = "/", title = "Select Image",            
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            
                g="""\\\\"""            
                self.paymentss=str(ss.replace('/',g))
                self.sslabel['text']=ss
            self.pss=Label(pay_frame,text="Payment Screenshot",font = "georgia 12",fg = "#33414f",bg="white")
            self.pss.place(x=30,y=170)
            self.pssbutton= Button(pay_frame,text="upload" ,bg = "#efefef",cursor="hand2",command=uploadss)
            self.pssbutton.place(x=30,y=190,width=200)

            self.slabel = Label(pay_frame, image = self.la1, borderwidth = 0, bg = "white")
            self.slabel.place(x = 290, y = 120)
            def payment_done():
                ptype = pay_type.get()
                self.pdate=self.cal.get_date()
                if(self.paymentss==""):
                    messagebox.showwarning("Screenshot","Payment Screenshot Necessary!!")
                else:
                    messagebox.showinfo("DONE","Payment done !")
                    insert_payment(ptype,pay[0][0],self.pdate,self.paymentss,self.bid)
                    price_combobox.destroy()
                    disp.destroy()
                    self.date.destroy()
                    self.cal.destroy()
                    self.sslabel.destroy()
                    self.pss.destroy()
                    self.pssbutton.destroy()
                    self.slabel.destroy()

            self.submit = Button(self.slabel, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                                relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                                highlightcolor = "#1dafb9", command = payment_done)
            self.submit.place(x = 12, y = 8)


        edit_payment = Button(pay_frame, image = edit, fg = "#F6F6F6" , borderwidth = 0 , command = edit_pay,cursor = "hand2")
        edit_payment.place(x = 460, y = 0)

        def over():
            window1.destroy()

        global logout 
        logout = ImageTk.PhotoImage(Image.open(r"label2.png").resize((100,40)))
        log_label = Label(vertical_frame ,image = logout, fg = "#33414f", font = "georgia 10 bold", bg = "#33414f" , borderwidth = 0 , relief = "flat")
        log_label.place(x=75,y=550)
        logout_button = Button(log_label,text = "LOGOUT", fg = "#33414f", font = "georgia 10 bold", bg = "#1daf9b",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1daf9b",
                        highlightcolor = "#1daf9b" , command = over)
        logout_button.place(x=10,y=5)


    def generate_otp(self):
        window1.title("STUDENT LOGIN PAGE")
        window_frame2 = Frame(window1, bg = "#efefef")
        window_frame2.place(x = 0, y = 0, height = 1350, width = 1350)

        background_label = Label(window_frame2, text = "@2020 by CET,SCET,MITWPU,All rights reserved.", font = "georgia",
                                 fg = "#33414f", bg = "#1daf9b")
        background_label.place(x = 0, y = 680, height = 30, width = 1350)

        background_label2 = Label(window_frame2, bg = "#1daf9b")
        background_label2.place(x = 0, y = 0, width = 1350, height = 330)

        label_1 = Label(window_frame2, bg = "white", borderwidth = 3, relief = "raised")
        label_1.place(x = 450, y = 100, height = 500, width = 400)    
        otp_no = StringVar()
        logo = Label(label_1, image = logo2, borderwidth = 0, bg = "white")
        logo.place(x = 100, y = 0)
        display_l = Label(label_1, fg = "#33414f", bg = "white", borderwidth = 1)
        display_l.place(x = 1, y = 180, height = 200, width = 350)

        main = Label(display_l, text = "LOGIN", bg = "white", fg = "#33414f", font = "georgia 20 bold")
        main.place(x = 140, y = 0)
        labelbox = Label(display_l, borderwidth = 0, bg = "white")
        labelbox.place(x=20,y=0 , height = 200 ,width = 400)
        
        label_otp = Label(labelbox, text = "ENTER VALID OTP ",font = "georgia 12", borderwidth = 0, bg = "white",fg ="grey")
        label_otp.place(x=10,y=40)
        enter_otp = Entry(labelbox , textvariable = otp_no,font = "georgia 12", borderwidth = 0.6 , bg = "white" , relief = "groove")
        enter_otp.place(x=10,y=60,height = 30 , width = 400)
            
        '''smp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        OTP = ""
        length = len(smp)
        for i in range(6):
            OTP += smp[math.floor(random.random() * length)]
            
        notif = ("Your OTP is: " + str(OTP))
        url = "https://www.fast2sms.com/dev/bulk"
            
        querystring = {"authorization":"vTaWBKucoELspqAHSl9t2NCm1w05xdMYfGbeiUJngIQVz4DR3XsUBDu2P6loCar5IfRxvWdNLgkqQFH9",
                            "sender_id":"HOSTELMS","message":notif,"language":"english","route":"p","numbers":self.stu_phone}
            
        headers = {
                    'cache-control': "no-cache"
        }
            
        response = requests.request("GET", url, headers=headers, params=querystring)

        def register_page():
            Entry = otp_no.get()
            if Entry == OTP:
                stud_window.destroy()
                
            else:
                error = Label(frame1, text = "TRY AGAIN , OTP WRONG !",bg="#8c54a1",fg = "white",font = "times 20 ")
                error.grid(row = 6,column = 1)
           '''

        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 152, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                    relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = self.stu_page)
        submit.place(x = 14, y = 8)

    def stud_login(self):
        # --------------------------------------------STUDENT LOGIN PAGE----------------------------------------------------------------------
        window1.title("STUDENT LOGIN PAGE")

        window_frame2 = Frame(window1, bg = "#efefef")
        window_frame2.place(x = 0, y = 0, height = 1350, width = 1350)

        background_label = Label(window_frame2, text = "@2020 by CET,SCET,MITWPU,All rights reserved.", font = "times",
                                 fg = "#33414f", bg = "#1daf9b")
        background_label.place(x = 0, y = 680, height = 30, width = 1350)

        background_label2 = Label(window_frame2, bg = "#1daf9b")
        background_label2.place(x = 0, y = 0, width = 1350, height = 330)

        label_1 = Label(window_frame2, bg = "white", borderwidth = 3, relief = "raised")
        label_1.place(x = 450, y = 100, height = 500, width = 400)

        logo = Label(label_1, image = logo2, borderwidth = 0, bg = "white")
        logo.place(x = 100, y = 0)
        display_l = Label(label_1, fg = "#33414f", bg = "white", borderwidth = 1)
        display_l.place(x = 1, y = 180, height = 200, width = 350)

        main = Label(display_l, text = "LOGIN", bg = "white", fg = "#33414f", font = "georgia 20 bold")
        main.place(x = 140, y = 0)
        std_id = Label(display_l, text = "  STUDENT ID ", bg = "white", fg = "grey", font = "georgia 12 ")
        std_id.place(x = 10, y = 40)
        phone = Label(display_l, text = "  PHONE NUMBER ", bg = "white", fg = "grey", font = "georgia 12 ")
        phone.place(x = 10, y = 100)

        id = IntVar()
        stdid_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white",textvariable = id,validate="key",validatecommand=(regint,"%P"))
        stdid_enter.place(x = 20, y = 60, width = 400, height = 30)

        phoneno = StringVar()

        stdphone_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white",textvariable = phoneno,validate="key",validatecommand=(regint,"%P"))
        stdphone_enter.place(x = 20, y = 120, width = 400, height = 30)

        def check():
            self.stu_id = id.get()
            self.stu_phone = phoneno.get()
            result = checkstudent(self.stu_id,self.stu_phone)
            if result == 0:
                messagebox.showinfo("ERROR FOUND ", "NOT VERIFIED , WAIT FOR VERFIICATION")
            elif result == 1 :
                messagebox.showinfo("REGISTRATION ", "OK CORRECT , PRESS OK !" ) 
                self.generate_otp()
            elif result == -1:
                messagebox.showinfo("ERROR FOUND ", "NOT REGISTERED ID , REGISTER FIRST !")

        def register():
            r = RegisterStudent()
            # r.student()
            # r.guardian()


        newuser = Button(label_1, text = "New User!Register?", fg = "#33414f", bg = "white",cursor = "hand2",
                         font = "georgia 12 bold underline", relief = "flat", borderwidth = 0,
                         activebackground = "white", activeforeground = "#33414f", highlightcolor = "white",
                         command = register)
        newuser.place(x = 13, y = 335)
        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 152, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = check)
        submit.place(x = 14, y = 8)

#-----------------------------------------MANAGER PAGE -------------------------------------------------------

class Manager:
    id = 0
    name = ""
    var = IntVar()
    hid = 0
    la2 = ImageTk.PhotoImage(Image.open(r"cross.jpeg").resize((20,20)))
    la1 = ImageTk.PhotoImage(Image.open(r"label.png").resize((150, 45)))

    def generate_otp_1(self):
        window1.title("MANAGER LOGIN PAGE")

        window_frame2 = Frame(window1, bg = "#efefef")
        window_frame2.place(x = 0, y = 0, height = 1350, width = 1350)

        background_label = Label(window_frame2, text = "@2020 by CET,SCET,MITWPU,All rights reserved.", font = "times",
                                 fg = "#33414f", bg = "#1daf9b")
        background_label.place(x = 0, y = 680, height = 30, width = 1350)

        background_label2 = Label(window_frame2, bg = "#1daf9b")
        background_label2.place(x = 0, y = 0, width = 1350, height = 330)

        label_1 = Label(window_frame2, bg = "white", borderwidth = 3, relief = "raised")
        label_1.place(x = 450, y = 100, height = 500, width = 400)    
        otp_no = StringVar()
        logo = Label(label_1, image = logo2, borderwidth = 0, bg = "white")
        logo.place(x = 100, y = 0)
        display_l = Label(label_1, fg = "#33414f", bg = "white", borderwidth = 1)
        display_l.place(x = 1, y = 180, height = 200, width = 350)

        main = Label(display_l, text = "LOGIN", bg = "white", fg = "#33414f", font = "georgia 20 bold")
        main.place(x = 140, y = 0)
        labelbox = Label(display_l, borderwidth = 0, bg = "white")
        labelbox.place(x=20,y=0 , height = 200 ,width = 400)
        
        passwd = StringVar()
        label_pass = Label(labelbox, text = "ENTER VALID PASSWORD ",font = "georgia 12", borderwidth = 0, bg = "white",fg ="grey" )
        label_pass.place(x=10,y=40)
        enter_pass = Entry(labelbox , textvariable = passwd,font = "georgia 12 bold", borderwidth = 0.6 , bg = "white" , relief = "groove" , show = "*")
        enter_pass.place(x=10,y=60,height = 30 , width = 400)

        def checkpass() : 
            pasw = passwd.get()
            if pasw == "Manager@hms0202":
                messagebox.showinfo("CORRECT ", "OK CORRECT , PRESS OK !")
                self.mgr_page()
            else :
                messagebox.showinfo("ERROR FOUND ", "INCORRECT PASSWORD , TRY AGAIN !")                
   
        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 152, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = checkpass)
        submit.place(x = 14, y = 8)

    def mgr_page(self):
        window1.title("MANAGER PAGE")
        mgr_frame1 = Frame(window1, bg = "#efefef")
        mgr_frame1.place(x = 0, y = 0, height = 1350, width = 1350)
        bottom_label = Label(mgr_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b")
        bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        vertical_frame = Frame(mgr_frame1, bg = "#33414f")
        vertical_frame.place(x = 0, y = 0, height = 680, width = 280)
        top_label = Label(mgr_frame1, bg = "#1daf9b")
        top_label.place(x = 0, y = 0, height = 30, width = 1350)
        self.name = getemployee(self.id)
        empidl = Label(vertical_frame, text = "ID:              {}".format(self.id), fg = "#efefef", bg = "#33414f",
                       font = "Georgia")
        empidl.place(x = 0, y = 200)
        empnamel = Label(vertical_frame, text = "Name:        {}".format(self.name[0]), fg = "#efefef", bg = "#33414f",
                         font = "Georgia")
        empnamel.place(x = 0, y = 230)

        def addemp():
            frame = Frame(mgr_frame1 , relief = "groove" , borderwidth = 0.6,bg="white")
            frame.place(x=770, y = 100 , height = 300 , width = 470)
            
            add_detail = Label(frame, text = "Add Employee",
                         font = "georgia 20 bold", fg = "#33414f", bg = "white")
            add_detail.place(x = 0, y = 18)
            ename_detail = Label(frame, text = "Employee Name",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            ename_detail.place(x = 30, y = 60)
            ename_var = StringVar()
            ename_entry = Entry(frame, width = 16,bg = "#efefef", textvariable = ename_var,validate="key",validatecommand=(regstr,"%P"))
            ename_entry.place(x = 30 , y = 80 , width =  290)
            empaddr_detail = Label(frame, text = "Employee Address",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            empaddr_detail.place(x = 30, y = 120)
            eaddr_var = StringVar()
            eaddr_entry = Entry(frame, width = 16,bg = "#efefef", textvariable = eaddr_var)
            eaddr_entry.place(x = 30 , y = 140 , width =  290)
            erole_detail = Label(frame, text = "Employee Role",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            erole_detail.place(x = 30, y = 180)
            role_var = StringVar()
            role_combobox = ttk.Combobox(frame, width = 16, textvariable = role_var, state = 'readonly')
            role_combobox['values'] = ('Manager','Cook','Cleaner')
            role_combobox.place(x = 30 , y = 200, width =  290)
            label = Label(frame, image = self.la1, borderwidth = 0, bg = "white")
            label.place(x = 190, y = 250)
            def insertemp():
                ename=ename_var.get()
                eaddr=eaddr_var.get()
                role=role_var.get()
                if ename == "" or eaddr == "" or role == "":
                    messagebox.showerror("ERROR FOUND", "NULL VALUES NOT ALLOWED ")
                    addemp()
                else :
                    addemps(ename,eaddr,role,self.hid)
                    messagebox.showinfo("INSERTED", "Employee Registered Successfully")
                    answer=messagebox.askokcancel("Confirm","Register more Employees?")  
                    if answer:
                        addemp()   
                    else:
                        frame.destroy()
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = insertemp)
            submit.place(x = 14, y = 8)

            crs = Button(frame,image = self.la2, command =frame.destroy , cursor = "hand2" , relief = "flat")
            crs.place(x = 440, y = 0)

        reg_emp = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0,command=addemp,cursor = "hand2")
        reg_emp.place(x = 630, y = 40)
        e_detail = Label(mgr_frame1, text = "Register Employee", anchor = "nw",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6")
        e_detail.place(x = 330, y = 40, width = 300)

        def verfification_sms(id):
            phone = student_phone(id)
            '''sms = "done for id  "
            notif = ("Your VERIFICATION for hostel is  " + str(sms) + "{}".format(id))
            url = "https://www.fast2sms.com/dev/bulk"
            
            querystring = {"authorization":"vTaWBKucoELspqAHSl9t2NCm1w05xdMYfGbeiUJngIQVz4DR3XsUBDu2P6loCar5IfRxvWdNLgkqQFH9",
                            "sender_id":"HOSTELMS","message":notif,"language":"english","route":"p","numbers":phone[0]}

            headers = {
                    'cache-control': "no-cache"
            }
            
            response = requests.request("GET", url, headers=headers, params=querystring)       '''     

        def ver_stu():
            s = view_student_to_verify(self.hid)
            check = []
            state =[]
            x = len(s)
            if x == 0 :
                messagebox.showinfo("FOUND","NO PENDING VERIFICATION REQUESTS!")
            else :
                frame = Frame(mgr_frame1 , relief = "groove" , borderwidth = 0.6)
                frame.place(x=770, y = 100 , height = 500 , width = 470)
                s_frame = ScrollableFrame(frame)
                s_frame.place(x = 0, y= 0 , height = 500 , width = 470)
                for i in range(x):
                    state.append(IntVar())
                    check.append(tk.Checkbutton(s_frame.scrollable_frame,text = "ID : {} / NAME : {} {} ".format(s[i][0],s[i][1],s[i][2]),var=state[i], font = "georgia 12 bold " , bg = "white").pack(anchor = "nw"))               
                def verifystudents():
                    answer=messagebox.askokcancel("CONFIRMATION","ARE YOU SURE YOU WANT TO VERIFY ?")
                    if answer:
                        for i in range(x):
                            if(state[i].get()==1):
                                verifystu(s[i][0])
                                verfification_sms(s[i][0])
                    s_frame.destroy()
                    frame.destroy()

                global l 
                l = ImageTk.PhotoImage(Image.open(r"e:/STUDY/TY sem - 7/DBMS/miniprojecct/final/ver.png").resize((100, 35)))                         
                self.label = Label(mgr_frame1, image = l, borderwidth = 0)
                self.label.place(x = 920 , y = 610)
                self.submit = Button(self.label,cursor = "hand2", text = "VERIFY", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                            relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                            highlightcolor = "#1dafb9", command = lambda:[verifystudents(),self.label1.destroy(),self.label.destroy(),self.submit.destroy(),self.submit1.destroy()])
                self.submit.place(x = 15, y = 5)

                def delete_values():
                    answer=messagebox.askokcancel("CONFIRMATION","ARE YOU SURE YOU WANT TO DELETE ?")
                    if answer:
                        for i in range(x):
                            if(state[i].get()==1):
                                deletestu(s[i][0])
                    s_frame.destroy()
                    frame.destroy()
                
                self.label1 = Label(mgr_frame1, image = l, borderwidth = 0, bg = "white")
                self.label1.place(x = 1020 , y = 610)
                self.submit1 = Button(self.label1, text = "DELETE", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                            relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9", cursor = "hand2",
                            highlightcolor = "#1dafb9", command = lambda:[delete_values(),self.label1.destroy(),self.label.destroy(),self.submit.destroy(),self.submit1.destroy()])
                self.submit1.place(x = 15, y = 5)

                crs = Button(frame,image = self.la2, command =frame.destroy , cursor = "hand2" , relief = "flat")
                crs.place(x = 440, y = 0)
            
        s_detail = Label(mgr_frame1, text = "Verify Student",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6" , anchor = "nw")
        s_detail.place(x = 330, y = 90, width = 300)
        ver_stu = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0, command = ver_stu)
        ver_stu.place(x = 630, y = 90)

        '''e_detail = Label(mgr_frame1, text = "Update Requests",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6" , anchor = "nw")
        e_detail.place(x = 330, y = 140, width = 300)
        reg_emp = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0)
        reg_emp.place(x = 630, y = 140)'''
        
        def checkcomplaint():
            c = verify_com()
            check = []
            state =[]
            x = len(c)
            if x == 0 :
                messagebox.showinfo("FOUND","NO PENDING COMPLAINTS !")
            else :
                frame = Frame(mgr_frame1 , relief = "groove" , borderwidth = 0.6)
                frame.place(x=770, y = 100 , height = 500 , width = 470)
                s_frame = ScrollableFrame(frame)
                s_frame.place(x = 0, y= 0 , height = 500 , width = 470)
                for i in range(x):
                    state.append(IntVar())
                    check.append(tk.Checkbutton(s_frame.scrollable_frame,text = "ID : {} / COMPLAINT : {}  ".format(c[i][0],c[i][1]),var=state[i], font = "georgia 12 bold " , bg = "white").pack(anchor = "nw"))               
                def verifycomp():
                    answer=messagebox.askokcancel("CONFIRMATION","ARE YOU SURE YOU WANT TO VERIFY ?")
                    if answer:
                        for i in range(x):
                            if(state[i].get()==1):
                                verifyc(c[i][0])
                    s_frame.destroy()
                    frame.destroy()
                crs = Button(frame,image = self.la2, command =frame.destroy , cursor = "hand2" , relief = "flat")
                crs.place(x = 440, y = 0)
                global l 
                l = ImageTk.PhotoImage(Image.open(r"e:/STUDY/TY sem - 7/DBMS/miniprojecct/final/ver.png").resize((100, 35)))                         
                self.label = Label(mgr_frame1, image = l, borderwidth = 0)
                self.label.place(x = 920 , y = 610)
                self.submit = Button(self.label, text = "VERIFY", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                            relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9", cursor = "hand2",
                            highlightcolor = "#1dafb9", command = lambda:[verifycomp(),self.label1.destroy(),self.label.destroy(),self.submit.destroy(),self.submit1.destroy()])
                self.submit.place(x = 15, y = 5)

                def delete_values():
                    answer=messagebox.askokcancel("CONFIRMATION","ARE YOU SURE YOU WANT TO DELETE ?")
                    if answer:
                        for i in range(x):
                            if(state[i].get()==1):
                                deletec(c[i][0])
                    s_frame.destroy()
                    frame.destroy()
                
                self.label1 = Label(mgr_frame1, image = l, borderwidth = 0, bg = "white")
                self.label1.place(x = 1020 , y = 610)
                self.submit1 = Button(self.label1, text = "DELETE", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                            relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9", cursor = "hand2",
                            highlightcolor = "#1dafb9", command = lambda:[delete_values(),self.label1.destroy(),self.label.destroy(),self.submit.destroy(),self.submit1.destroy()])
                self.submit1.place(x = 15, y = 5)

        e_detail = Label(mgr_frame1, text = "Student Complaints", anchor= "nw",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6")
        e_detail.place(x = 330, y = 140, width = 300)
        reg_emp = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0 , command = checkcomplaint)
        reg_emp.place(x = 630, y = 140)

        def addrooms():
            r=existroom(self.hid)
            frame = Frame(mgr_frame1 , relief = "groove" , borderwidth = 0.6,bg="white")
            frame.place(x=770, y = 100 , height = 300 , width = 470)
            
            add_detail = Label(frame, text = "Add Room",
                         font = "georgia 20 bold", fg = "#33414f", bg = "white")
            add_detail.place(x = 0, y = 18)

            no_detail = Label(frame, text = "Room No",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            no_detail.place(x = 30, y = 60)
            no_var = StringVar()
            no_entry = Entry(frame, width = 16, textvariable = no_var,validate="key",validatecommand=(regint,"%P"), bg= "#efefef" )
            no_entry.place(x = 30 , y = 80 , width =  290)

            type_detail = Label(frame, text = "Type Of Room",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            type_detail.place(x = 30, y = 120)
            type_var = StringVar()
            type_combobox = ttk.Combobox(frame, width = 16, textvariable = type_var, state = 'readonly')
            type_combobox['values'] = ('2 Bed - NORMAL', '2 Bed - AC','2 Bed - BALCONY', '3 Bed - Normal')
            type_combobox.place(x = 30 , y = 140 , width =  290)
            label = Label(frame, image = self.la1, borderwidth = 0, bg = "white")
            label.place(x = 190, y = 250)

            def insertroom():
                rid=no_var.get()
                types=type_var.get()
                if rid == "" or beds == "" or types == "" :
                    messagebox.showerror("ERROR FOUND", "NULL VALUES NOT ALLOWED")
                    addrooms()                  
                else :
                    if types == "2 Bed - NORMAL" :
                        bed = 2 
                        types = "NORMAL"
                    elif types == "2 Bed - AC" :
                        bed = 2 
                        types = "AC"
                    elif types == "2 Bed - BALCONY" :
                        bed = 2
                        types = "BALCONY"
                    elif types == "3 Bed - NORMAL" :
                        bed = 3
                        types = "NORMAL"  
                    re = addroom(self.hid,rid,bed,types)  
                    if re == -1 :
                        messagebox.showerror("ERROR FOUND", "ROOM NO. ALREADY EXISTS")
                        addrooms()
                    else:
                        messagebox.showinfo("INSERTED", "Room Added Successfully")
                        answer=messagebox.askokcancel("Confirm","Add more Rooms?")  
                        if answer:
                            addrooms()   
                        else:
                            frame.destroy()
            
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold", cursor = "hand2" ,
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = insertroom)
            submit.place(x = 14, y = 8)

            crs = Button(frame,image = self.la2, command =frame.destroy , cursor = "hand2" , relief = "flat")
            crs.place(x = 440, y = 0)

        r_detail = Label(mgr_frame1, text = "Add New Room ", anchor = "nw",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6")
        r_detail.place(x = 330, y = 190, width = 300)
        radd = Button(mgr_frame1, image = edit,cursor = "hand2", fg = "#F6F6F6", borderwidth = 0,command=addrooms)
        radd.place(x = 630, y = 190)

        def update_room_price():
            r = existprice(self.hid)
            frame = Frame(mgr_frame1 , relief = "groove" , borderwidth = 0.6,bg="white")
            frame.place(x=770, y = 100 , height = 500 , width = 470)
            
            add_detail = Label(frame, text = "Update Room Price",
                         font = "georgia 20 bold", fg = "#33414f", bg = "white")
            add_detail.place(x = 0, y = 18)
            room_detail = Label(frame, text = "EXISTING ROOMS :",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            room_detail.place(x = 30, y = 60)
            x = len(r)
            for i in range(x):
                room_detail = Label(frame, text = "Price : {} / Beds : {} / Type : {}".format(r[i][0],r[i][1],r[i][2]),
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
                room_detail.place(x = 30, y = 90+(i*20))
            room_detail = Label(frame, text = "ROOM TYPE :",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            room_detail.place(x = 30, y = 190)
            
            room_var = StringVar()
            room_combobox = ttk.Combobox(frame, width = 16, textvariable = room_var, state = 'readonly')
            room_combobox['values'] = ('2 Bed - NORMAL', '2 Bed - AC','2 Bed - BALCONY', '3 Bed - NORMAL')
            room_combobox.place(x = 30 , y = 210, width =  290)

            price_detail = Label(frame, text = "PRICE :",
                         font = "georgia 12 bold", fg = "#33414f", bg = "white")
            price_detail.place(x = 30, y = 240)

            price_var = StringVar()
            price_entry = Entry(frame, width = 16, textvariable = price_var,validate="key",validatecommand=(regint,"%P"), bg = "#efefef")
            price_entry.place(x = 30 , y = 260 , width =  290)
            label = Label(frame, image = self.la1, borderwidth = 0, bg = "white")
            label.place(x = 190, y = 400)
            def upd():
                ro=room_var.get()
                price=price_var.get()
                if ro == "" or price == "" :
                    messagebox.showerror("ERROR FOUND", "NULL VALUES NOT ALLOWED ")
                    update_room_price()
                else:
                    if ro == "2 Bed - NORMAL" :
                        bed = 2 
                        ro = "NORMAL"
                    elif ro == "2 Bed - AC" :
                        bed = 2 
                        ro = "AC"
                    elif ro == "2 Bed - BALCONY" :
                        bed = 2
                        ro = "BALCONY"
                    elif ro == "3 Bed - NORMAL" :
                        bed = 3
                        ro = "NORMAL"  
                    updateprice(price,ro,bed)
                    messagebox.showinfo("INSERTED", "Price Updated Successfully")
                    answer=messagebox.askokcancel("Confirm","Update more Room Price?")  
                    if answer:
                        update_room_price()   
                    else:
                        frame.destroy()

            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9", cursor = "hand2",
                        highlightcolor = "#1dafb9", command = upd)
            submit.place(x = 14, y = 8)
            crs = Button(frame,image = self.la2, command =frame.destroy , cursor = "hand2" , relief = "flat")
            crs.place(x = 440, y = 0)

        e_detail = Label(mgr_frame1, text = "Update Room Price ", anchor= "nw",
                         font = "georgia 18 bold", fg = "#33414f", bg = "#F6F6F6")
        e_detail.place(x = 330, y = 240, width = 300)
        reg_emp = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0 , command = update_room_price)
        reg_emp.place(x = 630, y = 240)

        def over():
            window1.destroy()
        global logout 
        logout = ImageTk.PhotoImage(Image.open(r"label2.png").resize((100,40)))
        log_label = Label(vertical_frame ,image = logout,cursor = 'hand2', fg = "#33414f", font = "georgia 10 bold", bg = "#33414f" , borderwidth = 0 , relief = "flat")
        log_label.place(x=75,y=550)
        logout_button = Button(log_label,text = "LOGOUT", fg = "#33414f", font = "georgia 10 bold", bg = "#1daf9b"
                        ,relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1daf9b",
                        highlightcolor = "#1daf9b" , command = over)
        logout_button.place(x=10,y=5)
    def mgr_login(self):
        # -------------------------------------------EMPLOYEE LOGIN PAGE----------------------------------------------------------------------
        self.var.get()
        window1.title("EMPLOYEE LOGIN PAGE")

        window_frame3 = Frame(window1, bg = "#efefef")
        window_frame3.place(x = 0, y = 0, height = 1350, width = 1350)

        background_label = Label(window_frame3, text = "@2020 by CET,SCET,MITWPU,All rights reserved.", font = "times",
                                 fg = "#33414f", bg = "#1daf9b")
        background_label.place(x = 0, y = 680, height = 30, width = 1350)

        background_label2 = Label(window_frame3, bg = "#1daf9b")
        background_label2.place(x = 0, y = 0, width = 1350, height = 330)

        label_1 = Label(window_frame3, bg = "white", borderwidth = 3, relief = "raised")
        label_1.place(x = 450, y = 100, height = 500, width = 400)

        logo = Label(label_1, image = logo2, borderwidth = 0, bg = "white")
        logo.place(x = 100, y = 0)

        display_l = Label(label_1, fg = "#33414f", bg = "white", borderwidth = 1)
        display_l.place(x = 1, y = 180, height = 200, width = 350)

        main = Label(display_l, text = "LOGIN", bg = "white", fg = "#33414f", font = "georgia 20 bold")
        main.place(x = 140, y = 0)
        emp_id = Label(display_l, text = "  EMPLOYEE ID ", bg = "white", fg = "grey", font = "georgia 12 ")
        emp_id.place(x = 10, y = 40)
        phone = Label(display_l, text = "  PHONE NUMBER ", bg = "white", fg = "grey", font = "georgia 12 ")
        phone.place(x = 10, y = 100)

        emp_id = IntVar()
        empid_enter = Entry(display_l, font = "georgia 12", relief = "groove",
                            borderwidth = 0.6, bg = "white" , textvariable = emp_id)
        empid_enter.place(x = 20, y = 60, width = 400, height = 30)

        phone_no = StringVar()
        empphone_enter = Entry(display_l, font = "georgia 12", relief = "groove",
                               borderwidth = 0.6, bg = "white" , textvariable = phone_no)
        empphone_enter.place(x = 20, y = 120, width = 400, height = 30)
        def check1():
            self.id = emp_id.get()
            self.hid = checkemployee(self.id)
            if self.hid == 0:
                messagebox.showinfo("ERROR FOUND ", "INCORRECT ID OR PASSWORD , TRY AGAIN")
            elif self.hid == -1:
                messagebox.showinfo("ERROR FOUND ", "NOT REGISTERED ID , REGISTER FIRST !")   
            else:
                messagebox.showinfo("REGISTRATION ", "OK CORRECT , PRESS OK !" ) 
                self.generate_otp_1()        


        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 152, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",cursor = "hand2",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = check1)
        submit.place(x = 14, y = 8)

#-----------------------------------------MAIN PAGE----------------------------------------------------------

class Login(Student, Manager):

    def action(self):
        # ---------------------------------------------LOGIN PAGE---------------------------------------------------------------------------------
        window1.title("LOGIN PAGE")

        window_frame1 = Frame(window1, bg = "#efefef")
        window_frame1.place(x = 0, y = 0, height = 1350, width = 1350)

        background_label2 = Label(window_frame1, bg = "#1daf9b")
        background_label2.place(x = 0, y = 0, height = 330, width = 1350)

        label_1 = Label(window_frame1, bg = "white", borderwidth = 3, relief = "raised")
        label_1.place(x = 450, y = 100, height = 500, width = 400)

        logo = Label(label_1, image = logo2, borderwidth = 0, bg = "white")
        logo.place(x = 100, y = 0)
        display_l = Label(label_1, fg = "#33414f", font = "times 20 bold ", bg = "white", borderwidth = 1)
        display_l.place(x = 1, y = 228, height = 200, width = 350)
        msg1 = Label(display_l, text = "SELECT LOGIN TYPE", fg = "#33414f", font = "georgia 20 bold", bg = "white")
        msg1.place(x = 45, y = 0)

        # FOR ACCEPTING TYPE OF USER
        student = Radiobutton(display_l, text = "STUDENT", variable = self.var, value = 1, bg = "white",
                              font = "georgia 15", fg = "#33414f", activebackground = "white",
                              activeforeground = "#33414f", highlightcolor = "#efefef", command = self.stud_login)
        student.place(x = 125, y = 30)
        employee = Radiobutton(display_l, text = "EMPLOYEE", variable = self.var, value = 2, bg = "white",
                               font = "georgia 15", fg = "#33414f", activebackground = "white",
                               activeforeground = "#33414f", highlightcolor = "#efefef", command = self.mgr_login)
        employee.place(x = 125, y = 60)
        background_label = Label(window_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                                 font = "times", fg = "#33414f", bg = "#1daf9b" , anchor = "n")
        background_label.place(x = 0, y = 680, height = 100, width = 1350)


# FOR INSERTING LOGO IMAGE :-
def action():
    window_frame.destroy()
    l = Login()
    l.action()


background = Button(window_frame, image = mainlogo, borderwidth = 0, bg = "#efefef", command = action,cursor = "hand2",
                    activebackground = "#efefef", activeforeground = "#efefef", highlightcolor = "#efefef")
background.place(x = 380, y = 80)

background_label = Label(window_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b",anchor = "n")
background_label.place(x = 0, y = 680, height = 100, width = 1350)
background_label2 = Label(window_frame, bg = "#1daf9b")
background_label2.place(x = 0, y = 0, width = 1350)

window1.mainloop()