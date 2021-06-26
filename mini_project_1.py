
import random
import os
import requests
import math
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
#--------------------------------------------------MAIN LOGO PAGE---------------------------------------------------------------------------
window1  = tk.Tk()
window1.iconbitmap(r"icon.ico")
window1.title('HOSTEL MANAGEMENT SYSTEM : ')
window1.geometry("1350x1350+0+0")
window1.config(bg = "#efefef")
window_frame = Frame(window1 , bg = "#efefef")
window_frame.place(x = 0 , y = 0,height = 1350 , width = 1350)
filename = ImageTk.PhotoImage(Image.open(r"logo.jpeg").resize((600,600)))
#--------------------------------------------------------------------------------------------------------------------------------------------


def action() :  
    #---------------------------------------------LOGIN PAGE---------------------------------------------------------------------------------
    window1.title("LOGIN PAGE")
    window_frame.destroy()

    window_frame1 = Frame(window1 , bg = "#efefef")
    window_frame1.place(x=0,y=0,height = 1350 , width = 1350)

    background_label2 = Label(window_frame1, bg = "#1daf9b")
    background_label2.place(x=0 , y= 0 ,height = 330, width = 1350)


    label_1 = Label(window_frame1 , bg = "white" , borderwidth = 3 , relief = "raised" )
    label_1.place(x=450,y=100, height = 500 , width = 400)

    l = ImageTk.PhotoImage(Image.open(r"logo2.jpeg").resize((200,200)))
    logo = Label(label_1, image = l ,borderwidth = 0 , bg = "white")
    logo.place(x=100, y =0)
    display_l =Label(label_1,fg = "#33414f",font = "times 20 bold ",bg = "white" ,borderwidth = 1)
    display_l.place(x=1 ,y =228 , height = 200 , width = 350)
    msg1 =Label(display_l,text="SELECT LOGIN TYPE",fg = "#33414f",font ="georgia 20 bold",bg = "white")
    msg1.place(x=45,y=0)

    var = IntVar()
    
    def stud_login():
        #--------------------------------------------STUDENT LOGIN PAGE----------------------------------------------------------------------
        var.get()
        window1.title("STUDENT LOGIN PAGE : ")

        window_frame2 = Frame(window1 , bg = "#efefef")
        window_frame2.place(x=0,y=0,height = 1350 , width = 1350)

        background_label = Label(window_frame2, text = "@2020 by CET,SCET,MITWPU,All rights reserved." , font = "times" , fg = "#33414f" , bg = "#1daf9b")
        background_label.place(x=0 , y= 680 , height = 30,width = 1350)

        background_label2 = Label(window_frame2, bg = "#1daf9b")
        background_label2.place(x=0 , y= 0 , width = 1350, height = 330)

        label_1 = Label(window_frame2, bg = "white" , borderwidth = 3 , relief = "raised" )
        label_1.place(x=450,y=100, height = 500 , width = 400)

        logo = Label(label_1, image = l ,borderwidth = 0 , bg = "white")
        logo.place(x=100, y =0)
        display_l =Label(label_1,fg = "#33414f",bg = "white" ,borderwidth = 1)
        display_l.place(x=1 ,y =228 , height = 200 , width = 350)
        
        main = Label(display_l,text = "FILL LOGIN DETAILS ",bg = "white",fg = "#33414f",font = "georgia 20 bold")
        main.place(x=35,y=0)
        std_id = Label(display_l,text="  STUDENT ID ", bg="white",fg = "grey",font = "georgia 12 " )
        std_id.place(x=10,y=40)
        phone = Label(display_l,text="  PHONE NUMBER ",bg="white",fg = "grey",font = "georgia 12 " )
        phone.place(x=10,y=100)

        stud_id = StringVar()
        phone_no = IntVar()
        stdid_enter = Entry(display_l, textvariable = stud_id ,font = "georgia 12", relief = "groove" , borderwidth = 0.6 , bg = "white")
        stdid_enter.place(x=20,y=60,width = 400 , height = 30)

        stdphone_enter = Entry(display_l , textvariable = phone_no ,font = "georgia 12", relief = "groove" , borderwidth = 0.6 , bg = "white")
        stdphone_enter.place(x=20,y=120,width = 400 , height = 30)
        def generate_otp(): 
            otp_no = StringVar()
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
                        "sender_id":"HOSTELMS","message":notif,"language":"english","route":"p","numbers":"8454907639"}

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
                    error.grid(row = 6,column = 1)''''''

            submit2 = ttk.Button(label_p,text = "SUBMIT",style = "new.TButton")#,command = register_page)
            submit2.place(x=160,y=300)'''

            label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
            label.place(x=130,y=100)

            submit = Button(label,text = "SUBMIT",fg = "#33414f" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = generate_otp)
            submit.place(x=18,y=6)

        la = ImageTk.PhotoImage(Image.open(r"label.png").resize((120,45)))
        label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
        label.place(x=140,y=160)

        submit = Button(label,text = "SUBMIT",fg = "#33414f" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = generate_otp)
        submit.place(x=18,y=6)


    def emp_login():
        #-------------------------------------------EMPLOYEE LOGIN PAGE----------------------------------------------------------------------
        var.get()
        window1.title("EMPLOYEE LOGIN PAGE : ")

        window_frame3 = Frame(window1 , bg = "#efefef")
        window_frame3.place(x=0,y=0,height = 1350 , width = 1350)

        background_label = Label(window_frame3, text = "@2020 by CET,SCET,MITWPU,All rights reserved." , font = "times" , fg = "#33414f" , bg = "#1daf9b")
        background_label.place(x=0 , y= 680 , height = 30,width = 1350)

        background_label2 = Label(window_frame3, bg = "#1daf9b")
        background_label2.place(x=0 , y= 0 , width = 1350, height = 330)

        label_1 = Label(window_frame3, bg = "white" , borderwidth = 3 , relief = "raised" )
        label_1.place(x=450,y=100, height = 500 , width = 400)

        logo = Label(label_1, image = l ,borderwidth = 0 , bg = "white")
        logo.place(x=100, y =0)
        display_l =Label(label_1,fg = "#33414f",bg = "white" ,borderwidth = 1)
        display_l.place(x=1 ,y =228 , height = 200 , width = 350)
        
        main = Label(display_l,text = "FILL LOGIN DETAILS ",bg = "white",fg = "#33414f",font = "georgia 20 bold")
        main.place(x=35,y=0)
        std_id = Label(display_l,text="  EMPLOYEE ID ", bg="white",fg = "grey",font = "georgia 12 " )
        std_id.place(x=10,y=40)
        phone = Label(display_l,text="  PHONE NUMBER ",bg="white",fg = "grey",font = "georgia 12 " )
        phone.place(x=10,y=100)

        stud_id = StringVar()
        phone_no = IntVar()
        stdid_enter = Entry(display_l, textvariable = stud_id ,font = "georgia 12", relief = "groove" , borderwidth = 0.6 , bg = "white")
        stdid_enter.place(x=20,y=60,width = 400 , height = 30)

        stdphone_enter = Entry(display_l , textvariable = phone_no ,font = "georgia 12", relief = "groove" , borderwidth = 0.6 , bg = "white")
        stdphone_enter.place(x=20,y=120,width = 400 , height = 30)
        def generate_otp(): 
            otp_no = StringVar()
            labelbox = Label(display_l, borderwidth = 0, bg = "white")
            labelbox.place(x=10,y=0 , height = 200 ,width = 400)

            label_otp = Label(labelbox, text = "ENTER VALID OTP ",font = "georgia 12", borderwidth = 0, bg = "white",fg ="grey")
            label_otp.place(x=10,y=10)
            enter_otp = Entry(labelbox , textvariable = otp_no,font = "georgia 12", borderwidth = 0.6 , bg = "white" , relief = "groove")
            enter_otp.place(x=10,y=30,height = 30 , width = 400)

            '''smp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            OTP = ""
            length = len(smp)
            for i in range(6):
                OTP += smp[math.floor(random.random() * length)]

            notif = ("Your OTP is: " + str(OTP))
            url = "https://www.fast2sms.com/dev/bulk"

            querystring = {"authorization":"vTaWBKucoELspqAHSl9t2NCm1w05xdMYfGbeiUJngIQVz4DR3XsUBDu2P6loCar5IfRxvWdNLgkqQFH9",
                        "sender_id":"HOSTELMS","message":notif,"language":"english","route":"p","numbers":"8454907639"}

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
                    error.grid(row = 6,column = 1)''''''

            submit2 = ttk.Button(label_p,text = "SUBMIT",style = "new.TButton")#,command = register_page)
            submit2.place(x=160,y=300)'''

            label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
            label.place(x=130,y=100)

            submit = Button(label,text = "SUBMIT",fg = "#efefef" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = generate_otp)
            submit.place(x=18,y=6)

        la = ImageTk.PhotoImage(Image.open(r"label.png").resize((120,45)))
        label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
        label.place(x=140,y=160)

        submit = Button(label,text = "SUBMIT",fg = "#efefef" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = generate_otp)
        submit.place(x=18,y=6)

    
    #FOR ACCEPTING TYPE OF USER 
    student = Radiobutton(display_l,text="STUDENT",variable = var , value = 1,bg="white",font = "georgia 15" ,fg = "#33414f" ,activebackground ="white" , activeforeground = "#33414f" , highlightcolor = "#efefef" ,command = stud_login)
    student.place(x= 125 ,y = 30)
    employee = Radiobutton(display_l,text="EMPLOYEE",variable = var,value = 2,bg="white",font = "georgia 15" , fg = "#33414f" ,activebackground ="white" , activeforeground = "#33414f" , highlightcolor = "#efefef",command = emp_login)
    employee.place(x=125,y = 60 )
    background_label = Label(window_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved." , font = "times" , fg = "#33414f" , bg = "#1daf9b")
    background_label.place(x=0 , y= 680 ,height = 30, width = 1350)

#FOR INSERTING LOGO IMAGE :-
background = Button(window_frame, image=filename ,borderwidth = 0,command = action, bg = "#efefef" , activebackground ="#efefef" , activeforeground = "#efefef" , highlightcolor = "#efefef")
background.place(x= 380 , y= 80)

background_label = Label(window_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved." , font = "times" , fg = "#33414f" , bg = "#1daf9b")
background_label.place(x=0 , y= 680 , height = 30 , width = 1350)

background_label2 = Label(window_frame, bg = "#1daf9b")
background_label2.place(x=0 , y= 0 , width = 1350)

window1.mainloop()
