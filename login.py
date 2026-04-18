from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
import os

def main():
    root = Tk()
    app = login(root)
    root.mainloop()

class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition Attendance System")

        # ================= Top Banner Image =================
        self.frame_banner = Frame(self.root)
        self.frame_banner.place(x=0, y=0, width=1550, height=130)

        img_width = 516

       # Banner 1
        img1 = Image.open(r"D:\project of ai engineer\attendance system\college_images\BestFacialRecognition.jpg").resize((img_width, 130), Image.Resampling.LANCZOS)
        self.img_banner1 = ImageTk.PhotoImage(img1)
        self.lbl_banner1 = Label(self.frame_banner, image=self.img_banner1)
        self.lbl_banner1.grid(row=0, column=0)

       # Banner 2
        img2 = Image.open(r"D:\project of ai engineer\attendance system\college_images\facialrecognition.jpg").resize((img_width, 130), Image.Resampling.LANCZOS)
        self.img_banner2 = ImageTk.PhotoImage(img2)
        self.lbl_banner2 = Label(self.frame_banner, image=self.img_banner2)
        self.lbl_banner2.grid(row=0, column=1)

        # Banner 3
        img3 = Image.open(r"D:\project of ai engineer\attendance system\college_images\images.jpg").resize((img_width, 130), Image.Resampling.LANCZOS)
        self.img_banner3 = ImageTk.PhotoImage(img3)
        self.lbl_banner3 = Label(self.frame_banner, image=self.img_banner3)
        self.lbl_banner3.grid(row=0, column=2) 
        # ================= Title =================
        title_lbl = Label(self.root,
                          text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 28, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1550, height=60)

        # ================= Background =================
        bg_img = Image.open(r"D:\project of ai engineer\attendance system\college_images\lo.jpeg")
        bg_img = bg_img.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=190, width=1550, height=610)

        # ================= Login Frame =================
        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.62, anchor=CENTER, width=350, height=450)

        # ================= Profile Icon =================
        img1 = Image.open(r"D:\project of ai engineer\attendance system\college_images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(frame, image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=125, y=10, width=100, height=100)

        # ================= Heading =================
        get_str = Label(frame, text="Get Started",
                        font=("times new roman", 20, "bold"),
                        fg="white", bg="black")
        get_str.place(x=95, y=110)

        # ================= Username =================
        username = Label(frame, text="Username",
                         font=("times new roman", 15, "bold"),
                         fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=70, y=180, width=230)

        user_icon = Image.open(r"D:\project of ai engineer\attendance system\college_images\LoginIconAppl.png")
        user_icon = user_icon.resize((25, 25), Image.Resampling.LANCZOS)
        self.user_icon = ImageTk.PhotoImage(user_icon)

        lbl_user_icon = Label(frame, image=self.user_icon, bg="black")
        lbl_user_icon.place(x=40, y=180, width=25, height=25)

        # ================= Password =================
        password = Label(frame, text="Password",
                         font=("times new roman", 15, "bold"),
                         fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=70, y=250, width=230)

        pass_icon = Image.open(r"D:\project of ai engineer\attendance system\college_images\lock-512.png")
        pass_icon = pass_icon.resize((25, 25), Image.Resampling.LANCZOS)
        self.pass_icon = ImageTk.PhotoImage(pass_icon)

        lbl_pass_icon = Label(frame, image=self.pass_icon, bg="black")
        lbl_pass_icon.place(x=40, y=250, width=25, height=25)

        # ================= Login Button =================
        loginbtn = Button(frame, text="Login",
                          font=("times new roman", 15, "bold"),
                          fg="white", bg="#d90429",
                          activebackground="#ef233c",
                          cursor="hand2",
                          command=self.login)
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ================= Links =================
        registerbtn = Button(frame, text="New User Register",
                             font=("times new roman", 10, "bold"),
                             fg="white", bg="black",
                             cursor="hand2", borderwidth=0,
                             command=self.register_window)
        registerbtn.place(x=20, y=350)

        forgetbtn = Button(frame, text="Forget Password",
                           font=("times new roman", 10, "bold"),
                           fg="white", bg="black",
                           cursor="hand2", borderwidth=0,
                           command=self.forget_password_window)
        forgetbtn.place(x=20, y=380)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="jainandan", database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app =Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    #=================reset function=================
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer of security question", parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="jainandan", database="my_data")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND security=%s AND answer=%s"
            value = (
           self.txtuser.get(),
           self.combo_security.get(),
           self.txt_security.get()
                                   )
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = ("UPDATE register SET password=%s WHERE email=%s")
                value = (self.txt_new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with new password", parent=self.root2)
                self.root2.destroy()


    #=================forget password window=================

    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset password", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="jainandan", database="my_data")
                my_cursor = conn.cursor()
                query = ("SELECT * FROM register WHERE email=%s")
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
               # print(row)

                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset password", parent=self.root)
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")
                    l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
                    l.place(x=0, y=10, relwidth=1)
                    security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
                    security_Q.place(x=50, y=80)
                    self.combo_security = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly")
                    self.combo_security["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your School Name")
                    self.combo_security.current(0)
                    self.combo_security.place(x=50, y=110, width=250)
                    security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                    security_A.place(x=50, y=150)
                    self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                    self.txt_security.place(x=50, y=180, width=250)
                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                    new_password.place(x=50, y=220)
                    self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                    self.txt_new_password.place(x=50, y=250, width=250)
                    btn = Button(self.root2, text="Reset Password", command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="green", activebackground="green", activeforeground="white", cursor="hand2")
                    btn.place(x=100, y=300)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
        
    

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition Attendance System")
        
        #==========variables===========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()
        self.var_check = IntVar()


        #==========background image===========

        self.bg = ImageTk.PhotoImage(file=r"D:\project of ai engineer\attendance system\college_images\employee_img2.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1600, height=900)

        #==========left image===========
        self.bg1 = ImageTk.PhotoImage(file=r"D:\project of ai engineer\attendance system\college_images\thought-good-morning-messages-LoveSove.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=50, y=100, width=470, height=550)
        #==========main frame===========
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550) 

            #==========register label==========
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        #==========labels and entry===========
        
        # First Name
        Label(frame, text="First Name", font=("times new roman", 13, "bold"), bg="white").place(x=50, y=100)
        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 13))
        self.txt_fname.place(x=50, y=130, width=250)

       # Last Name
        Label(frame, text="Last Name", font=("times new roman", 13, "bold"), bg="white").place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 13))
        self.txt_lname.place(x=370, y=130, width=250)

       # Contact
        Label(frame, text="Contact No", font=("times new roman", 13, "bold"), bg="white").place(x=50, y=180)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 13))
        self.txt_contact.place(x=50, y=210, width=250)

        # Email
        Label(frame, text="Email", font=("times new roman", 13, "bold"), bg="white").place(x=370, y=180)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 13))
        self.txt_email.place(x=370, y=210, width=250)

       # Security Question
        Label(frame, text="Select Security Questions", font=("times new roman", 13, "bold"), bg="white").place(x=50, y=260)
        self.combo_security = ttk.Combobox(frame, textvariable=self.var_security,font=("times new roman", 13),state="readonly")
        self.combo_security["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your School Name")
        self.combo_security.current(0)
        self.combo_security.place(x=50, y=290, width=250)

         # Answer
        Label(frame, text="Security Answer", font=("times new roman", 13, "bold"), bg="white").place(x=370, y=260)
        self.txt_answer = ttk.Entry(frame, textvariable=self.var_answer, font=("times new roman", 13))
        self.txt_answer.place(x=370, y=290, width=250)

       # Password
        Label(frame, text="Password", font=("times new roman", 13, "bold"), bg="white").place(x=50, y=340)
        self.txt_password = ttk.Entry(frame, textvariable=self.var_password,font=("times new roman", 13), show="*")
        self.txt_password.place(x=50, y=370, width=250)

       # Confirm Password
        Label(frame, text="Confirm Password", font=("times new roman", 13, "bold"), bg="white").place(x=370, y=340)
        self.txt_confirmpassword = ttk.Entry(frame, textvariable=self.var_confirmpassword,font=("times new roman", 13), show="*")
        self.txt_confirmpassword.place(x=370, y=370, width=250)

        # Checkbox
        Checkbutton(frame,
            text="I Agree The Terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,font=("times new roman", 11),bg="white").place(x=50, y=410)
        
        #==========register button==========
        img4=Image.open(r"D:\project of ai engineer\attendance system\college_images\register-now-button1.jpg")
        img4 = img4.resize((200,50), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1_button = Button(frame, image=self.photoimg4, borderwidth=0, command=self.register_data, cursor="hand2")
        b1_button.place(x=50, y=450, width=200, height=50)
        
        img5=Image.open(r"D:\project of ai engineer\attendance system\college_images\loginpng.png")
        img5 = img5.resize((200,50), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2_button = Button(frame, image=self.photoimg5, borderwidth=0, command=self.return_login, cursor="hand2")
        b2_button.place(x=370, y=450, width=200, height=50)

        #==========function declaration==========
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.var_password.get() != self.var_confirmpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="jainandan", database="my_data")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User Already Exists, Please Try Another Email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security.get(),
                    self.var_answer.get(),
                    self.var_password.get()

                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Register Successfully", parent=self.root)

    def return_login(self):
     self.root.destroy()



if __name__ == "__main__":
    main()