from tkinter import *
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        # ================= TITLE =================
        title = Label(self.root, text="DEVELOPER PROFILE",
                      font=("Segoe UI", 30, "bold"),
                      bg="#0a192f", fg="#00ffff")
        title.pack(fill=X)

        # ================= TOP BACKGROUND IMAGE =================
        img_top = Image.open(r"D:\project of ai engineer\attendance system\college_images\developer.png")
        img_top = img_top.resize((1530, 300), Image.Resampling.LANCZOS)
        self.top_img = ImageTk.PhotoImage(img_top)

        bg_label = Label(self.root, image=self.top_img)
        bg_label.place(x=0, y=50, width=1530, height=300)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bg="#0a192f")
        main_frame.place(x=0, y=350, width=1530, height=418)

        # ================= LEFT SIDE (IMAGE) =================
        left_frame = Frame(main_frame, bg="#0a192f")
        left_frame.place(x=100, y=30, width=400, height=350)

        img_dev = Image.open(r"D:\project of ai engineer\attendance system\college_images\Developer Team.jpeg")
        img_dev = img_dev.resize((250, 250), Image.Resampling.LANCZOS)
        self.dev_img = ImageTk.PhotoImage(img_dev)

        dev_label = Label(left_frame, image=self.dev_img, bg="#0a192f", bd=5, relief=RIDGE)
        dev_label.place(x=75, y=20, width=250, height=250)

        name = Label(left_frame, text="Jai Nandan ,Gagandeep Singh, Gagan",
                     font=("Segoe UI", 18, "bold"),
                     bg="#0a192f", fg="#00ffff")
        name.place(x=120, y=290)

        # ================= RIGHT SIDE (INFO) =================
        right_frame = Frame(main_frame, bg="#112240")
        right_frame.place(x=550, y=30, width=800, height=350)

        heading = Label(right_frame,
                        text="About Developer",
                        font=("Segoe UI", 20, "bold"),
                        bg="#112240", fg="#00ffff")
        heading.place(x=20, y=20)

        desc = Label(right_frame,
                     text="Hi, I am Jai Nandan. ,Gagandeep Singh, Gagan \n\n"
                          "I am a passionate Python Developer specializing\n"
                          "in AI-based applications like Face Recognition Systems.\n\n"
                          "I love building smart solutions using:\n"
                          "• Python\n• OpenCV\n• Flask\n• Machine Learning",
                     font=("Segoe UI", 13),
                     bg="#112240", fg="white",
                     justify=LEFT)
        desc.place(x=20, y=80)

        # ================= BOTTOM IMAGE =================
        img_bottom = Image.open(r"D:\project of ai engineer\attendance system\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_bottom = img_bottom.resize((760, 120), Image.Resampling.LANCZOS)
        self.bottom_img = ImageTk.PhotoImage(img_bottom)

        bottom_label = Label(right_frame, image=self.bottom_img, bg="#112240")
        bottom_label.place(x=20, y=220, width=760, height=120)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()