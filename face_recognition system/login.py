from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_recognition_System
import mysql.connector


def main():
     win = Tk()
     app = Login_window(win)
     win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x780+0+0")
        self.bg=ImageTk.PhotoImage

        frame = Frame(self.root,bg="black")
        frame.place(x=600,y=170,width=340,height=450)

        img1 = Image.open(r"C:\Users\M.Tayyab KAMBOH\Desktop\face_recognition system\images\img.jpeg")
        img1=img1.resize((100,100),Image.BICUBIC)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        #username
        username = lbl = Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=40,y=140)

        self.txtuser =Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=230)
#password
        password = lbl = Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=40,y=215)

        self.txtpass =Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=230)

        loginbtn = Button(frame,text="Login",command = self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=80,y=300,width=120,height=35)

        registerbtn = Button(frame,command=self.register_window,text="Register",font=("times new roman",10,"bold"),relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="gray")
        registerbtn.place(x=20,y=350,width=120)

        # forgetbtn = Button(frame,text="Forget Password",font=("times new roman",10,"bold"),relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="gray")
        # forgetbtn.place(x=20,y=370,width=120)
    
    def register_window(self):
         self.new_window = Toplevel(self.root)
         self.app= Register(self.new_window)

    def login(self):
        
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Mariam" and self.txtpass.get()=="112233":
            messagebox.showinfo("Success","Welcome")
        else:
             conn = mysql.connector.connect(host="localhost",user="root",password="Downloadming1",database="face_recognizer")
             mycursor = conn.cursor()
             mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
             row = mycursor.fetchone()
             if row==None:
                  messagebox.showerror("Error","Invalid Username & password")
             else:
                  open_main = messagebox.askyesno("yesno","Access only admin")
                  if open_main>0:
                       self.new_window=Toplevel(self.root)
                       self.app=Face_recognition_System(self.new_window)
                  else:
                       if not open_main:
                            return
             conn.commit()
             self.clear()
             conn.close()
    
    

             
class Register:
    def __init__(self,root):
        self.root = root 
        self.root.title("Register")
        self.root.geometry("1600x800+0+0")

        # ===========variable=======
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_phone_no = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = StringVar()


        frame = Frame(self.root,bg="lightblue")
        frame.place(x=300,y=100,width=800,height=550)

        register_lbl = Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkblue",bg="lightblue")
        register_lbl.place(x=300,y=10)

        fname = Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="lightblue")
        fname.place(x=50,y=50)

        self.txtuser =Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=90,width=230)

        lname = Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="lightblue")
        lname.place(x=400,y=50)

        self.txtuser =Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=400,y=90,width=230)

        email = Label(frame,text="Email",font=("times new roman",20,"bold"),bg="lightblue")
        email.place(x=50,y=150)

        self.txtuser =Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=190,width=230)

        phone = Label(frame,text="Phone no.",font=("times new roman",20,"bold"),bg="lightblue")
        phone.place(x=400,y=150)

        self.txtuser =Entry(frame,textvariable=self.var_phone_no,font=("times new roman",15,"bold"))
        self.txtuser.place(x=400,y=190,width=230)

        Password = Label(frame,text="Password",font=("times new roman",20,"bold"),bg="lightblue")
        Password.place(x=50,y=250)

        self.txtuser =Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=300,width=230)

        Confirm_Password  = Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="lightblue")
        Confirm_Password.place(x=400,y=250)

        self.txtuser =Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txtuser.place(x=400,y=300,width=230)

         
        checkbtn = Checkbutton(frame,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="lightblue",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=350)

        Registerbtn = Button(frame,command=self.register_data,text="Register Now",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        Registerbtn.place(x=50,y=400,width=150,height=40)

        loginbtn = Button(frame,command=self.return_login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=300,y=400,width=150,height=40) 

      # ======function decartion=========
    def return_login(self):
         self.root.destroy() 

    def register_data(self):
          if self.var_fname.get()=="" or self.var_email.get()=="":
               messagebox.showerror("Error","All fields required")
          elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and confirm password must be same")
          elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions")
          else:
                 conn = mysql.connector.connect(host="localhost",user="root",password="Downloadming1",database="face_recognizer")
                 mycursor = conn.cursor()
                 query = ("select * from register where email=%s")
                 value=(self.var_email.get(),)
                 mycursor.execute(query,value)
                 row = mycursor.fetchone()
                 if row!=None:
                      messagebox.showerror("Error","User already exist, please try another email")
                 else:
                      mycursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_phone_no.get(),
                                                                                      self.var_pass.get()
                                                                                      
                                                                                      ))
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Register Successfully")



        

if __name__=="__main__":
     main() 