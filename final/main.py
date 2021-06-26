#------------------------------------------------------------------------------------------------------------
import tkinter as tk
from allsql import * 
import mysql.connector
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
#------------------------------------------------------------------------------------------------------------
window1 = tk.Tk()
window1.iconbitmap(r"icon.ico")
window1.title('HOSTEL MANAGEMENT SYSTEM')
mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "28868755", database = "hostelmanagementsystem")
ptr = mydb.cursor()

window1.geometry("1350x720+0+0")
window1.config(bg = "#efefef")
window_frame = Frame(window1, bg = "#efefef")
window_frame.place(x = 0, y = 0, height = 1350, width = 1350)
window1.resizable(False, False)
global file 
file = ""
# ----------------------------------------------------------------------#
# FIRST WINDOW FOR STUDENT DETAILS#
# ----------------------------------------------------IMAGE CREATIONS------------------------------------------------------------------------
global mainlogo
mainlogo = ImageTk.PhotoImage(Image.open(r"logo.jpeg").resize((600, 600)))
global edit
edit = ImageTk.PhotoImage(Image.open(r"edit.jpeg").resize((25, 25)))
global edit2
edit2 = ImageTk.PhotoImage(Image.open(r"edit2.jpg").resize((25, 25)))
global logo
logo2 = ImageTk.PhotoImage(Image.open(r"logo2.jpeg").resize((200, 200)))
'''
*************************************************************************************************************
MINI PROJECT - HOSTEL MANAGEMENT SYSTEM 
ROLL NO - 18,23,62,63
*************************************************************************************************************
'''
class RegisterStudent:
    st_id = 0
    fname = ""
    lname = ""
    sphoneno = []
    state = ""
    city = ""
    street = ""
    face = ""
    idproof = ""
    gender = ""
    gname = ""

    def __init__(self):
        # -------------------------------------REGISTRATION PAGE-----------------------------------------------
            self.win = tk.Tk()
            self.win.title('REGISTRATION')
            self.win.geometry("1350x720+0+0")
            self.win.resizable(False, False)
            self.win.iconbitmap(r"icon.ico")                    
            self.tabControl = ttk.Notebook(self.win)  
            s = ttk.Style()
            s.configure('TFrame')
            s.configure('stu_frame.TFrame' ,bg = "#efefef",font = "georgia 15 " , fg = "#33414f" )
            s.configure('g_frame.TFrame',  bg = "#efefef", font = "georgia 15 " , fg = "#33414f")  
            self.stu_frame = ttk.Frame(self.tabControl)
            self.g_frame = ttk.Frame(self.tabControl)
            self.tabControl.add(self.stu_frame, text = 'STUDENT')
            self.tabControl.add(self.g_frame, text = 'GUARDIAN')
            self.tabControl.pack(expand = 1, fill = "both")
            self.background_label2 = Label(self.stu_frame, bg = "#1daf9b")
            self.background_label2.place(x = 0, y = 0, height = 330, width = 1350)
            self.background_label21 = Label(self.g_frame, bg = "#1daf9b")
            self.background_label21.place(x = 0, y = 0, height = 330, width = 1350)
            self.bottom_label = Label(self.win, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b", anchor = "n")
            self.bottom_label.place(x = 0, y = 680, height = 100, width = 1350)

            self.label_1 = Label(self.stu_frame, bg = "white", borderwidth = 3, relief = "raised")
            self.label_1.place(x = 450, y = 100, height = 500, width = 400) 
            self.label_2 = Label(self.g_frame, bg = "white", borderwidth = 3, relief = "raised")
            self.label_2.place(x = 450, y = 100, height = 500, width = 400)   
            self.guardian()
            self.student()
            self.win.mainloop()

    def guardian(self):
        # ----------------------------------------------------------------------#
        # LABELS FOR GUARDIAN DETAILS#

        guardian_label = Label(self.g_frame, text = "GUARDIAN DETAIL", background = "white", foreground = "#33414f",
                               font = "georgia 20 bold ", anchor = 's')
        guardian_label.place(x = 490, y = 130)

        guardianname_label = Label(self.g_frame, text = "Enter Name", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianname_label.place(x = 460, y = 220)

        guardianphone_label = Label(self.g_frame, text = "Enter Phone", background = "white", foreground = "#33414f",
                                    font = "georgia 12", anchor = 's')
        guardianphone_label.place(x = 460, y = 260)

        guardianalt_label = Label(self.g_frame, text = "Enter Alt Phone", background = "white", foreground = "#33414f",
                                  font = "georgia 12", anchor = 's')
        guardianalt_label.place(x = 460, y = 300)

        guardianrole_label = Label(self.g_frame, text = "Enter Role", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianrole_label.place(x = 460, y = 340)

        guardianaddr_label = Label(self.g_frame, text = "Enter Address", background = "white", foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        guardianaddr_label.place(x = 460, y = 380)

        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR GUARDIAN DETAILS#
        gname_var = StringVar()
        gname_entrybox = Entry(self.g_frame, width = 13, textvariable = gname_var , font = "georgia 12")
        gname_entrybox.place(x = 650, y = 227)

        gphone_var = IntVar()
        gphone_entrybox = Entry(self.g_frame, width = 13, textvariable = gphone_var , font = "georgia 12 ")
        gphone_entrybox.place(x = 650, y = 267)

        galt_var = IntVar()
        galt_entrybox = Entry(self.g_frame, width = 13, textvariable = galt_var , font = "georgia 12 ")
        galt_entrybox.place(x = 650, y = 307)

        grole_var = StringVar()
        grole_combobox = ttk.Combobox(self.g_frame, width = 16, textvariable = grole_var, state = 'readonly')
        grole_combobox['values'] = ('GUARDIAN', 'FATHER', 'MOTHER')
        grole_combobox.place(x = 650, y = 347)

        gaddr_var = StringVar()
        gaddr_entrybox = Entry(self.g_frame, width = 13, textvariable = gaddr_var , font = "georgia 12")
        gaddr_entrybox.place(x = 650, y = 387)
        label = Label(self.g_frame, borderwidth = 0, bg = "white")
        label.place(x=560 , y= 510)
        button = Button(label, text = "SAVE & NEXT", borderwidth = "0", fg = "#33414f" , font = " gerogia 11 bold"
                        , bg = "#1daf9b" ,activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9",command = self.win.destroy)
        button.place(x = 18, y = 5)

    # ======================================================================#
    # END MAINLOOP FOR SECOND WINDOW#

    def student(self):
        # stu_frame=Frame(win)
        # stu_frame.place(x=0,y=0,height = 1350 , width = 1350)
        tablename_label = ttk.Label(self.stu_frame, text = "STUDENT DETAILS", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 22 bold ")
        tablename_label.place(x = 490, y = 130)

        studentid_label = ttk.Label(self.stu_frame, text = "Enter student id", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 12")
        studentid_label.place(x = 470, y = 190)

        firstname_label = ttk.Label(self.stu_frame, text = "Enter first name", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 12")
        firstname_label.place(x = 470, y = 220)

        lastname_label = ttk.Label(self.stu_frame, text = "Enter last name", background = "white",
                                   foreground = "#33414f",
                                   font = "georgia 12", anchor = 's')
        lastname_label.place(x = 470, y = 250)

        state_label = ttk.Label(self.stu_frame, text = "Enter state", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        state_label.place(x = 470, y = 280)

        city_label = ttk.Label(self.stu_frame, text = "Enter city", background = "white", foreground = "#33414f",
                               font = "georgia 12", anchor = 's')
        city_label.place(x = 470, y = 310)

        street_label = ttk.Label(self.stu_frame, text = "Enter street", background = "white", foreground = "#33414f",
                                 font = "georgia 12", anchor = 's')
        street_label.place(x = 470, y = 340)

        face_label = ttk.Label(self.stu_frame, text = "Upload face photo", background = "white", foreground = "#33414f",
                               font = "georgia 12", anchor = 's')
        face_label.place(x = 470, y = 370)

        idproof_label = ttk.Label(self.stu_frame, text = "Upload id proof", background = "white",
                                  foreground = "#33414f",
                                  font = "georgia 12", anchor = 's')
        idproof_label.place(x = 470, y = 400)

        gender_label = ttk.Label(self.stu_frame, text = "Select your gender", background = "white",
                                 foreground = "#33414f",
                                 font = "georgia 12", anchor = 's')
        gender_label.place(x = 470, y = 430)

        phone_label = ttk.Label(self.stu_frame, text = "Enter Phone no", background = "white", foreground = "#33414f",
                                font = "georgia 12", anchor = 's')
        phone_label.place(x = 470, y = 462)
        alt_label = ttk.Label(self.stu_frame, text = "Enter Alt Phone no", background = "white", foreground = "#33414f",
                              font = "georgia 12", anchor = 's')
        alt_label.place(x = 470, y = 490)

        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR STUDENT DETAILS#

        stid_var = IntVar()
        stid_entrybox = Entry(self.stu_frame, width = 13, textvariable = stid_var , font = "georgia 12"
                                , borderwidth = 0.6 , relief = "groove")
        stid_entrybox.place(x = 650, y = 187 , width = 150)
        stid_entrybox.focus()

        firstname_var = StringVar()
        firstname_entrybox = Entry(self.stu_frame, width = 13, borderwidth = 0.6 , font = "georgia 12 "
                            , relief = "groove", textvariable = firstname_var)
        firstname_entrybox.place(x = 650, y = 217 , width = 150)

        lastname_var = StringVar()
        lastname_entrybox = Entry(self.stu_frame, width = 13, borderwidth = 0.6 , font = "georgia 12"
                            ,relief = "groove", textvariable = lastname_var)
        lastname_entrybox.place(x = 650 , y = 247 , width = 150 )

        state_var = StringVar()
        state_entrybox = Entry(self.stu_frame, width = 13, borderwidth = 0.6 , font = "georgia 12"
                            ,relief = "groove", textvariable = state_var)
        state_entrybox.place(x = 650 , y = 277 , width = 150 )

        city_var = StringVar()
        city_entrybox = Entry(self.stu_frame, width = 13,  borderwidth = 0.6 , font = "georgia 12 "
                            ,relief = "groove",textvariable = city_var)
        city_entrybox.place(x = 650, y = 307 , width = 150 )

        street_var = StringVar()
        street_entrybox = Entry(self.stu_frame, width = 13, borderwidth = 0.6 , font = "georgia 12 ", textvariable = street_var)
        street_entrybox.place(x = 650 , y = 337 , width = 150)

        # ----------------------------------------------------------------------#
        # BUTTONS FOR STUDENT DETAILS#

        def filed():
            self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select Image",
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            file = self.filename

        uploadface_button = Button(self.stu_frame, text = 'upload', command = lambda: filed())
        uploadface_button.place(x = 650, y = 367 , width = 150)

        uploadproof_button = Button(self.stu_frame, text = 'upload', command = lambda: filed())
        uploadproof_button.place(x = 650, y = 397 , width = 150)

        # ----------------------------------------------------------------------#
        # COMBO BOX FOR STUDENT DETAILS AND DESTROY THE WINDOW 1#

        gender_var = StringVar()
        gender_combobox = ttk.Combobox(self.stu_frame, width = 14, textvariable = gender_var, state = 'readonly')
        gender_combobox['values'] = ('MALE', 'FEMALE')
        gender_combobox.place(x = 650, y = 427 , width = 150 )

        phone_var = IntVar()
        phone_entrybox = Entry(self.stu_frame, width = 13, font = "georgia 12",textvariable = phone_var ,
                              borderwidth = 0.6 , relief = "groove")
        phone_entrybox.place(x = 650, y = 457 , width = 150)

        alt_var = IntVar()
        alt_entrybox = Entry(self.stu_frame, width = 13,font = "georgia 12 ",  textvariable = phone_var 
                            ,  borderwidth = 0.6 , relief = "groove")
        alt_entrybox.place(x = 650 , y = 487 , width = 150 )

        def save():
            st_id = stid_entrybox.get()
            fname = firstname_entrybox.get()
            lname = lastname_entrybox.get()
            state = state_entrybox.get()
            city = city_entrybox.get()
            street = street_entrybox.get()
            gender = gender_combobox.get()
            self.guardian()
        label = Label(self.stu_frame, borderwidth = 0, bg = "white")
        label.place(x=500 , y= 510)
        button = Button(label, text = "SAVE & NEXT", borderwidth = "0", fg = "#33414f" , font = " gerogia 11 bold"
                        , bg = "#1daf9b" ,activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9",command = self.stu_frame.destroy)
        button.place(x = 18, y = 5)

#------------------------------------------END OF REGISTRATION-----------------------------------------------
#------------------------------------------STUDENT PAGE------------------------------------------------------

class Student():
    la1 = ImageTk.PhotoImage(Image.open(r"label.png").resize((100, 40)))
    submit_logo = ImageTk.PhotoImage(Image.open(r"label.png").resize((100, 35)))
    add = ImageTk.PhotoImage(Image.open(r'add.jpeg').resize((35,40)))
    grd = ImageTk.PhotoImage(Image.open(r'grad.png').resize((1350,1350)))
    stu_id = 0
    stu_phone = ""

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
        pay_frame = Frame(window1, bg = "white" , borderwidth = 0.6 , relief = "raised")
        pay_frame.place(x = 780, y = 60, height = 300, width = 300)
        pay_detail = Label(pay_frame, text = "Guardian Details  "
                           ,font = "georgia 18 bold", fg = "#33414f", bg = "white")
        pay_detail.place(x = 0, y = 0)

        c_frame = Frame(stu_frame1 , bg = "white" , borderwidth = 0.6 , relief = "raised")
        c_frame.place(x=350,y=400 , height = 200 , width = 732)

        student = student_info(self.stu_id)
        for i in student : 
            sidl = Label(vertical_frame, text = "ID :                      {}\n".format(i[0]), fg = "#efefef", bg = "#33414f",
                     font = "Georgia 12")
            sidl.place(x = 0, y = 200)
            snamel = Label(vertical_frame, text = "Name :                {}\n".format(i[1] + " " + i[2]), fg = "#efefef", bg = "#33414f",
                       font = "Georgia 12")
            snamel.place(x = 0, y = 230)
            sphone = Label(s_frame, text = "Phone number :           {}\n".format(self.stu_phone), fg = "#33414f", bg = "white", 
                       font = "Georgia 12")
            sphone.place(x = 0, y = 60)   
            saddr = Label(s_frame, text = "Student Address :        {} , {} \n \t\t {} ,\n\t\t {} , {}".format(i[4],i[5],i[6],i[7],i[8]),
                         bg = "white", fg = "#33414f", font = "Georgia 12" , anchor = "nw")
            saddr.place(x = 0, y = 90)
            sgen = Label(vertical_frame, text = "Gender :               {}\n".format(i[3]), fg = "#efefef", bg = "#33414f",
                       font = "Georgia 12")
            sgen.place(x = 0, y = 260)
        
        hostel = hostel_info(self.stu_id)
        for j in hostel :
            hostel_detail = Label(vertical_frame, text = "Hostel :               {}\n".format(j[0]),fg = "#efefef", bg = "#33414f",
                           font = "Georgia 12")
            hostel_detail.place(x = 0, y = 290)
            hostel_detail = Label(vertical_frame, text = "Room :               {}\n".format(j[1]),fg = "#efefef", bg = "#33414f",
                           font = "Georgia 12")
            hostel_detail.place(x = 0, y = 320)
        guardian = guradian_info(self.stu_id)
        for j in guardian:
            g_detail = Label(pay_frame, text = "Guardian Name :         {} \n".format(j[2]) ,
                         font = "georgia 12", fg = "#33414f", bg = "white")
            g_detail.place(x = 0, y = 60)
            g_detail = Label(pay_frame, text = "Guardian Role :           {}\n".format(j[3]),
                         font = "georgia 12", fg = "#33414f", bg = "white")
            g_detail.place(x = 0, y = 90)
            g_detail = Label(pay_frame, text = "Guardian Address :     {}\n".format(j[4]),
                         font = "georgia 12", fg = "#33414f", bg = "white")
            g_detail.place(x = 0, y = 120)
        phone = guradian_phone(self.stu_id)
        for k in phone :
            g_detail = Label(pay_frame, text = "Guardian Phone :           {}\n".format(k[2]),
                         font = "georgia 12", fg = "#33414f", bg = "white")
            g_detail.place(x = 0, y = 150)
        def edit_student_info():

            sphone_var = IntVar()
            sphone_entrybox = Entry(s_frame, textvariable = sphone_var , font = "georgia 12 " ,bg = "#EFEFEF")
            sphone_entrybox.place(x = 130 , y = 60 , width = 150)

            sadd_var = StringVar()
            sadd_entrybox = Entry(s_frame, textvariable = sadd_var , font = "georgia 12 ", bg = "#efefef")
            sadd_entrybox.place(x=130 , y = 95 , width = 150 , height = 50)

            label = Label(s_frame, image = self.submit_logo, borderwidth = 0, bg = "white")
            label.place(x = 100, y = 200)
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
        edit_info.place(x = 270, y = 0)

        def edit_guard():
            gname_var = StringVar()
            gname_entrybox = Entry(pay_frame, textvariable = gname_var , font = "georgia 12" ,bg = "#efefef")
            gname_entrybox.place(x = 150 , y = 60 , width = 130 )

            gphone_var = IntVar()
            gphone_entrybox = Entry(pay_frame, textvariable = gphone_var , font = "georgia 12 ", bg = "#efefef")
            gphone_entrybox.place(x = 150 , y = 90 , width = 130 )

            grole_var = StringVar()
            grole_entrybox = Entry(pay_frame, textvariable = grole_var, font = "georgia 12 ", bg = "#efefef")
            grole_entrybox.place(x = 150 , y = 120 , width = 130 )

            phone_var = StringVar()
            sgphone_entrybox = Entry(pay_frame , textvariable = phone_var , font = "georgia 12 ", bg = "#efefef")
            sgphone_entrybox.place(x=150 , y = 150 , width = 130)      

            label = Label(pay_frame, image = self.submit_logo, borderwidth = 0, bg = "white")
            label.place(x = 100, y = 200)
            def callsubmit():
                messagebox.showinfo("UPDATE REQUEST ", "Request for updation is sent to the administration")    
                gname_entrybox.destroy()
                gphone_entrybox.destroy()
                sgphone_entrybox.destroy()
                grole_entrybox.destroy()
                submit.destroy()  
                label.destroy()
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9" , command = callsubmit)            
            submit.place(x = 12, y = 5)


        edit_pay = Button(pay_frame, image = edit, fg = "#F6F6F6", borderwidth = 0 , command = edit_guard)
        edit_pay.place(x = 270, y = 0)

        add_complaint = Label(c_frame , text = "Complaint box" 
                         ,font = "georgia 18 bold", fg = "#33414f", bg = "white" )
        add_complaint.place(x=0,y=0)

        def add_compt() : 
            add_entrybox = Entry(c_frame ,font = "georgia 12 " ,bg = "#efefef")
            add_entrybox.place(x=30 , y = 60 , height = 80 , width = 600)

            label = Label(c_frame, image = self.submit_logo, borderwidth = 0, bg = "white")
            label.place(x = 310, y = 150)
            def callsubmit():
                messagebox.showinfo("UPDATE REQUEST ", "Request for updation is sent to the administration")    
                add_entrybox.destroy()
                label.destroy()
                submit.destroy()  
            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9" , command = callsubmit)
            submit.place(x = 12, y = 5)
        
        edit_complaint = Button(c_frame , image = self.add , fg = "#f6f6f6" , borderwidth = 0 , command = add_compt)
        edit_complaint.place(x= 690 , y=0)

        def over():
            window1.destroy()

        global logout 
        logout = ImageTk.PhotoImage(Image.open(r"label2.png").resize((100,40)))
        log_label = Label(vertical_frame ,image = logout, fg = "#33414f", font = "georgia 10 bold", bg = "#33414f" , borderwidth = 0 , relief = "flat")
        log_label.place(x=75,y=550)
        logout_button = Button(log_label,text = "LOGOUT", fg = "#33414f", font = "georgia 10 bold", bg = "#1daf9b"
                        ,relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1daf9b",
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
            #
            #     '''smp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            #     OTP = ""
            #     length = len(smp)
            #     for i in range(6):
            #         OTP += smp[math.floor(random.random() * length)]
            #
            #     notif = ("Your OTP is: " + str(OTP))
            #     url = "https://www.fast2sms.com/dev/bulk"
            #
            #     querystring = {"authorization":"vTaWBKucoELspqAHSl9t2NCm1w05xdMYfGbeiUJngIQVz4DR3XsUBDu2P6loCar5IfRxvWdNLgkqQFH9",
            #                 "sender_id":"HOSTELMS","message":notif,"language":"english","route":"p","numbers":"8454907639"}
            #
            #     headers = {
            #         'cache-control': "no-cache"
            #     }
            #
            #     response = requests.request("GET", url, headers=headers, params=querystring)
            #
            #     def register_page():
            #         Entry = otp_no.get()
            #         if Entry == OTP:
            #             stud_window.destroy()
            #
            #         else:
            #             error = Label(frame1, text = "TRY AGAIN , OTP WRONG !",bg="#8c54a1",fg = "white",font = "times 20 ")
            #             error.grid(row = 6,column = 1)''''''
            #
            #     submit2 = ttk.Button(label_p,text = "SUBMIT",style = "new.TButton")#,command = register_page)
            #     submit2.place(x=160,y=300)'''
            #
            #     label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
            #     label.place(x=130,y=100)
            #
            #     submit = Button(label,text = "SUBMIT",fg = "#33414f" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = generate_otp)
            #     submit.place(x=18,y=6)
    
            label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
            label.place(x = 152, y = 410)

            submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = self.stu_page)
            submit.place(x = 14, y = 8)

    def stud_login(self):
        # --------------------------------------------STUDENT LOGIN PAGE----------------------------------------------------------------------
        self.var.get()
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
        stdid_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white",textvariable = id)
        stdid_enter.place(x = 20, y = 60, width = 400, height = 30)

        phoneno = StringVar()

        stdphone_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white",textvariable = phoneno)
        stdphone_enter.place(x = 20, y = 120, width = 400, height = 30)

        def check():
            self.stu_id = id.get()
            self.stu_phone = phoneno.get()
            result = checkstudent(self.stu_id,self.stu_phone)
            if result == 0:
                messagebox.showinfo("ERROR FOUND ", "INCORRECT ID OR PASSWORD , TRY AGAIN")
            elif result == 1 :
                messagebox.showinfo("REGISTRATION ", "OK CORRECT , PRESS OK !" ) 
                self.generate_otp()
            elif result == -1:
                messagebox.showinfo("ERROR FOUND ", "NOT REGISTERED ID , REGISTER FIRST !")

        def register():
            r = RegisterStudent()
            # r.student()
            # r.guardian()


        newuser = Button(label_1, text = "New User!Register?", fg = "#33414f", bg = "white",
                         font = "georgia 12 bold underline", relief = "flat", borderwidth = 0,
                         activebackground = "white", activeforeground = "#33414f", highlightcolor = "white",
                         command = register)
        newuser.place(x = 13, y = 335)
        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 152, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 10 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = check)
        submit.place(x = 14, y = 8)

#-----------------------------------------MANAGER PAGE -------------------------------------------------------

class Manager:
    id = 0
    name = ""
    phoneno = 0
    var = IntVar()
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
            if pasw == "Manager@43hsm1":
                messagebox.showinfo("CORRECT ", "OK CORRECT , PRESS OK !")
                self.mgr_page()
            else :
                messagebox.showinfo("ERROR FOUND ", "INCORRECT PASSWORD , TRY AGAIN !")                
    
        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 120, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 12 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = checkpass)
        submit.place(x = 30, y = 5)

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
        '''empidl = Label(vertical_frame, text = "ID:              {}".format(self.id), fg = "#efefef", bg = "#33414f",
                       font = "Georgia")
        empidl.place(x = 0, y = 200);
        empnamel = Label(vertical_frame, text = "Name:        {}".format(self.phoneno), fg = "#efefef", bg = "#33414f",
                         font = "Georgia")
        empnamel.place(x = 0, y = 230);
        # e_frame = Frame(window1, bg = "#F6F6F6")
        # e_frame.place(x = 350, y = 40, height = 100, width = 300)
        e_detail = Label(mgr_frame1, text = "REGISTER EMPLOYEE",
                         font = "times", fg = "#33414f", bg = "#F6F6F6")
        e_detail.place(x = 400, y = 40, width = 300)

        reg_emp = Button(mgr_frame1, image = edit, fg = "#F6F6F6", borderwidth = 0)
        reg_emp.place(x = 672, y = 40)
        stu_reg = Frame(mgr_frame1, bg = "#F6F6F6")
        stu_reg.place(x = 400, y = 120, height = 500, width = 300)
        reg_detail = Label(stu_reg, text = "REGISTRATIONS FOR STUDENT",
                           font = "times", fg = "#33414f", bg = "#F6F6F6")
        reg_detail.place(x = 0, y = 0)
        stu_edit = Button(stu_reg, image = edit , fg = "#f6f6f6" , borderwidth = 0)
        stu_edit.place(x=272, y = 0)
        complaints = Frame(mgr_frame1, bg = "#F6F6F6")
        complaints.place(x = 900, y = 40, height = 580, width = 400)
        comp_label = Label(complaints, text = "                          COMPLAINT BOX",
                           font = "times", fg = "#33414f", bg = "#F6F6F6")
        comp_label.place(x = 0, y = 0)
        def over():
            window1.destroy()

        global logout 
        logout = ImageTk.PhotoImage(Image.open(r"label2.png").resize((150, 60)))
        img = Label(mgr_frame1 , image = logout)
        img.place(x=725,y=600)
        logout_button = Button(img ,text = "LOGOUT" , fg = "#33414f", bg = "#1daf9b", font = "georgia 12 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9" , command = over)
        logout_button.place(x=30,y=15)'''
        def over():
            window1.destroy()
        global logout 
        logout = ImageTk.PhotoImage(Image.open(r"label2.png").resize((150, 45)))
        log_label = Label(vertical_frame ,image = logout, fg = "#33414f", font = "georgia 12 bold", bg = "#33414f" , borderwidth = 0 , relief = "flat")
        log_label.place(x=50,y=550)
        logout_button = Button(log_label,text = "LOGOUT", fg = "#33414f", font = "georgia 12 bold", bg = "#1daf9b"
                        ,relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1daf9b",
                        highlightcolor = "#1daf9b", command = over)
        logout_button.place(x=30,y=5)

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
            id = emp_id.get()
            phoneno = phone_no.get()
            res = checkemployee(id)
            if res == 0:
                messagebox.showinfo("ERROR FOUND ", "INCORRECT ID OR PASSWORD , TRY AGAIN")
            elif res == 1 :
                messagebox.showinfo("REGISTRATION ", "OK CORRECT , PRESS OK !" ) 
                self.generate_otp_1()
            elif res == -1:
                messagebox.showinfo("ERROR FOUND ", "NOT REGISTERED ID , REGISTER FIRST !")           


        label = Label(label_1, image = self.la1, borderwidth = 0, bg = "white")
        label.place(x = 120, y = 410)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 12 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", anchor = "n",command = check1)
        submit.place(x = 30, y = 5)

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


background = Button(window_frame, image = mainlogo, borderwidth = 0, bg = "#efefef", command = action,
                    activebackground = "#efefef", activeforeground = "#efefef", highlightcolor = "#efefef")
background.place(x = 380, y = 80)

background_label = Label(window_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b",anchor = "n")
background_label.place(x = 0, y = 680, height = 100, width = 1350)
background_label2 = Label(window_frame, bg = "#1daf9b")
background_label2.place(x = 0, y = 0, width = 1350)

window1.mainloop()


'''********************************************************************************************************************************************'''