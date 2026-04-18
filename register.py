from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


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

        self.bg = ImageTk.PhotoImage(file=r"D:\project of ai engineer\attendance system\college_images\hackers2.jpg")
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
        b2_button = Button(frame, image=self.photoimg5, borderwidth=0, cursor="hand2")
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





if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()