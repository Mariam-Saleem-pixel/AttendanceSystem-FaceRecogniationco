# ======================Haar cascade Algorithm=======Video 4 
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#Machine Learning data set found in open cv
import cv2 

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("face Recognition System")
        # variables==========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #First img

        img = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download.jfif")
        img=img.resize((500,130),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
 
        img1 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download.jfif")
        img1=img1.resize((500,130),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #3rd Image

        img2 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download.jfif")
        img2=img2.resize((500,130),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
         #background img
        img3 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\bg.jpg")
        img3=img3.resize((1530,710),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="green",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=46,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE)
        Left_frame.place(x=10,y=10,width=660,height=525)

        Border=LabelFrame(Left_frame,bg="light green",text="STUDENT DETAILS",font=("times new roman",14,"bold"))
        Border.place(x=0,y=0,width=660,height=50)

        #current_course
        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current course information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=5,y=53,width=650,height=150)
        #department      

        dep_label=Label(current_course_frame,text="Department ",bg="white",font=("times new roman",14,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Computer Engineering","Software")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10)

        #Course      

        course_label=Label(current_course_frame,text="Course ",bg="white",font=("times new roman",14,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CC","DIP","FA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        #Year      

        year_label=Label(current_course_frame,text="Year ",bg="white",font=("times new roman",14,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-24","2021-25","2022-26","2023-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        #Semester      

        semester_label=Label(current_course_frame,text="Semester ",bg="white",font=("times new roman",14,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",14,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","8th","6th","4th","2nd")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #class student information 
        class_student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",14,"bold"))
        class_student_frame.place(x=5,y=170,width=650,height=340)
        # Student id
        studentId_label=Label(class_student_frame,text="Student ID ",bg="white",font=("times new roman",14,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",14,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        student_name_label=Label(class_student_frame,text="Student Name ",bg="white",font=("times new roman",14,"bold"))
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",14,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_division_label=Label(class_student_frame,text="Class Division ",bg="white",font=("times new roman",14,"bold"))
        class_division_label.grid(row=1,column=0,padx=5,pady=0,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",14,"bold"),width=14,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        # Roll No
        student_rollno_label=Label(class_student_frame,text="Roll No",bg="white",font=("times new roman",14,"bold"))
        student_rollno_label.grid(row=1,column=2,padx=10,sticky=W)
        student_rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",14,"bold"))
        student_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        # Gender
        gender_label=Label(class_student_frame,text="Gender ",bg="white",font=("times new roman",14,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=14,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        # DOB
        DOB_label=Label(class_student_frame,text="DOB ",bg="white",font=("times new roman",14,"bold"))
        DOB_label.grid(row=2,column=2,padx=10,sticky=W)
        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",14,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        # Email
        Email_label=Label(class_student_frame,text="Email ",bg="white",font=("times new roman",14,"bold"))
        Email_label.grid(row=3,column=0,padx=10,sticky=W)
        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",14,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone number
        phone_label=Label(class_student_frame,text="Phone No ",bg="white",font=("times new roman",14,"bold"))
        phone_label.grid(row=3,column=2,padx=10,sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",14,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #    address number
        address_label=Label(class_student_frame,text="Address: ",bg="white",font=("times new roman",14,"bold"))
        address_label.grid(row=4,column=0,padx=10,sticky=W)
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",14,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # teacher number
        teacher_label=Label(class_student_frame,text="Teacher Name: ",bg="white",font=("times new roman",14,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",14,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #Radio buttons with the help of ttk
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take a Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0)
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        #button frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=229,width=648,height=49)
        #save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,padx=44,font=("times new roman",14,"bold"),bg="Green",fg="White")
        save_btn.grid(row=0,column=0,padx=5,pady=5)
        #update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,padx=44,font=("times new roman",14,"bold"),bg="Green",fg="White")
        update_btn.grid(row=0,column=1,padx=5,pady=5)
        #delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,padx=44,font=("times new roman",14,"bold"),bg="Red",fg="White")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)
        # #reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,padx=44,font=("times new roman",14,"bold"),bg="Green",fg="White")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)
        #photo button frame
        photo_btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="White")
        photo_btn_frame.place(x=0,y=279,width=648,height=49)
        #Take photo Sample
        take_photo_btn=Button(photo_btn_frame, text="Photo Sample",command=self.generate_dataset,width=28,font=("times new roman",15,"bold"),bg="Green",fg="White")
        take_photo_btn.grid(row=1,column=0)
        #Update photo Sample
        update_photo_btn=Button(photo_btn_frame,text="Update",width=28,font=("times new roman",15,"bold"),bg="Green",fg="White")
        update_photo_btn.grid(row=1,column=2)
        #right label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,font=("times new roman",14,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=520)
        
        Border=LabelFrame(Right_frame,bg="light green",text="STUDENT DETAILS",font=("times new roman",14,"bold"))
        Border.place(x=0,y=0,width=660,height=50)
        # ======Search System======= 
        search_frame=LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=5,y=50,width=650,height=95)
        btn_search=Label(search_frame,text="Search by",bg="green",fg="white")
        btn_search.grid(row=0,column=0,padx=3)
        #combo box for roll number
        search_combo=ttk.Combobox(search_frame,font=("times new roman",14,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Roll number","Department")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        #Entry for search
        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        #Search btn
        search_btn=Button(search_frame,text="Search",padx=30,font=("times new roman",14,"bold"),bg="blue",fg="White")
        search_btn.grid(row=0,column=3,padx=5,pady=5)
        # showAll button
        showall_btn=Button(search_frame,text="Reset",padx=30,font=("times new roman",14,"bold"),bg="Green",fg="White")
        showall_btn.grid(row=0,column=4,padx=5,pady=5)
        #table
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=150,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","gender","roll","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="RolNo")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ============function declartion=======
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password="Downloadming1",
                    database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()

                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    # ============fetch data========
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password="Downloadming1",
                    database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # ===== Get Cursor========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


    # =====Update Function=====
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password="Downloadming1",
                    database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()
                                                                                                                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student Details Successfully Update",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)
    # ======delete function===
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must me required",parent=self.root)
        else:
            try:
                delete =messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password="Downloadming1",
                    database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)
    # =========reset=========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ==========Generate data set or take a photo sample=====
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "root",
                    password="Downloadming1",
                    database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ===============load predified data on face frontals from openCV======
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                # ====BGR imgs convert into gray scale======
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # 1.3=scaling factor    , minimum neighbor= 5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                # Original camera open then value 0 in below videocapture function if other camera open then put 1
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                    # ======Crop img====
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    # image name......user.1.2.jpg
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                    # =====FONT_HERSHEY_COMPLEX,fontscale,fontcolor,thickness
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                    #  ====13 means After press enter window open will automatically close==
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
