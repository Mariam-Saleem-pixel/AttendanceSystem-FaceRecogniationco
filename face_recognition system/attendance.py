from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
# grid by using numpy
import numpy as np
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

my_data = []
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("face Recognition System")

        # ===============Text Variable==========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        title_lbl=Label(self.root,text="ATTENDANCE",font=("times new roman",35,"bold"),bg="green",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download.jfif")
        img=img.resize((500,130),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
 
        img1 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download.png")
        img1=img1.resize((500,130),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
      #3rd Image

        img2 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\download1.jfif")
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

        title_lbl=Label(bg_img,text="ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=46,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE)
        Left_frame.place(x=10,y=10,width=660,height=525)

        Border=LabelFrame(Left_frame,bg="light green",text="ATTENDANCE DETAILS",font=("times new roman",14,"bold"))
        Border.place(x=0,y=0,width=660,height=50)


        #right label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,font=("times new roman",14,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=520)

        Border=LabelFrame(Right_frame,bg="light green",text="STUDENT DETAILS",font=("times new roman",14,"bold"))
        Border.place(x=0,y=0,width=660,height=50)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=55,width=655,height=455)

        # ==========Label and entries==========
        # Student id
        attendanceId_label=Label(left_inside_frame,text="AttendanceID: ",bg="white",font=("times new roman",14,"bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",14,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll
        rollLabel=Label(left_inside_frame,text="Roll: ",bg="white",font=("times new roman",14,"bold"))
        rollLabel.grid(row=0,column=2,padx=10,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",14,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        nameLabel=Label(left_inside_frame,text="Name: ",bg="white",font=("times new roman",14,"bold"))
        nameLabel.grid(row=1,column=0,padx=10,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",14,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Department
        depLabel=Label(left_inside_frame,text="Department: ",bg="white",font=("times new roman",14,"bold"))
        depLabel.grid(row=1,column=2,padx=10,sticky=W)
        
        atten_dep_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("times new roman",14,"bold"))
        atten_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # time
        timeLabel=Label(left_inside_frame,text="Time: ",bg="white",font=("times new roman",14,"bold"))
        timeLabel.grid(row=2,column=0,padx=10,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",14,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date
        dateLabel=Label(left_inside_frame,text="Date: ",bg="white",font=("times new roman",14,"bold"))
        dateLabel.grid(row=2,column=2,padx=10,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",14,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status: ",bg="white",font=("times new roman",14,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.atten_status = ttk.Combobox(left_inside_frame,width=17,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=5)
        self.atten_status.current(0)
        
        #button frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=370,width=648,height=49)
        #import
        import_btn=Button(btn_frame,text="ImportCsv",command=self.importCsv,padx=60,font=("times new roman",14,"bold"),bg="Green",fg="White")
        import_btn.grid(row=0,column=0)
        #export
        export_btn=Button(btn_frame,text="ExportCsv",command=self.exportCsv,padx=60,font=("times new roman",14,"bold"),bg="Green",fg="White")
        export_btn.grid(row=0,column=1)
        #update
        # update_btn=Button(btn_frame,text="Update",command=self.update_data,padx=53,font=("times new roman",14,"bold"),bg="Green",fg="White")
        # update_btn.grid(row=0,column=2)
        # #reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,padx=70,font=("times new roman",14,"bold"),bg="Green",fg="White")
        reset_btn.grid(row=0,column=2)

        #right label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,font=("times new roman",14,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=520)

        Border=LabelFrame(Right_frame,bg="light green",text="STUDENT DETAILS",font=("times new roman",14,"bold"))
        Border.place(x=0,y=0,width=660,height=50)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="White")
        table_frame.place(x=5,y=55,width=640,height=450)

        # =======scroll bar============
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        # Set width if eacg column in right frame
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ===============Fetch data===========
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)
    # ==================import=========
    def importCsv(self):
        global my_data
        # my_data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln)as myfile:
          csvread = csv.reader(myfile,delimiter=",")
          for i in csvread:
            my_data.append(i)
          self.fetchData(my_data)

    # ===========Export data=======
    def exportCsv(self):
      try:
        if len(my_data)<1:
          messagebox.showerror("no data","No Data Export",parent=self.root)
          return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write = csv.writer(myfile,delimiter=",")
          for i in my_data:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Exported Data to"+os.path.basename(fln)+"Succesfully")
      except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
      cursor_row = self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
      rows = content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])


    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("Status")
    

    # def update_data(self):
    #   if self.var_atten_dep.get()=="Select Department" or self.var_atten_name.get()=="" or self.var_atten_id.get()=="":
    #      messagebox.showerror("Error","All fields are required",parent=self.root)
      # else:
      #   update will do from this position

            




                
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()