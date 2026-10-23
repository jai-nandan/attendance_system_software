
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import psycopg
import os

from main import Face_Recognition_System


# ================= DATABASE CONFIGURATION =================
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "face_recognizer",
    "user": "postgres",
    "password": "jai5911"
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "college_images")


def db_connect():
    return psycopg.connect(**DB_CONFIG)


def image_path(filename):
    return os.path.join(IMAGE_DIR, filename)


def load_image(filename, size=None):
    path = image_path(filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    img = Image.open(path)

    if size:
        img = img.resize(size, Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(img)


def main():
    root = Tk()
    login(root)
    root.mainloop()


# ================= LOGIN CLASS =================
class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition Attendance System")

        # Banner
        self.frame_banner = Frame(self.root)
        self.frame_banner.place(
            x=0, y=0, width=1550, height=130
        )

        banner_files = [
            "BestFacialRecognition.jpg",
            "facialrecognition.jpg",
            "images.jpg"
        ]

        self.banner_images = []

        for col, filename in enumerate(banner_files):
            try:
                photo = load_image(filename, (516, 130))
                self.banner_images.append(photo)

                Label(
                    self.frame_banner,
                    image=photo
                ).grid(row=0, column=col)

            except Exception as e:
                print("Banner image error:", e)

        # Title
        Label(
            self.root,
            text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 28, "bold"),
            bg="white",
            fg="red"
        ).place(x=0, y=130, width=1550, height=60)

        # Background
        try:
            self.bg = load_image("lo.jpeg", (1550, 610))
            Label(
                self.root,
                image=self.bg
            ).place(x=0, y=190, width=1550, height=610)
        except Exception as e:
            print("Background image error:", e)
            self.root.configure(bg="lightgray")

        # Login frame
        frame = Frame(self.root, bg="black")
        frame.place(
            relx=0.5, rely=0.62, anchor=CENTER,
            width=350, height=450
        )

        # Profile icon
        try:
            self.photoimg1 = load_image(
                "LoginIconAppl.png", (100, 100)
            )
            Label(
                frame,
                image=self.photoimg1,
                bg="black",
                borderwidth=0
            ).place(x=125, y=10, width=100, height=100)
        except Exception as e:
            print("Login icon error:", e)

        Label(
            frame,
            text="Get Started",
            font=("times new roman", 20, "bold"),
            fg="white",
            bg="black"
        ).place(x=95, y=110)

        Label(
            frame, text="Username",
            font=("times new roman", 15, "bold"),
            fg="white", bg="black"
        ).place(x=70, y=155)

        self.txtuser = ttk.Entry(
            frame, font=("times new roman", 15)
        )
        self.txtuser.place(x=70, y=180, width=230)

        Label(
            frame, text="Password",
            font=("times new roman", 15, "bold"),
            fg="white", bg="black"
        ).place(x=70, y=225)

        self.txtpass = ttk.Entry(
            frame, font=("times new roman", 15), show="*"
        )
        self.txtpass.place(x=70, y=250, width=230)

        Button(
            frame,
            text="Login",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="#d90429",
            activebackground="#ef233c",
            cursor="hand2",
            command=self.login
        ).place(x=110, y=300, width=120, height=35)

        Button(
            frame,
            text="New User Register",
            font=("times new roman", 10, "bold"),
            fg="white", bg="black",
            cursor="hand2", borderwidth=0,
            command=self.register_window
        ).place(x=20, y=350)

        Button(
            frame,
            text="Forget Password",
            font=("times new roman", 10, "bold"),
            fg="white", bg="black",
            cursor="hand2", borderwidth=0,
            command=self.forget_password_window
        ).place(x=20, y=380)

    # Login
    def login(self):
        email = self.txtuser.get().strip()
        password = self.txtpass.get()

        if not email or not password:
            messagebox.showerror(
                "Error", "All fields are required",
                parent=self.root
            )
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT 1 FROM register
                        WHERE email = %s AND password = %s
                        """,
                        (email, password)
                    )
                    row = cursor.fetchone()

            if not row:
                messagebox.showerror(
                    "Error", "Invalid email or password",
                    parent=self.root
                )
                return

            if messagebox.askyesno(
                "Admin Access",
                "Open Face Recognition System?",
                parent=self.root
            ):
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(
                    self.new_window
                )

        except Exception as e:
            messagebox.showerror(
                "Database Error", str(e),
                parent=self.root
            )

    # Open registration window
    def register_window(self):
        self.new_window = Toplevel(self.root)
        Register(self.new_window)

    # Forgot password
    def forget_password_window(self):
        email = self.txtuser.get().strip()

        if not email:
            messagebox.showerror(
                "Error", "Enter your email address first",
                parent=self.root
            )
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT 1 FROM register WHERE email = %s",
                        (email,)
                    )
                    row = cursor.fetchone()

            if not row:
                messagebox.showerror(
                    "Error", "Email address not found",
                    parent=self.root
                )
                return

            self.root2 = Toplevel(self.root)
            self.root2.title("Forget Password")
            self.root2.geometry("340x450+610+170")
            self.reset_email = email

            Label(
                self.root2,
                text="Forget Password",
                font=("times new roman", 20, "bold"),
                fg="darkgreen", bg="white"
            ).place(x=0, y=10, relwidth=1)

            Label(
                self.root2, text="Security Question",
                font=("times new roman", 13, "bold")
            ).place(x=50, y=80)

            self.combo_security = ttk.Combobox(
                self.root2,
                font=("times new roman", 12),
                state="readonly",
                values=[
                    "Your Birth Place",
                    "Your Pet Name",
                    "Your School Name"
                ]
            )
            self.combo_security.place(x=50, y=110, width=250)
            self.combo_security.current(0)

            Label(
                self.root2, text="Security Answer",
                font=("times new roman", 13, "bold")
            ).place(x=50, y=155)

            self.txt_security = ttk.Entry(
                self.root2, font=("times new roman", 13)
            )
            self.txt_security.place(x=50, y=185, width=250)

            Label(
                self.root2, text="New Password",
                font=("times new roman", 13, "bold")
            ).place(x=50, y=230)

            self.txt_new_password = ttk.Entry(
                self.root2, font=("times new roman", 13),
                show="*"
            )
            self.txt_new_password.place(
                x=50, y=260, width=250
            )

            Button(
                self.root2,
                text="Reset Password",
                command=self.reset_pass,
                font=("times new roman", 13, "bold"),
                fg="white", bg="green",
                cursor="hand2"
            ).place(x=85, y=320)

        except Exception as e:
            messagebox.showerror(
                "Database Error", str(e),
                parent=self.root
            )

    def reset_pass(self):
        question = self.combo_security.get()
        answer = self.txt_security.get().strip()
        new_password = self.txt_new_password.get()

        if not question or not answer or not new_password:
            messagebox.showerror(
                "Error", "Please complete all fields",
                parent=self.root2
            )
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT 1 FROM register
                        WHERE email = %s
                          AND security = %s
                          AND answer = %s
                        """,
                        (self.reset_email, question, answer)
                    )

                    if not cursor.fetchone():
                        messagebox.showerror(
                            "Error",
                            "Incorrect security answer",
                            parent=self.root2
                        )
                        return

                    cursor.execute(
                        """
                        UPDATE register
                        SET password = %s
                        WHERE email = %s
                        """,
                        (new_password, self.reset_email)
                    )

            self.txtpass.delete(0, END)
            self.root2.destroy()

            messagebox.showinfo(
                "Success",
                "Password reset successfully. Please log in again.",
                parent=self.root
            )

        except Exception as e:
            messagebox.showerror(
                "Database Error", str(e),
                parent=self.root2
            )


# ================= REGISTRATION CLASS =================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+100+50")
        self.root.title("User Registration")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()
        self.var_check = IntVar()

        self.root.configure(bg="white")

        # Optional background image
        try:
            self.bg = load_image(
                "employee_img2.jpg", (1350, 750)
            )
            Label(
                self.root, image=self.bg
            ).place(x=0, y=0, width=1350, height=750)
        except Exception as e:
            print("Registration background image error:", e)

        frame = Frame(self.root, bg="white")
        frame.place(x=220, y=70, width=900, height=610)

        Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 22, "bold"),
            fg="darkgreen", bg="white"
        ).place(x=30, y=20)

        Label(
            frame, text="First Name", bg="white"
        ).place(x=50, y=90)

        self.txt_fname = ttk.Entry(
            frame, textvariable=self.var_fname
        )
        self.txt_fname.place(x=50, y=115, width=300)

        Label(
            frame, text="Last Name", bg="white"
        ).place(x=450, y=90)

        ttk.Entry(
            frame, textvariable=self.var_lname
        ).place(x=450, y=115, width=300)

        Label(
            frame, text="Contact No", bg="white"
        ).place(x=50, y=165)

        ttk.Entry(
            frame, textvariable=self.var_contact
        ).place(x=50, y=190, width=300)

        Label(
            frame, text="Email", bg="white"
        ).place(x=450, y=165)

        ttk.Entry(
            frame, textvariable=self.var_email
        ).place(x=450, y=190, width=300)

        Label(
            frame, text="Security Question", bg="white"
        ).place(x=50, y=240)

        self.combo_security = ttk.Combobox(
            frame,
            textvariable=self.var_security,
            state="readonly",
            values=[
                "Select",
                "Your Birth Place",
                "Your Pet Name",
                "Your School Name"
            ]
        )
        self.combo_security.current(0)
        self.combo_security.place(x=50, y=265, width=300)

        Label(
            frame, text="Security Answer", bg="white"
        ).place(x=450, y=240)

        ttk.Entry(
            frame, textvariable=self.var_answer
        ).place(x=450, y=265, width=300)

        Label(
            frame, text="Password", bg="white"
        ).place(x=50, y=315)

        ttk.Entry(
            frame, textvariable=self.var_password,
            show="*"
        ).place(x=50, y=340, width=300)

        Label(
            frame, text="Confirm Password", bg="white"
        ).place(x=450, y=315)

        ttk.Entry(
            frame, textvariable=self.var_confirmpassword,
            show="*"
        ).place(x=450, y=340, width=300)

        Checkbutton(
            frame,
            text="I Agree to the Terms & Conditions",
            variable=self.var_check,
            onvalue=1, offvalue=0,
            bg="white"
        ).place(x=50, y=395)

        Button(
            frame,
            text="Register",
            font=("times new roman", 14, "bold"),
            bg="green", fg="white",
            cursor="hand2",
            command=self.register_data
        ).place(x=100, y=460, width=200, height=45)

        Button(
            frame,
            text="Close",
            font=("times new roman", 14, "bold"),
            bg="#d90429", fg="white",
            cursor="hand2",
            command=self.root.destroy
        ).place(x=450, y=460, width=200, height=45)

    def register_data(self):
        fname = self.var_fname.get().strip()
        lname = self.var_lname.get().strip()
        contact = self.var_contact.get().strip()
        email = self.var_email.get().strip()
        security = self.var_security.get()
        answer = self.var_answer.get().strip()
        password = self.var_password.get()
        confirm = self.var_confirmpassword.get()

        if not all([
            fname, email, security, answer, password, confirm
        ]) or security == "Select":
            messagebox.showerror(
                "Error", "Please fill in all required fields",
                parent=self.root
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error", "Passwords do not match",
                parent=self.root
            )
            return

        if self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree to the terms",
                parent=self.root
            )
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT 1 FROM register WHERE email = %s",
                        (email,)
                    )

                    if cursor.fetchone():
                        messagebox.showerror(
                            "Error",
                            "This email is already registered",
                            parent=self.root
                        )
                        return

                    cursor.execute(
                        """
                        INSERT INTO register
                        (fname, lname, contact, email,
                         security, answer, password)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            fname, lname, contact, email,
                            security, answer, password
                        )
                    )

            messagebox.showinfo(
                "Success", "Registration successful",
                parent=self.root
            )
            self.root.destroy()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e),
                parent=self.root
            )


if __name__ == "__main__":
    main()
