from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#Machine Learning data set found in open cv
import cv2 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Histogram:
    def __init__(self,root):
        # self.root=root
        # self.root.geometry("1530x750+0+0")
        # self.root.title("face Recognition System")
        # title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="green",fg="yellow")
        # title_lbl.place(x=0,y=0,width=1530,height=45)
        
        data = pd.read_csv('All data.csv')
        print(data)
        data.dropna(inplace=True)      
        sns.histplot(data['Name'],kde=False)
        plt.show()

        

if __name__=="__main__":
    root=Tk()
    obj= Histogram(root)
    root.mainloop()
    
