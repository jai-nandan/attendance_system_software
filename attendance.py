from tkinter import *
from tkinter import ttk
from unittest import result
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


file_path = "Attendance.csv"
mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        #========varibales========
        self.var_attendance_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()

         #===== Header IMAGE=====
        img_right = Image.open(r"D:\project of ai engineer\attendance system\college_images\gettyimages-1022573162.jpg")
        img_right = img_right.resize((800,130), Image.Resampling.LANCZOS)
        self.header_right = ImageTk.PhotoImage(img_right)

        right_lbl = Label(self.root, image=self.header_right)
        right_lbl.place(x=0, y=0, width=800, height=130)

        img_left = Image.open(r"D:\project of ai engineer\attendance system\college_images\smart-attendance.jpg")
        img_left = img_left.resize((800, 130), Image.Resampling.LANCZOS)
        self.header_left = ImageTk.PhotoImage(img_left)

        left_lbl = Label(self.root, image=self.header_left)
        left_lbl.place(x=800, y=0, width=800, height=130)

        #===== BACKGROUND IMAGE =====
        bg_img = Image.open(r"D:\project of ai engineer\attendance system\college_images\background.png")
        bg_img = bg_img.resize((1530, 768), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=130, width=1530, height=638)

        #===== TITLE =====
        Label(bg_label,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"),bg="white",fg="blue").place(x=0, y=0, width=1530, height=45)

        #========Main Frame =====
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=580)    

        #==========Left Frame ======
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance", font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=10, width=730, height=560)

        img_left = Image.open(r"D:\project of ai engineer\attendance system\college_images\attendance.png")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_left)
        left_lbl = Label(left_frame, image=self.photo_left)
        left_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=0, y=135, width=720, height=400)

        #========Attendance Id========
        Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_attendance_id,width=20, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #========Student Name========
        Label(left_inside_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #========Date========
        Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_date, width=20, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #========Department=====
        Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_department, width=20, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #========Time========
        Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_time, width=20, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #========Attendance========
        Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_attendance_status, width=20, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W) 

        #======attendance Status========
        Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.attendance_status_entry = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.attendance_status_entry["values"] = ("Present", "Absent")
        self.attendance_status_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.attendance_status_entry.current(0)

        #=======Buttons========
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.importcsv, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19).grid(row=0, column=0, padx=1)
        Button(btn_frame, text="Export CSV", command=self.exportcsv, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19).grid(row=0, column=1, padx=1)
        Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19).grid(row=0, column=2, padx=1)
        Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19).grid(row=0, column=3, padx=1)

        #==========Right Frame ======
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=560)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=710, height=540)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,
            column=("id","name","roll","department","time","date","attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance Status")

        self.attendance_table["show"] = "headings"
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

        # AUTO LOAD DATA
        self.importcsv()

    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    def importcsv(self):
        global mydata
        mydata.clear()

        if not os.path.exists(file_path):
            return

        with open(file_path) as myfile:
            csvread = csv.reader(myfile)
            for i in csvread:
                mydata.append(i)

        self.fetch_data(mydata)

    def exportcsv(self):
        with open(file_path, mode="w", newline="") as myfile:
            csvwrite = csv.writer(myfile)
            for i in mydata:
                csvwrite.writerow(i)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        data = content["values"]

        self.var_attendance_id.set(data[0])
        self.var_name.set(data[1])
        self.var_roll.set(data[2])
        self.var_department.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_attendance_status.set(data[6])

    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")

    def update_data(self):
        for i in mydata:
            if i[0] == self.var_attendance_id.get():
                i[1] = self.var_name.get()
                i[2] = self.var_roll.get()
                i[3] = self.var_department.get()
                i[4] = self.var_time.get()
                i[5] = self.var_date.get()
                i[6] = self.var_attendance_status.get()
                break

        self.fetch_data(mydata)
        self.exportcsv()
        messagebox.showinfo("Success", "Updated Successfully", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()