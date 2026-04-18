from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")


        #========variables========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        # ================= HEADER IMAGES =================
        self.load_header_images()

        # ================= BACKGROUND =================
        bg_img = Image.open(r"D:\project of ai engineer\attendance system\college_images\background.png")
        bg_img = bg_img.resize((1530, 768), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=130, width=1530, height=638)

        # ================= TITLE =================
        Label(bg_label,
              text="STUDENT MANAGEMENT SYSTEM",
              font=("times new roman", 35, "bold"),
              bg="white",
              fg="blue").place(x=0, y=0, width=1530, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=580)

        # ================= LEFT FRAME =================
        left_frame = LabelFrame(main_frame, bd=2, bg="white",
                                relief=RIDGE,
                                text="Student Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=10, width=730, height=560)
        self.build_left_section(left_frame)

        # ================= RIGHT FRAME =================
        right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                 relief=RIDGE,
                                 text="Student Records",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=560)
        self.build_right_section(right_frame)

    # ======================================================
    # HEADER IMAGES
    # ======================================================
    def load_header_images(self):
        img = Image.open(r"D:\project of ai engineer\attendance system\college_images\face-recognition.png")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photo1).place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"D:\project of ai engineer\attendance system\college_images\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photo2).place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"D:\project of ai engineer\attendance system\college_images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((530, 130), Image.Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photo3).place(x=1000, y=0, width=530, height=130)

    # ======================================================
    # LEFT SECTION
    # ======================================================
    def build_left_section(self, parent):
        # Top Image
        img_left = Image.open(r"D:\project of ai engineer\attendance system\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((710, 130), Image.Resampling.LANCZOS)
        self.left_img = ImageTk.PhotoImage(img_left)
        Label(parent, image=self.left_img).place(x=0, y=0, width=710, height=130)

        # ================= COURSE FRAME =================
        course_frame = LabelFrame(parent, bd=2, bg="white",
                                  relief=RIDGE,
                                  text="Current Course Information",
                                  font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=140, width=710, height=120)

        Label(course_frame, text="Department", bg="white",
              font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(course_frame, textvariable=self.var_dep,
             values=("Select Department", "B.Tech", "M.Tech", "PhD"),
             state="readonly", width=18).grid(row=0, column=1)

        Label(course_frame, text="Course", bg="white",
              font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, sticky=W)
        ttk.Combobox(course_frame, textvariable=self.var_course,
             values=("Select Course", "CSE", "EEE", "ME"),
             state="readonly", width=18).grid(row=0, column=3)
      

        Label(course_frame, text="Year", bg="white",
              font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(course_frame, textvariable=self.var_year,
             values=("Select Year", "2021","2020", "2021", "2022" ,"2023", "2024", "2025", "2026"),
             state="readonly", width=18).grid(row=1, column=1)

        Label(course_frame, text="Semester", bg="white",
      font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=10, sticky=W)

        ttk.Combobox(course_frame, textvariable=self.var_semester,
           values=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8"),
           state="readonly", width=18).grid(row=1, column=3)
        # ================= SCROLLABLE STUDENT INFO =================
        info_container = LabelFrame(parent, bd=2, bg="white",
                                    relief=RIDGE,
                                    text="Student Information",
                                    font=("times new roman", 12, "bold"))
        info_container.place(x=5, y=270, width=710, height=270)

        canvas = Canvas(info_container, bg="white")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(info_container, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        info_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=info_frame, anchor="nw")

        info_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # Grid layout inside scroll
        for i in range(4):
            info_frame.columnconfigure(i, weight=1)

        # Row 0
        Label(info_frame, text="Student ID:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_std_id).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        Label(info_frame, text="Student Name:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_std_name).grid(row=0, column=3, padx=10, pady=5, sticky="ew")

        # Row 1
        Label(info_frame, text="Division:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(info_frame, textvariable=self.var_div, values=("A", "B", "C"), state="readonly").grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        Label(info_frame, text="Roll No:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_roll).grid(row=1, column=3, padx=10, pady=5, sticky="ew")

        # Row 2
        Label(info_frame, text="Gender:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(info_frame, textvariable=self.var_gender, values=("Male", "Female", "Other"), state="readonly").grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        Label(info_frame, text="DOB:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_dob).grid(row=2, column=3, padx=10, pady=5, sticky="ew")

        # Row 3
        Label(info_frame, text="Email:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_email).grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        Label(info_frame, text="Phone:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=3, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_phone).grid(row=3, column=3, padx=10, pady=5, sticky="ew")

        # Row 4
        Label(info_frame, text="Address:", bg="white",
              font=("times new roman", 12, "bold")).grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(info_frame, textvariable=self.var_address).grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Radio buttons
        self.photo_var = IntVar()
        Radiobutton(info_frame, text="Take Photo Sample", variable=self.photo_var, value=1, bg="white").grid(row=5, column=0, pady=10, sticky=W)
        Radiobutton(info_frame, text="No Photo Sample", variable=self.photo_var, value=2, bg="white").grid(row=5, column=1, sticky=W)

        # Buttons
        btn_frame = Frame(info_frame, bg="white")
        btn_frame.grid(row=6, column=0, columnspan=4, pady=10)

        Button(btn_frame, text="Save",  command=self.add_data, width=15, bg="blue", fg="white").grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update", command=self.update_data,width=15, bg="blue", fg="white").grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete",  command=self.delete_data, width=15, bg="blue", fg="white").grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset",   command=self.reset_data, width=15, bg="blue", fg="white").grid(row=0, column=3, padx=5)
        Button(btn_frame, text="Take Photo",command=self.generate_dataset,   width=15, bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
        Button(btn_frame, text="Update Photo", command=self.update_photo, width=15, bg="blue", fg="white").grid(row=1, column=1, padx=5, pady=5)
       

    # ======================================================
    # RIGHT SECTION
    # ======================================================
    def build_right_section(self, parent):
    # Top Image
      img_right = Image.open(r"D:\project of ai engineer\attendance system\college_images\gettyimages-1022573162.jpg")
      img_right = img_right.resize((710, 130), Image.Resampling.LANCZOS)
      self.right_img = ImageTk.PhotoImage(img_right)
      Label(parent, image=self.right_img).place(x=0, y=0, width=710, height=130)

    # ================= SEARCH FRAME =================
      search_frame = LabelFrame(parent, bd=2, bg="white", relief=RIDGE, 
                              text="Search System", font=("times new roman", 12, "bold"))
      search_frame.place(x=5, y=140, width=705, height=70)

      Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=5, pady=5, sticky=W)

      self.search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15,
                                     values=("Roll_No", "Phone_No", "StudentID"))
      self.search_combo.grid(row=0, column=1, padx=5, pady=5)
      self.search_combo.current(0)

      self.search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
      self.search_entry.grid(row=0, column=2, padx=5, pady=5)

      Button(search_frame, text="Search", font=("arial", 11, "bold"), bg="blue", fg="white", width=10).grid(row=0, column=3, padx=5)
      Button(search_frame, text="Show All", font=("arial", 11, "bold"), bg="blue", fg="white", width=10).grid(row=0, column=4, padx=5)

    # ================= TABLE FRAME =================
      table_frame = Frame(parent, bd=2, bg="white", relief=RIDGE)
      table_frame.place(x=5, y=220, width=705, height=320)

      scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
      self.student_table = ttk.Treeview(table_frame,
          columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set)
    # ================= TABLE HEADINGS =================
      self.student_table.heading("dep", text="Department")
      self.student_table.heading("course", text="Course")
      self.student_table.heading("year", text="Year")
      self.student_table.heading("sem", text="Semester")
      self.student_table.heading("id", text="ID")
      self.student_table.heading("name", text="Name")
      self.student_table.heading("div", text="Division")
      self.student_table.heading("roll", text="Roll No")
      self.student_table.heading("gender", text="Gender")
      self.student_table.heading("dob", text="DOB")
      self.student_table.heading("email", text="Email")
      self.student_table.heading("phone", text="Phone")
      self.student_table.heading("address", text="Address")
      self.student_table.heading("teacher", text="Teacher")
      self.student_table.heading("photo", text="Photo")

      self.student_table["show"] = "headings"  # Remove empty first column

    # Column Widths
      self.student_table.column("dep", width=100)
      self.student_table.column("course", width=100)
      self.student_table.column("year", width=80)
      self.student_table.column("sem", width=80)
      self.student_table.column("id", width=100)
      self.student_table.column("name", width=120)
      self.student_table.column("div", width=80)
      self.student_table.column("roll", width=100)
      self.student_table.column("gender", width=100)
      self.student_table.column("dob", width=100)
      self.student_table.column("email", width=150)
      self.student_table.column("phone", width=120)
      self.student_table.column("address", width=150)
      self.student_table.column("teacher", width=120)
      self.student_table.column("photo", width=80)

      self.student_table.pack(fill=BOTH, expand=1)
      self.student_table.bind("<ButtonRelease>", self.get_cursor)
      self.fetch_data()  # Load data when initializing


     #===================== BUTTON FUNCTION =================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or \
           self.var_course.get()=="Select Course" or \
           self.var_year.get()=="Select Year" or \
           self.var_semester.get()=="Select Semester" or \
           self.var_std_id.get()=="" or \
           self.var_std_name.get()=="" or \
           self.var_div.get()=="" or \
           self.var_roll.get()=="" or \
           self.var_gender.get()=="" or \
           self.var_dob.get()=="" or \
           self.var_email.get()=="" or \
           self.var_phone.get()=="" or \
           self.var_address.get()=="":

            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    username='root',
                    password='jainandan',
                    host='localhost',
                    database='attendancesystem',
                    port=3306
                )

                mycursor = conn.cursor()

                mycursor.execute(
    "INSERT INTO student (DEPARTMENT, COURCE, YEAR, SEMESTER, STUDENT_ID, NAME, DIVISION, ROLL, GENDER, DOB, EMAIL, PHONE, ADDRESS, TEACHER, PHOTO_SAMPLE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (
        self.var_dep.get(),        # DEPARTMENT
        self.var_course.get(),     # COURSE
        self.var_year.get(),       # YEAR
        self.var_semester.get(),   # SEMESTER
        self.var_std_id.get(),     # STUDENT_ID
        self.var_std_name.get(),   # NAME
        self.var_div.get(),        # DIVISION
        self.var_roll.get(),       # ROLL
        self.var_gender.get(),     # GENDER
        self.var_dob.get(),        # DOB
        self.var_email.get(),      # EMAIL
        self.var_phone.get(),      # PHONE
        self.var_address.get(),    # ADDRESS
        self.var_teacher.get(),    # TEACHER
        self.photo_var.get()       # PHOTO_SAMPLE
    )
)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)

            except Exception as es:
                print("ERROR:", es)
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # ==================== FETCH DATA ====================
    def fetch_data(self):
        conn = mysql.connector.connect(
            username='root',
            password='jainandan',
            host='localhost',
            database='attendancesystem',
            port=3306
        )

        mycursor = conn.cursor()
        mycursor.execute("""SELECT DEPARTMENT, COURCE, YEAR, SEMESTER, STUDENT_ID, NAME, DIVISION, ROLL, GENDER, DOB, EMAIL, PHONE, ADDRESS, TEACHER, PHOTO_SAMPLE FROM student""")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=(
            i[0],   # DEPARTMENT
            i[1],   # COURSE
           i[2],   # YEAR
           i[3],   # SEMESTER
           i[4],   # STUDENT_ID
           i[5],   # NAME
           i[6],   # DIVISION
           i[7],   # ROLL
           i[8],   # GENDER
           i[9],   # DOB
           i[10],  # EMAIL
           i[11],  # PHONE
           i[12],  # ADDRESS
           i[13],  # TEACHER
           i[14]   # PHOTO_SAMPLE
            ))

            conn.commit()

        conn.close()
        #=====================get cursor data====================
    def get_cursor(self, event=""):
     cursor_focus = self.student_table.focus()
     content = self.student_table.item(cursor_focus)
     data = content["values"]

     if data:
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

      #====================update data======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or \
           self.var_course.get()=="Select Course" or \
           self.var_year.get()=="Select Year" or \
           self.var_semester.get()=="Select Semester" or \
           self.var_std_id.get()=="" or \
           self.var_std_name.get()=="" or \
           self.var_div.get()=="" or \
           self.var_roll.get()=="" or \
           self.var_gender.get()=="" or \
           self.var_dob.get()=="" or \
           self.var_email.get()=="" or \
           self.var_phone.get()=="" or \
           self.var_address.get()=="":

            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student record?", parent=self.root)
                if update > 0:     
                    conn = mysql.connector.connect(
                        username='root',
                        password='jainandan',
                        host='localhost',
                        database='attendancesystem',
                        port=3306
                    )

                    mycursor = conn.cursor()
                    mycursor.execute("""
                        UPDATE student SET DEPARTMENT=%s, COURCE=%s, YEAR=%s, SEMESTER=%s, NAME=%s, DIVISION=%s, ROLL=%s, GENDER=%s, DOB=%s, EMAIL=%s, PHONE=%s, ADDRESS=%s, TEACHER=%s, PHOTO_SAMPLE=%s WHERE STUDENT_ID=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),   
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.photo_var.get(),
                        self.var_std_id.get()
                    ))
                else:
                        if not update:
                            return
                messagebox.showinfo("Success","Student record successfully updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                print("ERROR:", es)
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
      #===============delete data======================
    def delete_data(self):
            if self.var_std_id.get()=="":
                  messagebox.showerror("Error","Student ID must be required", parent=self.root)
            else:
                  try:
                   delete = messagebox.askyesno("Delete", "Do you want to delete this student record?", parent=self.root)
                   if delete > 0:
                        conn = mysql.connector.connect(
                              username='root',
                              password='jainandan',
                              host='localhost',
                              database='attendancesystem',
                              port=3306
                        )
      
                        mycursor = conn.cursor()
                        sql = "DELETE FROM student WHERE STUDENT_ID=%s"
                        val = (self.var_std_id.get(),)
                        mycursor.execute(sql, val)
                   else:
                        if not delete:
                              return
                   messagebox.showinfo("Success","Student record successfully deleted!", parent=self.root)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                  except Exception as es:
                   print("ERROR:", es)
                   messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        
      #====================reset data======================
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("")
            self.var_roll.set("")
            self.var_gender.set("")
            self.var_dob.set("")   
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.photo_var.set(0)

    #===================generate dataset and take photo samples====================== 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or \
           self.var_course.get()=="Select Course" or \
           self.var_year.get()=="Select Year" or \
           self.var_semester.get()=="Select Semester" or \
           self.var_std_id.get()=="" or \
           self.var_std_name.get()=="" or \
           self.var_div.get()=="" or \
           self.var_roll.get()=="" or \
           self.var_gender.get()=="" or \
           self.var_dob.get()=="" or \
           self.var_email.get()=="" or \
           self.var_phone.get()=="" or \
           self.var_address.get()=="":

            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)

        else:
            try:
                     
                    conn = mysql.connector.connect(
                        username='root',
                        password='jainandan',
                        host='localhost',
                        database='attendancesystem',
                        port=3306
                    )

                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM student WHERE STUDENT_ID=%s", (self.var_std_id.get(),))
                    result = mycursor.fetchone()

                    if result is None:
                       messagebox.showerror("Error", "Student not found!", parent=self.root)
                       return
                    
                    
                    
                    
  
                    id = result[4]   # correct index for STUDENT_ID
                    mycursor.execute("""
                        UPDATE student SET DEPARTMENT=%s, COURCE=%s, YEAR=%s, SEMESTER=%s, NAME=%s, DIVISION=%s, ROLL=%s, GENDER=%s, DOB=%s, EMAIL=%s, PHONE=%s, ADDRESS=%s, TEACHER=%s, PHOTO_SAMPLE=%s WHERE STUDENT_ID=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),   
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.photo_var.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()  
                    self.reset_data()
                    conn.close()
                    #===============load predefined data on face frontals from opencv=============
                    face_classifier = cv2.CascadeClassifier("D:/project of ai engineer/attendance system/haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                     if len(faces) == 0:
                      return None

                     for (x,y,w,h) in faces:
                      return img[y:y+h, x:x+w]
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!", parent=self.root)
            except Exception as es:
                    print("ERROR:", es)
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  

            #===============update photo sample status in database================
    def update_photo(self):
             if self.var_std_id.get()=="":
              messagebox.showerror("Error","Student ID must be required", parent=self.root)
             else:
                try:
                  conn = mysql.connector.connect(username='root',password='jainandan',host='localhost',database='attendancesystem',port=3306)

                  mycursor = conn.cursor()
                  mycursor.execute(
                 "UPDATE student SET PHOTO_SAMPLE=%s WHERE STUDENT_ID=%s",
                 (self.photo_var.get(), self.var_std_id.get()))

                  conn.commit()
                  self.fetch_data()
                  conn.close()

                  messagebox.showinfo("Success","Photo sample updated!", parent=self.root)
                except Exception as es:
                 print("ERROR:", es)
                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


           
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()