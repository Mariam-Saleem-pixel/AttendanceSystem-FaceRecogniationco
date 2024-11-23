# =================================Train by using local binary pattern histogram(LBPH)=>1996==================
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
# grid by using numpy
import numpy as np
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("face Recognition System")
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="green",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        b1_1=Button(self.root,text="Train",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="lightgreen",fg="blue")
        b1_1.place(x=500,y=100,width=320,height=40)
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            # convert to gray scale image
            img = Image.open(image).convert('L')
            # uint8 is data type 
            imageNp = np.array(img,'uint8')
            # C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\data\user.1.1.jpg
            # [0                                                           ][1         ]
            #                                                               [0 ,1(id) ,2]
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        # ======To convert in array 88% perform good so we use numpy
        ids = np.array(ids)

        # ========= Train Classifier and save=======

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed")

    


      

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()