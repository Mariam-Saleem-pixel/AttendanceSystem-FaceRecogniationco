from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import tkinter

class  Help:
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

      title_lbl=Label(bg_img,text="How Web App works?",font=("times new roman",35,"bold"),bg="white",fg="red")
      title_lbl.place(x=0,y=0,width=1530,height=45)

      
      title_lbl=Label(bg_img,text="Steps: \n 1.Click student detail button and add all detail of student i.e: student name,student roll no., student id etc. \n 2. Take Photo Samples by clicking photo sample button it will take 100 images in 10-12 seconds. \n 3. Train the model by clicking to Train button. \n 4. Mark the Student attendance by clicking face recognization button which student comes next to \n camera his/her attendance marked automatically and save in excel file. \n 5. By clicking Attendance button you will click import csv button, import all files of which you want \n to draw histogram. \n 6. After this you can check the no. of attendance of all students by clicking histogram button \n 7. For any Query you feel free for contact us: \n \n \n Email: mariamsaleem6620@gmail.com \n Phone no.: 03046620435 \n   ",font=("times new roman",25),bg="white",fg="black")
      title_lbl.place(x=0,y=50)


if __name__=="__main__":
    root=Tk()
    obj= Help(root)
    root.mainloop()