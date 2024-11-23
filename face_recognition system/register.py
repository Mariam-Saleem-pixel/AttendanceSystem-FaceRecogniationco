from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
 

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
    def return_login(self):
         self.root.destory()
    # def login_data(self):
    #   self.new_window=Toplevel(self.root)
    #   self.app= Login_window(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop() 