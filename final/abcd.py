class Booking:
    hid=0
    rid=0
    jdate=""
    stid=0
    hostel=0
    roomtype=""
    ptype=""
    pamount=0
    pdate=""
    price=0
    paymentss=""
    def __init__(self,st_id):
        self.stid=st_id
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
        
        # bookingroom(self.hid,self.rid,self.stid,self.jdate)
        answer = messagebox.askokcancel("Registration","Registration Request Sent!!")
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

            self.B2N_button=Button(self.room_label,bg="white",image=self.B2N,borderwidth=0,activebackground="white",command=lambda:which_room("B2N",hostel_id))
            self.B2N_button.place(x=35,y=35)

            self.B3N_button=Button(self.room_label,bg="white",image=self.B3N,borderwidth=0,activebackground="white",command=lambda:which_room("B3N",hostel_id))
            self.B3N_button.place(x=220,y=35) 
            
            self.B2A_button=Button(self.room_label,bg="white",image=self.B2A,borderwidth=0,activebackground="white",command=lambda:which_room("B2A",hostel_id))
            self.B2A_button.place(x=405,y=35)        

            self.B2B_button=Button(self.room_label,bg="white",image=self.B2B,borderwidth=0,activebackground="white",command=lambda:which_room("B2B",hostel_id))
            self.B2B_button.place(x=590,y=35)
            self.submitroom=Button(self.room_label,bg="#33414f",fg="white",text="SUBMIT",font="georgia 10 bold",relief="raised",command=self.booking)
            self.submitroom.place(x=360,y=460)        
           
        #placing room images as button
        self.B2N_button=Button(self.room_label,bg="white",image=self.B2N,borderwidth=0,activebackground="white",command=lambda:which_room("B2N",hostel_id))
        self.B2N_button.place(x=35,y=35)

        self.B3N_button=Button(self.room_label,bg="white",image=self.B3N,borderwidth=0,activebackground="white",command=lambda:which_room("B3N",hostel_id))
        self.B3N_button.place(x=220,y=35) 

        self.B2A_button=Button(self.room_label,bg="white",image=self.B2A,borderwidth=0,activebackground="white",command=lambda:which_room("B2A",hostel_id))
        self.B2A_button.place(x=405,y=35)        
 
        self.B2B_button=Button(self.room_label,bg="white",image=self.B2B,borderwidth=0,activebackground="white",command=lambda:which_room("B2B",hostel_id))
        self.B2B_button.place(x=590,y=35)
        

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
        self.h1 = ImageTk.PhotoImage(Image.open(r"h1.png").resize((150,150)))
        self.h2 = ImageTk.PhotoImage(Image.open(r"h2.png").resize((150,150)))
        self.h3 = ImageTk.PhotoImage(Image.open(r"h3.png").resize((150,150)))
        self.h4 = ImageTk.PhotoImage(Image.open(r"h4.png").resize((150,150)))
        h1_button=Button(main_label,bg="white",image=self.h1,borderwidth=0,command=lambda:[self.room(1),white_frame1.destroy()])
        h1_button.place(x=35,y=35)

        self.hostel=hostelinfo(1)
        for x in self.hostel:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=35,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=35,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=35,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=35,y=370)

        h2_button=Button(main_label,bg="white",image=self.h2,borderwidth=0,command=lambda:[self.room(2),white_frame1.destroy()])
        h2_button.place(x=220,y=35)
        self.hostel=hostelinfo(2)
        for x in self.hostel:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=220,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=220,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=220,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=220,y=370)

        h3_button=Button(main_label,bg="white",image=self.h3,borderwidth=0,command=lambda: [self.room(3),white_frame1.destroy()])
        h3_button.place(x=405,y=35)
        self.hostel=hostelinfo(3)
        for x in self.hostel:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=405,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=405,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=405,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=405,y=370)

        h4_button=Button(main_label,bg="white",image=self.h4,borderwidth=0,command=lambda: [self.room(4),white_frame1.destroy()])
        h4_button.place(x=590,y=35)
        self.hostel=hostelinfo(4)
        for x in self.hostel:
            hid_label=Label(main_label,bg="white",fg ="#33414f",text="Hostel ID:{}".format(x[0]),font="georgia 12 bold")
            hid_label.place(x=590,y=250)
            hname_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[1]),font="georgia 12 bold")
            hname_label.place(x=590,y=290)
            haddr_label=Label(main_label,bg="white",fg ="#33414f",text="{}".format(x[2]),font="georgia 12 bold")
            haddr_label.place(x=590,y=330)
            htype_label=Label(main_label,bg="white",fg ="#33414f",text="{} Hostel".format(x[3]),font="georgia 12 bold")
            htype_label.place(x=590,y=370)

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
        inst2=(float(self.price[0][0])-inst1)/2
        inst3=(float(self.price[0][0])-inst1)/2
        inst4=float(self.price[0][0])
        self.hostellabel=Label(self.pay_label,text="{} Hostel,{}".format(self.hostel[0][1],self.hostel[0][2]),font = "georgia 12",fg = "#33414f",bg="white")
        self.hostellabel.place(x=5,y=100)
        self.room=Label(self.pay_label,text="Room No. {}".format(self.rid),font = "georgia 12",fg = "#33414f",bg="white")
        self.room.place(x=5,y=130)  
        self.type=Label(self.pay_label,text="Room Type {}".format(self.roomtype),font = "georgia 12",fg = "#33414f",bg="white")
        self.type.place(x=5,y=160)
        self.cost=Label(self.pay_label,text="Room Cost Rs.{}".format(inst4),font = "georgia 12",fg = "#33414f",bg="white")
        self.cost.place(x=5,y=190)  
        def payment_det(ptype):
            self.ptype=ptype
            self.select=Label(self.pay_label,text="Select Payment Method",font = "georgia 18 bold",fg = "#33414f",bg="white")
            self.select.place(x=45,y=0)
            self.hostellabel=Label(self.pay_label,text="{} Hostel,{}".format(self.hostel[0][1],self.hostel[0][2]),font = "georgia 12",fg = "#33414f",bg="white")
            self.hostellabel.place(x=5,y=100)
            self.room=Label(self.pay_label,text="Room No. {}".format(self.rid),font = "georgia 12",fg = "#33414f",bg="white")
            self.room.place(x=5,y=130)  
            self.type=Label(self.pay_label,text="Room Type {}".format(self.roomtype),font = "georgia 12",fg = "#33414f",bg="white")
            self.type.place(x=5,y=160)
            self.cost=Label(self.pay_label,text="Room Cost Rs.{}".format(inst4),font = "georgia 12",fg = "#33414f",bg="white")
            self.cost.place(x=5,y=190)  
            self.CCbutton= Button(self.pay_label, bg = "white",image=self.CC,relief="flat",cursor="hand2",command=lambda:payment_det("Credit Card"))
            self.CCbutton.place(x=7,y=40)
            self.NBbutton= Button(self.pay_label, bg = "white",image=self.NB,relief="flat",cursor="hand2",command=lambda:payment_det("Net Banking"))
            self.NBbutton.place(x=110,y=40)
            self.DCbutton= Button(self.pay_label, bg = "white",image=self.DC,relief="flat",cursor="hand2",command=lambda:payment_det("Debit Card"))
            self.DCbutton.place(x=210,y=40)
            self.WLbutton= Button(self.pay_label, bg = "white",image=self.WL,relief="flat",cursor="hand2",command=lambda:payment_det("UPI Wallet"))
            self.WLbutton.place(x=315,y=40)

            self.inst=Label(self.pay_label,text="Installment(Rs)",font = "georgia 12",fg = "#33414f",bg="white")
            self.inst.place(x=5,y=220)
            self.inst_var=IntVar()
            self.price_combobox = ttk.Combobox(self.pay_label, width = 14,font="georgia 12",foreground = "#33414f",textvariable = self.inst_var, state = 'readonly')
            self.price_combobox.place(x = 8, y = 250,width=375)
            self.price_combobox['values']=[inst1,inst2,inst3,inst4]
            self.price_combobox.set(inst1)
            self.date=Label(self.pay_label,text="Payment Date",font = "georgia 12",fg = "#33414f",bg="white")
            self.date.place(x=5,y=280)
            self.cal = DateEntry(self.pay_label, background="#33414f",foreground="white",activebackground="#33414f", borderwidth=2,year=datetime.datetime.today().year)
            self.cal.place(x = 8, y = 310,width=375)
            self.sslabel=Label(self.pay_label,bg="white")
            self.sslabel.place(x =8, y = 400,width=350)
            def uploadss():
                ss = filedialog.askopenfilename(initialdir = "/", title = "Select Image",            
                                                  filetype = ((".jpeg", "*.jpg"), (".png", "*.png")))
            
                g="""\\\\"""            
                self.paymentss=str(ss.replace('/',g))
                self.sslabel['text']=ss
            self.pss=Label(self.pay_label,text="Payment Screenshot",font = "georgia 12",fg = "#33414f",bg="white")
            self.pss.place(x=5,y=340)
            self.pssbutton= Button(self.pay_label,text="upload" ,bg = "#efefef",cursor="hand2",command=uploadss)
            self.pssbutton.place(x=5,y=370,width=375)

        self.CCbutton= Button(self.pay_label, bg = "white",image=self.CC,relief="flat",cursor="hand2",command=lambda:payment_det("Credit Card"))
        self.CCbutton.place(x=7,y=40)
        self.NBbutton= Button(self.pay_label, bg = "white",image=self.NB,relief="flat",cursor="hand2",command=lambda:payment_det("Net Banking"))
        self.NBbutton.place(x=110,y=40)
        self.DCbutton= Button(self.pay_label, bg = "white",image=self.DC,relief="flat",cursor="hand2",command=lambda:payment_det("Debit Card"))
        self.DCbutton.place(x=210,y=40)
        self.WLbutton= Button(self.pay_label, bg = "white",image=self.WL,relief="flat",cursor="hand2",command=lambda:payment_det("UPI Wallet"))
        self.WLbutton.place(x=315,y=40)
        def payment_done():
            self.pamount=self.inst_var.get()
            self.pdate=self.cal.get_date()
            
        self.submit= Button(self.pay_label, bg = "white",relief="flat",cursor="hand2",command=payment_done)
        self.submit.place(x=175,y=410)
