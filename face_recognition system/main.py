from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Histogram
from help import Help
import tkinter

class Face_recognition_System:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("face Recognition System")
      #First img

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

      title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
      title_lbl.place(x=0,y=0,width=1530,height=45)
        # std button

      img4 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std.jfif")
      img4=img4.resize((220,220),Image.BICUBIC)
      self.photoimg4=ImageTk.PhotoImage(img4)

      b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
      b1.place(x=100,y=80,width=220,height=220)

      b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=100,y=280,width=220,height=40)

         #detect Facebutton

      img5 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std1.jfif")
      img5=img5.resize((220,220),Image.BICUBIC)
      self.photoimg5=ImageTk.PhotoImage(img5)

      b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
      b1.place(x=400,y=80,width=220,height=220)

      b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=400,y=280,width=220,height=40)


         #attandance button

      img6 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std3.jfif")
      img6=img6.resize((220,220),Image.BICUBIC)
      self.photoimg6=ImageTk.PhotoImage(img6)

      b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attandance_data)
      b1.place(x=700,y=80,width=220,height=220)

      b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attandance_data,font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=700,y=280,width=220,height=40)
        
         #help button

      img7 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\help.png")
      img7=img7.resize((220,220),Image.BICUBIC)
      self.photoimg7=ImageTk.PhotoImage(img7)

      b1=Button(bg_img,command=self.help_data,image=self.photoimg7,cursor="hand2")
      b1.place(x=1020,y=80,width=220,height=220)

      b1_1=Button(bg_img,text="Help",command=self.help_data ,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=1020,y=280,width=220,height=40)
        

        #TRAIN button

      img8 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std5.jfif")
      img8=img8.resize((220,220),Image.BICUBIC)
      self.photoimg8=ImageTk.PhotoImage(img8)

      b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
      b1.place(x=100,y=350,width=220,height=220)

      b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=100,y=550,width=220,height=40)

           #photo button

      img9 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std6.jfif")
      img9=img9.resize((220,220),Image.BICUBIC)
      self.photoimg9=ImageTk.PhotoImage(img9)

      b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
      b1.place(x=400,y=350,width=220,height=220)

      b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=400,y=550,width=220,height=40)

        
           #histogram button

      img10 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\histogram.jfif")
      img10=img10.resize((220,220),Image.BICUBIC)
      self.photoimg10=ImageTk.PhotoImage(img10)

      b1=Button(bg_img,image=self.photoimg10,command=self.histogram_data,cursor="hand2")
      b1.place(x=700,y=350,width=220,height=220)

      b1_1=Button(bg_img,text="Histogram",command=self.histogram_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=700,y=550,width=220,height=40)
           #exit button

      img11 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\std8.jfif")
      img11=img11.resize((220,220),Image.BICUBIC)
      self.photoimg11=ImageTk.PhotoImage(img11)

      b1=Button(bg_img,image=self.photoimg11,command=self.exit,cursor="hand2")
      b1.place(x=1020,y=350,width=220,height=220)

      b1_1=Button(bg_img,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
      b1_1.place(x=1020,y=550,width=220,height=40)
        
   def open_img(self):
       os.startfile("data")
# =========functin=====
   def exit(self):
      self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project?",parent = self.root)
      if self.exit > 0:
         self.root.destroy()
      else: 
         return
   def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)

   def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)

   def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)

   def attandance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)

   def  histogram_data(self):
      self.new_window=Toplevel(self.root)
      self.app= Histogram(self.new_window)

   def  help_data(self):
      self.new_window=Toplevel(self.root)
      self.app= Help(self.new_window)
    
     



if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
