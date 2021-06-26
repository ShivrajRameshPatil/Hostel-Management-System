import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

window1 = tk.Tk()
window1.iconbitmap(r"icon.ico")
window1.title('HOSTEL MANAGEMENT SYSTEM')

window1.geometry("1350x700+0+0")
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
edit = ImageTk.PhotoImage(Image.open(r"edit.jpg").resize((25, 25)))
global logo
logo2 = ImageTk.PhotoImage(Image.open(r"logo2.jpeg").resize((200, 200)))
global p
p = ImageTk.PhotoImage(Image.open(r"image.png").resize((1349, 700)))



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
            self.win = tk.Toplevel(window1)
            self.win.title('REGISTRATION')
            self.win.geometry("1350x1350+0+0")
            self.win.resizable(False, False)

            self.tabControl = ttk.Notebook(self.win)

            self.stu_frame = ttk.Frame(self.tabControl)
            self.g_frame = ttk.Frame(self.tabControl)

            self.label_s = Label(self.stu_frame, image = p, borderwidth = 0)
            self.label_s.place(x = 0, y = 0)
            # self.label_s.image = p
            self.label_g = Label(self.g_frame, image = p, borderwidth = 0)
            # self.label_g.image = p
            self.label_g.place(x = 0, y = 0)
            self.tabControl.add(self.stu_frame, text = 'Student')
            self.tabControl.add(self.g_frame, text = 'Guardian')
            self.tabControl.pack(expand = 1, fill = "both")
            self.guardian()
            self.student()

            self.win.mainloop()

    def guardian(self):
        # ----------------------------------------------------------------------#
        # LABELS FOR GUARDIAN DETAILS#

        guardian_label = Label(self.g_frame, text = "GUARDIAN DETAIL", background = "white", foreground = "#33414f",
                               font = "georgia 20", anchor = 's')
        guardian_label.place(x = 523, y = 130)

        guardianname_label = Label(self.g_frame, text = "Enter Name", background = "white", foreground = "#33414f",
                                   font = "georgia 20", anchor = 's')
        guardianname_label.place(x = 450, y = 220)

        guardianphone_label = Label(self.g_frame, text = "Enter Phone", background = "white", foreground = "#33414f",
                                    font = "georgia 20", anchor = 's')
        guardianphone_label.place(x = 450, y = 260)

        guardianalt_label = Label(self.g_frame, text = "Enter Alt Phone", background = "white", foreground = "#33414f",
                                  font = "georgia 20", anchor = 's')
        guardianalt_label.place(x = 450, y = 300)

        guardianrole_label = Label(self.g_frame, text = "Enter Role", background = "white", foreground = "#33414f",
                                   font = "georgia 20", anchor = 's')
        guardianrole_label.place(x = 450, y = 340)

        guardianaddr_label = Label(self.g_frame, text = "Enter Address", background = "white", foreground = "#33414f",
                                   font = "georgia 20", anchor = 's')
        guardianaddr_label.place(x = 450, y = 380)

        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR GUARDIAN DETAILS#
        gname_var = StringVar()
        gname_entrybox = Entry(self.g_frame, width = 16, textvariable = gname_var)
        gname_entrybox.place(x = 725, y = 227)

        gphone_var = IntVar()
        gphone_entrybox = Entry(self.g_frame, width = 16, textvariable = gphone_var)
        gphone_entrybox.place(x = 725, y = 267)

        galt_var = IntVar()
        galt_entrybox = Entry(self.g_frame, width = 16, textvariable = galt_var)
        galt_entrybox.place(x = 725, y = 307)

        grole_var = StringVar()
        grole_entrybox = Entry(self.g_frame, width = 16, textvariable = grole_var)
        grole_entrybox.place(x = 725, y = 347)

        gaddr_var = StringVar()
        gaddr_entrybox = Entry(self.g_frame, width = 16, textvariable = gaddr_var)
        gaddr_entrybox.place(x = 725, y = 387)

        button = Button(self.g_frame, text = "SAVE AND NEXT", relief = "ridge", borderwidth = "5", bg = "white",
                        fg = "#33414f", width = 15)
        button.place(x = 575, y = 615)

    # ======================================================================#
    # END MAINLOOP FOR SECOND WINDOW#

    def student(self):
        # stu_frame=Frame(win)
        # stu_frame.place(x=0,y=0,height = 1350 , width = 1350)
        tablename_label = ttk.Label(self.stu_frame, text = "STUDENT DETAILS", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 20")
        tablename_label.place(x = 525, y = 130)

        studentid_label = ttk.Label(self.stu_frame, text = "Enter student id", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 20")
        studentid_label.place(x = 450, y = 180)

        firstname_label = ttk.Label(self.stu_frame, text = "Enter first name", background = "white",
                                    foreground = "#33414f",
                                    font = "georgia 20")
        firstname_label.place(x = 450, y = 210)

        lastname_label = ttk.Label(self.stu_frame, text = "Enter last name", background = "white",
                                   foreground = "#33414f",
                                   font = "georgia 20", anchor = 's')
        lastname_label.place(x = 450, y = 240)

        state_label = ttk.Label(self.stu_frame, text = "Enter state", background = "white", foreground = "#33414f",
                                font = "georgia 20", anchor = 's')
        state_label.place(x = 450, y = 270)

        city_label = ttk.Label(self.stu_frame, text = "Enter city", background = "white", foreground = "#33414f",
                               font = "georgia 20", anchor = 's')
        city_label.place(x = 450, y = 300)

        street_label = ttk.Label(self.stu_frame, text = "Enter street", background = "white", foreground = "#33414f",
                                 font = "georgia 20", anchor = 's')
        street_label.place(x = 450, y = 330)

        face_label = ttk.Label(self.stu_frame, text = "Upload face photo", background = "white", foreground = "#33414f",
                               font = "georgia 20", anchor = 's')
        face_label.place(x = 450, y = 360)

        idproof_label = ttk.Label(self.stu_frame, text = "Upload id proof", background = "white",
                                  foreground = "#33414f",
                                  font = "georgia 20", anchor = 's')
        idproof_label.place(x = 450, y = 390)

        gender_label = ttk.Label(self.stu_frame, text = "Select your gender", background = "white",
                                 foreground = "#33414f",
                                 font = "georgia 20", anchor = 's')
        gender_label.place(x = 450, y = 420)

        phone_label = ttk.Label(self.stu_frame, text = "Enter Phone no", background = "white", foreground = "#33414f",
                                font = "georgia 20", anchor = 's')
        phone_label.place(x = 450, y = 452)
        alt_label = ttk.Label(self.stu_frame, text = "Enter Alt Phone no", background = "white", foreground = "#33414f",
                              font = "georgia 20", anchor = 's')
        alt_label.place(x = 450, y = 480)

        # ----------------------------------------------------------------------#
        # ENTRY BOXES FOR STUDENT DETAILS#

        stid_var = IntVar()
        stid_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = stid_var)
        stid_entrybox.place(x = 720, y = 187)
        stid_entrybox.focus()

        firstname_var = StringVar()
        firstname_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = firstname_var)
        firstname_entrybox.place(x = 720, y = 217)

        lastname_var = StringVar()
        lastname_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = lastname_var)
        lastname_entrybox.place(x = 720, y = 247)

        state_var = StringVar()
        state_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = state_var)
        state_entrybox.place(x = 720, y = 277)

        city_var = StringVar()
        city_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = city_var)
        city_entrybox.place(x = 720, y = 307)

        street_var = StringVar()
        street_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = street_var)
        street_entrybox.place(x = 720, y = 337)

        # ----------------------------------------------------------------------#
        # BUTTONS FOR STUDENT DETAILS#

        def filed():
            filename = filedialog.askopenfilename(initialdir = "/", title = "Select Image",
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            file = filename
            print(file)

        uploadface_button = ttk.Button(self.stu_frame, text = 'upload', command = lambda: filed())
        uploadface_button.place(x = 730, y = 367)

        uploadproof_button = ttk.Button(self.stu_frame, text = 'upload', command = lambda: filed())
        uploadproof_button.place(x = 730, y = 397)

        # ----------------------------------------------------------------------#
        # COMBO BOX FOR STUDENT DETAILS AND DESTROY THE WINDOW 1#

        gender_var = StringVar()
        gender_combobox = ttk.Combobox(self.stu_frame, width = 14, textvariable = gender_var, state = 'readonly')
        gender_combobox['values'] = ('male', 'female')
        gender_combobox.place(x = 720, y = 427)

        phone_var = IntVar()
        phone_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = phone_var)
        phone_entrybox.place(x = 720, y = 457)

        alt_var = IntVar()
        alt_entrybox = ttk.Entry(self.stu_frame, width = 16, textvariable = phone_var)
        alt_entrybox.place(x = 720, y = 487)

        def save():
            st_id = stid_entrybox.get()
            fname = firstname_entrybox.get()
            lname = lastname_entrybox.get()
            state = state_entrybox.get()
            city = city_entrybox.get()
            street = street_entrybox.get()
            gender = gender_combobox.get()
            self.guardian()

        button = Button(self.stu_frame, text = "SAVE AND NEXT", relief = "ridge", borderwidth = "5", bg = "white",
                        fg = "#33414f",
                        width = 15, command = self.stu_frame.destroy)
        button.place(x = 580, y = 600)


class Student():
    id = 0
    name = ""
    phoneno = 0
    gid = 0
    gname = ""
    gphoneno = 0
    var = IntVar()

    def stu_page(self):
        window1.title("STUDENT PAGE")
        stu_frame1 = Frame(window1, bg = "#efefef")
        stu_frame1.place(x = 0, y = 0, height = 1350, width = 1350)
        bottom_label = Label(stu_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b")
        bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        vertical_frame = Frame(stu_frame1, bg = "#33414f")
        vertical_frame.place(x = 0, y = 0, height = 680, width = 280)
        sidl = Label(vertical_frame, text = "ID:              {}".format(self.id), fg = "#efefef", bg = "#33414f",
                     font = "Georgia")
        sidl.place(x = 0, y = 200);
        snamel = Label(vertical_frame, text = "Name:        {}".format(self.phoneno), fg = "#efefef", bg = "#33414f",
                       font = "Georgia")
        snamel.place(x = 0, y = 230);
        add_comp = Label(vertical_frame, )
        g_frame = Frame(stu_frame1, bg = "#F6F6F6")
        g_frame.place(x = 350, y = 40, height = 300, width = 300)
        g_detail = Label(g_frame, text = "Guardian Details",
                         font = "times", fg = "#33414f", bg = "#F6F6F6")
        g_detail.place(x = 0, y = 0)

        edit_guardian = Button(g_frame, image = edit, fg = "#F6F6F6", borderwidth = 0)
        edit_guardian.place(x = 272, y = 0)
        pay_frame = Frame(window1, bg = "#F6F6F6")
        pay_frame.place(x = 780, y = 40, height = 300, width = 300)
        pay_detail = Label(pay_frame, text = "Payment Details",
                           font = "times", fg = "#33414f", bg = "#F6F6F6")
        pay_detail.place(x = 0, y = 0)
        edit_pay = Button(pay_frame, image = edit, fg = "#F6F6F6", borderwidth = 0)
        edit_pay.place(x = 272, y = 0)

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

        stdid_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white")
        stdid_enter.place(x = 20, y = 60, width = 400, height = 30)
        # id = stdid_enter.get()
        stdphone_enter = Entry(display_l, font = "georgia 12", relief = "groove", borderwidth = 0.6, bg = "white")
        stdphone_enter.place(x = 20, y = 120, width = 400, height = 30)

        # phone = stdphone_enter.get()
        # def generate_otp():
        #     otp_no = StringVar()
        #     labelbox = Label(display_l, borderwidth = 0, bg = "white")
        #     labelbox.place(x=20,y=0 , height = 200 ,width = 400)
        #
        #     label_otp = Label(labelbox, text = "ENTER VALID OTP ",font = "georgia 12", borderwidth = 0, bg = "white",fg ="grey")
        #     label_otp.place(x=10,y=40)
        #     enter_otp = Entry(labelbox , textvariable = otp_no,font = "georgia 12", borderwidth = 0.6 , bg = "white" , relief = "groove")
        #     enter_otp.place(x=10,y=60,height = 30 , width = 400)
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
        def check():
            id = stdid_enter.get()
            phoneno = stdphone_enter.get()
            self.id = id
            self.phoneno = phoneno
            self.stu_page()
            print(id)
            print(phoneno)

        def register():
            r = RegisterStudent()
            # r.student()
            # r.guardian()

        newuser = Button(label_1, text = "New User!Register?", fg = "#33414f", bg = "white",
                         font = "georgia 12 bold underline", relief = "flat", borderwidth = 0,
                         activebackground = "white", activeforeground = "#33414f", highlightcolor = "white",
                         command = register)
        newuser.place(x = 13, y = 335)

        la = ImageTk.PhotoImage(Image.open(r"label.png").resize((120, 45)))
        label = Label(label_1, image = la, borderwidth = 0, bg = "white")
        label.place(x = 140, y = 400)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 12 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = check)
        submit.place(x = 15, y = 3)


class Manager:
    id = 0
    name = ""
    phoneno = 0
    var = IntVar()

    def mgr_page(self):
        window1.title("MANAGER PAGE")
        mgr_frame1 = Frame(window1, bg = "#efefef")
        mgr_frame1.place(x = 0, y = 0, height = 1350, width = 1350)
        bottom_label = Label(mgr_frame1, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                             font = "times", fg = "#33414f", bg = "#1daf9b")
        bottom_label.place(x = 0, y = 680, height = 30, width = 1350)
        vertical_frame = Frame(mgr_frame1, bg = "#33414f")
        vertical_frame.place(x = 0, y = 0, height = 680, width = 280)
        empidl = Label(vertical_frame, text = "ID:              {}".format(self.id), fg = "#efefef", bg = "#33414f",
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
        # edit_pay = Button(mgr_frame1,image=edit,fg = "#F6F6F6",borderwidth=0)
        # edit_pay.place(x= 272, y= 0)
        complaints = Frame(mgr_frame1, bg = "#F6F6F6")
        complaints.place(x = 900, y = 40, height = 580, width = 400)
        comp_label = Label(complaints, text = "                          COMPLAINT BOX",
                           font = "times", fg = "#33414f", bg = "#F6F6F6")
        comp_label.place(x = 0, y = 0)

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
        std_id = Label(display_l, text = "  EMPLOYEE ID ", bg = "white", fg = "grey", font = "georgia 12 ")
        std_id.place(x = 10, y = 40)
        phone = Label(display_l, text = "  PHONE NUMBER ", bg = "white", fg = "grey", font = "georgia 12 ")
        phone.place(x = 10, y = 100)

        stud_id = StringVar()
        phone_no = IntVar()
        stdid_enter = Entry(display_l, textvariable = stud_id, font = "georgia 12", relief = "groove",
                            borderwidth = 0.6, bg = "white")
        stdid_enter.place(x = 20, y = 60, width = 400, height = 30)

        stdphone_enter = Entry(display_l, textvariable = phone_no, font = "georgia 12", relief = "groove",
                               borderwidth = 0.6, bg = "white")
        stdphone_enter.place(x = 20, y = 120, width = 400, height = 30)

        def generate_otp():
            otp_no = StringVar()
            labelbox = Label(display_l, borderwidth = 0, bg = "white")
            labelbox.place(x = 10, y = 0, height = 200, width = 400)

            label_otp = Label(labelbox, text = "ENTER VALID OTP ", font = "georgia 12", borderwidth = 0, bg = "white",
                              fg = "grey")
            label_otp.place(x = 10, y = 10)
            enter_otp = Entry(labelbox, textvariable = otp_no, font = "georgia 12", borderwidth = 0.6, bg = "white",
                              relief = "groove")
            enter_otp.place(x = 10, y = 30, height = 30, width = 400)

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

            # label = Label(display_l , image = la , borderwidth = 0 , bg = "white")
            # label.place(x=130,y=100)
            #
            # submit = Button(label,text = "SUBMIT",fg = "#efefef" , bg ="#1daf9b" ,font = "georgia 12 bold" , relief = "flat" , borderwidth = 0,activebackground ="#1daf9b" , activeforeground = "#1dafb9" , highlightcolor = "#1dafb9" , command = self.mgr_page)
            # submit.place(x=18,y=6)

        la = ImageTk.PhotoImage(Image.open(r"label.png").resize((150, 45)))
        label = Label(label_1, image = la, borderwidth = 0, bg = "white")
        label.place(x = 140, y = 400)

        submit = Button(label, text = "SUBMIT", fg = "#33414f", bg = "#1daf9b", font = "georgia 12 bold",
                        relief = "flat", borderwidth = 0, activebackground = "#1daf9b", activeforeground = "#1dafb9",
                        highlightcolor = "#1dafb9", command = generate_otp)
        submit.place(x = 15, y = 6)


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
                                 font = "times", fg = "#33414f", bg = "#1daf9b")
        background_label.place(x = 0, y = 680, height = 30, width = 1350)


# FOR INSERTING LOGO IMAGE :-
def action():
    window_frame.destroy()
    l = Login()
    l.action()


background = Button(window_frame, image = mainlogo, borderwidth = 0, bg = "#efefef", command = action,
                    activebackground = "#efefef", activeforeground = "#efefef", highlightcolor = "#efefef")
background.place(x = 380, y = 80)

background_label = Label(window_frame, text = "@2020 by Students of TY CET,SCET,MITWPU,All rights reserved.",
                         font = "times", fg = "#33414f", bg = "#1daf9b")
background_label.place(x = 0, y = 680, height = 30, width = 1350)
background_label2 = Label(window_frame, bg = "#1daf9b")
background_label2.place(x = 0, y = 0, width = 1350)

window1.mainloop()
