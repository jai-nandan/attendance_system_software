from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recogition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help_me import Help_Support


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition Attendance System")

        # ================= HEADER IMAGES =================

        img = Image.open(r"D:\project of ai engineer\attendance system\college_images\BestFacialRecognition.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"D:\project of ai engineer\attendance system\college_images\facialrecognition.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"D:\project of ai engineer\attendance system\college_images\images.jpg")
        width, height = img2.size
        img2 = img2.crop((0, 0, width - 120, height))
        img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb3 = Label(self.root, image=self.photoimg2, borderwidth=0)
        f_lb3.place(x=1000, y=0)

        # ================= BACKGROUND =================

        img3 = Image.open(r"D:\project of ai engineer\attendance system\college_images\background.png")
        img3 = img3.resize((1530, 768), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=638)

        title_lb1 = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("new times roman", 35, "bold"),
                          bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # ================= BUTTON CREATION FUNCTION =================

        def create_button(img_path, text, x, y, command):
            img_btn = Image.open(img_path)
            img_btn = img_btn.resize((220, 220), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img_btn)

            btn1 = Button(bg_img, image=photo, cursor="hand2", command=command)
            btn1.image = photo
            btn1.place(x=x, y=y, width=220, height=220)

            btn2 = Button(bg_img, text=text, cursor="hand2",
                          font=("new times roman", 15, "bold"),
                          bg="darkblue", fg="white",
                          command=command)
            btn2.place(x=x, y=y + 220, width=220, height=40)

        # ================= BUTTONS =================

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\Gemini_Generated_Image_vrubbkvrubbkvrub.png",
            "Student Panel", 200, 100, self.student_details)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\face_dector.png",
            "Face Detector", 500, 100, self.face_detector)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\report.jpg",
            "Attendance", 800, 100, self.attendance)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\Gemini_Generated_Image_bvxwe7bvxwe7bvxw.png",
            "Help Support", 1100, 100, self.help_support)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\Train.jpg",
            "Data Train", 200, 380, self.train_data)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\sample.jpg",
            "Photo Sample", 500, 380, self.photo_sample)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\developer.png",
            "Developers", 800, 380, self.developers)

        create_button(
            r"D:\project of ai engineer\attendance system\college_images\Gemini_Generated_Image_clsy5clsy5clsy5c.png",
            "Exit", 1100, 380, self.iExit)
        def open_image(self):
            os.startfile("data")

        
    # ================= FUNCTIONS =================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_support(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_Support(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def photo_sample(self):
     path = "D:/project of ai engineer/attendance system/data"

     if not os.path.exists(path):
         os.makedirs(path)

     os.startfile(path)
   

    def developers(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def iExit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()