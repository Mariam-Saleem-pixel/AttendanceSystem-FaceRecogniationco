
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# class Face_recognition_System:
#    def __init__(self,root):
#       self.root=root
#       self.root.geometry("1530x790+0+0")
#       self.root.title("face Recognition System")
data = pd.read_csv('All data.csv')
print(data)
data.dropna(inplace=True)      
sns.histplot(data['Name'],kde=False)
plt.show()
 
# if __name__=="__main__":
#     root=Tk()
#     obj=Face_recognition_System(root)
#     root.mainloop()