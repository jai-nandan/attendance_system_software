
import os
import tkinter as tk
from tkinter import ttk, messagebox

import cv2
import psycopg
from PIL import Image, ImageTk


# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "college_images")
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)


def db_connect():
    """Connect to the PostgreSQL database."""
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="face_recognizer",
        user="postgres",
        password="jai5911"
    )


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_std_id = tk.StringVar()
        self.var_std_name = tk.StringVar()
        self.var_div = tk.StringVar()
        self.var_roll = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_teacher = tk.StringVar()
        self.photo_var = tk.IntVar(value=0)

        self.load_header_images()

        bg_img = self.load_image("background.png", (1530, 768))
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=130, width=1530, height=638)

        tk.Label(
            bg_label,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue"
        ).place(x=0, y=0, width=1530, height=45)

        main_frame = tk.Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=580)

        left_frame = tk.LabelFrame(
            main_frame, bd=2, bg="white", relief=tk.RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold")
        )
        left_frame.place(x=5, y=10, width=730, height=560)
        self.build_left_section(left_frame)

        right_frame = tk.LabelFrame(
            main_frame, bd=2, bg="white", relief=tk.RIDGE,
            text="Student Records",
            font=("times new roman", 12, "bold")
        )
        right_frame.place(x=750, y=10, width=720, height=560)
        self.build_right_section(right_frame)

    # --------------------------------------------------
    # IMAGE HELPERS
    # --------------------------------------------------
    def load_image(self, filename, size):
        path = os.path.join(IMAGE_DIR, filename)

        if not os.path.isfile(path):
            raise FileNotFoundError(
                f"Image not found:\n{path}\n"
                "Please check the filename in college_images."
            )

        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return img

    def load_header_images(self):
        img = self.load_image("face-recognition.png", (500, 130))
        self.photo1 = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.photo1).place(
            x=0, y=0, width=500, height=130
        )

        img = self.load_image("smart-attendance.jpg", (500, 130))
        self.photo2 = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.photo2).place(
            x=500, y=0, width=500, height=130
        )

        img = self.load_image(
            "iStock-182059956_18390_t12.jpg", (530, 130)
        )
        self.photo3 = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.photo3).place(
            x=1000, y=0, width=530, height=130
        )

    # --------------------------------------------------
    # LEFT SECTION
    # --------------------------------------------------
    def build_left_section(self, parent):
        img = self.load_image("AdobeStock_303989091.jpeg", (710, 130))
        self.left_img = ImageTk.PhotoImage(img)
        tk.Label(parent, image=self.left_img).place(
            x=0, y=0, width=710, height=130
        )

        course_frame = tk.LabelFrame(
            parent, bd=2, bg="white", relief=tk.RIDGE,
            text="Current Course Information",
            font=("times new roman", 12, "bold")
        )
        course_frame.place(x=5, y=140, width=710, height=120)

        tk.Label(
            course_frame, text="Department", bg="white",
            font=("times new roman", 12, "bold")
        ).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        ttk.Combobox(
            course_frame, textvariable=self.var_dep,
            values=("Select Department", "B.Tech", "M.Tech", "PhD"),
            state="readonly", width=18
        ).grid(row=0, column=1)

        tk.Label(
            course_frame, text="Course", bg="white",
            font=("times new roman", 12, "bold")
        ).grid(row=0, column=2, padx=10, sticky=tk.W)

        ttk.Combobox(
            course_frame, textvariable=self.var_course,
            values=("Select Course", "CSE", "EEE", "ME"),
            state="readonly", width=18
        ).grid(row=0, column=3)

        tk.Label(
            course_frame, text="Year", bg="white",
            font=("times new roman", 12, "bold")
        ).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        ttk.Combobox(
            course_frame, textvariable=self.var_year,
            values=(
                "Select Year", "2020", "2021", "2022",
                "2023", "2024", "2025", "2026"
            ),
            state="readonly", width=18
        ).grid(row=1, column=1)

        tk.Label(
            course_frame, text="Semester", bg="white",
            font=("times new roman", 12, "bold")
        ).grid(row=1, column=2, padx=10, sticky=tk.W)

        ttk.Combobox(
            course_frame, textvariable=self.var_semester,
            values=(
                "Select Semester", "1", "2", "3", "4",
                "5", "6", "7", "8"
            ),
            state="readonly", width=18
        ).grid(row=1, column=3)

        info_container = tk.LabelFrame(
            parent, bd=2, bg="white", relief=tk.RIDGE,
            text="Student Information",
            font=("times new roman", 12, "bold")
        )
        info_container.place(x=5, y=270, width=710, height=270)

        canvas = tk.Canvas(info_container, bg="white")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(
            info_container, orient=tk.VERTICAL, command=canvas.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        info_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=info_frame, anchor="nw")

        info_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.bind_all(
            "<MouseWheel>",
            lambda event: canvas.yview_scroll(
                int(-1 * (event.delta / 120)), "units"
            )
        )

        fields = [
            ("Student ID:", self.var_std_id),
            ("Student Name:", self.var_std_name),
            ("Division:", self.var_div),
            ("Roll No:", self.var_roll),
            ("Gender:", self.var_gender),
            ("DOB:", self.var_dob),
            ("Email:", self.var_email),
            ("Phone:", self.var_phone),
            ("Address:", self.var_address),
        ]

        for col in range(4):
            info_frame.columnconfigure(col, weight=1)

        def add_label(row, col, text):
            tk.Label(
                info_frame, text=text, bg="white",
                font=("times new roman", 12, "bold")
            ).grid(row=row, column=col, padx=10, pady=5, sticky=tk.W)

        def add_entry(row, col, variable):
            ttk.Entry(
                info_frame, textvariable=variable
            ).grid(row=row, column=col, padx=10, pady=5, sticky="ew")

        add_label(0, 0, "Student ID:")
        add_entry(0, 1, self.var_std_id)
        add_label(0, 2, "Student Name:")
        add_entry(0, 3, self.var_std_name)

        add_label(1, 0, "Division:")
        ttk.Combobox(
            info_frame, textvariable=self.var_div,
            values=("A", "B", "C"), state="readonly"
        ).grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        add_label(1, 2, "Roll No:")
        add_entry(1, 3, self.var_roll)

        add_label(2, 0, "Gender:")
        ttk.Combobox(
            info_frame, textvariable=self.var_gender,
            values=("Male", "Female", "Other"), state="readonly"
        ).grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        add_label(2, 2, "DOB:")
        add_entry(2, 3, self.var_dob)

        add_label(3, 0, "Email:")
        add_entry(3, 1, self.var_email)
        add_label(3, 2, "Phone:")
        add_entry(3, 3, self.var_phone)

        add_label(4, 0, "Address:")
        ttk.Entry(
            info_frame, textvariable=self.var_address
        ).grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        tk.Radiobutton(
            info_frame, text="Take Photo Sample",
            variable=self.photo_var, value=1, bg="white"
        ).grid(row=5, column=0, pady=10, sticky=tk.W)

        tk.Radiobutton(
            info_frame, text="No Photo Sample",
            variable=self.photo_var, value=0, bg="white"
        ).grid(row=5, column=1, sticky=tk.W)

        btn_frame = tk.Frame(info_frame, bg="white")
        btn_frame.grid(row=6, column=0, columnspan=4, pady=10)

        buttons = [
            ("Save", self.add_data),
            ("Update", self.update_data),
            ("Delete", self.delete_data),
            ("Reset", self.reset_data),
            ("Take Photo", self.generate_dataset),
            ("Update Photo", self.update_photo),
        ]

        for index, (label, command) in enumerate(buttons):
            row = index // 4
            col = index % 4
            tk.Button(
                btn_frame, text=label, command=command, width=15,
                bg="blue", fg="white"
            ).grid(row=row, column=col, padx=5, pady=5)

    # --------------------------------------------------
    # RIGHT SECTION
    # --------------------------------------------------
    def build_right_section(self, parent):
        img = self.load_image(
            "gettyimages-1022573162.jpg", (710, 130)
        )
        self.right_img = ImageTk.PhotoImage(img)
        tk.Label(parent, image=self.right_img).place(
            x=0, y=0, width=710, height=130
        )

        search_frame = tk.LabelFrame(
            parent, bd=2, bg="white", relief=tk.RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold")
        )
        search_frame.place(x=5, y=140, width=705, height=70)

        tk.Label(
            search_frame, text="Search By:",
            font=("times new roman", 12, "bold"), bg="white"
        ).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.search_combo = ttk.Combobox(
            search_frame, state="readonly", width=15,
            values=("Roll_No", "Phone_No", "StudentID")
        )
        self.search_combo.grid(row=0, column=1, padx=5, pady=5)
        self.search_combo.current(0)

        self.search_entry = ttk.Entry(search_frame, width=20)
        self.search_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            search_frame, text="Search", command=self.search_data,
            bg="blue", fg="white", width=10
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            search_frame, text="Show All", command=self.fetch_data,
            bg="blue", fg="white", width=10
        ).grid(row=0, column=4, padx=5)

        table_frame = tk.Frame(parent, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=5, y=220, width=705, height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)

        columns = (
            "dep", "course", "year", "sem", "id", "name", "div",
            "roll", "gender", "dob", "email", "phone", "address",
            "teacher", "photo"
        )

        self.student_table = ttk.Treeview(
            table_frame, columns=columns, show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        headings = {
            "dep": "Department", "course": "Course",
            "year": "Year", "sem": "Semester", "id": "ID",
            "name": "Name", "div": "Division", "roll": "Roll No",
            "gender": "Gender", "dob": "DOB", "email": "Email",
            "phone": "Phone", "address": "Address",
            "teacher": "Teacher", "photo": "Photo"
        }

        widths = {
            "dep": 100, "course": 100, "year": 80, "sem": 80,
            "id": 100, "name": 120, "div": 80, "roll": 100,
            "gender": 100, "dob": 100, "email": 150, "phone": 120,
            "address": 150, "teacher": 120, "photo": 80
        }

        for col in columns:
            self.student_table.heading(col, text=headings[col])
            self.student_table.column(col, width=widths[col])

        self.student_table.pack(fill=tk.BOTH, expand=True)
        self.student_table.bind(
            "<ButtonRelease-1>", self.get_cursor
        )

        self.fetch_data()

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------
    def fields_valid(self):
        required = [
            self.var_dep.get(), self.var_course.get(),
            self.var_year.get(), self.var_semester.get(),
            self.var_std_id.get().strip(),
            self.var_std_name.get().strip(), self.var_div.get(),
            self.var_roll.get().strip(), self.var_gender.get(),
            self.var_dob.get().strip(), self.var_email.get().strip(),
            self.var_phone.get().strip(), self.var_address.get().strip()
        ]

        if any(value == "" or value.startswith("Select ") for value in required):
            messagebox.showerror(
                "Error", "Please fill in all required fields!",
                parent=self.root
            )
            return False

        try:
            int(self.var_std_id.get().strip())
        except ValueError:
            messagebox.showerror(
                "Error", "Student ID must be a whole number.",
                parent=self.root
            )
            return False

        return True

    # --------------------------------------------------
    # SAVE STUDENT
    # --------------------------------------------------
    def add_data(self):
        if not self.fields_valid():
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO student
                        (department, cource, year, semester, student_id,
                         name, division, roll, gender, dob, email, phone,
                         address, teacher, photo_sample)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            int(self.var_std_id.get()),
                            self.var_std_name.get().strip(),
                            self.var_div.get(),
                            self.var_roll.get().strip(),
                            self.var_gender.get(),
                            self.var_dob.get().strip(),
                            self.var_email.get().strip(),
                            self.var_phone.get().strip(),
                            self.var_address.get().strip(),
                            self.var_teacher.get().strip(),
                            str(self.photo_var.get())
                        )
                    )

            self.fetch_data()
            messagebox.showinfo(
                "Success", "Student record saved!", parent=self.root
            )

        except psycopg.errors.UniqueViolation:
            messagebox.showerror(
                "Error", "This Student ID already exists.",
                parent=self.root
            )
        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # FETCH STUDENTS
    # --------------------------------------------------
    def fetch_data(self):
        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT department, cource, year, semester,
                               student_id, name, division, roll, gender,
                               dob, email, phone, address, teacher,
                               photo_sample
                        FROM student
                        ORDER BY student_id
                        """
                    )
                    rows = cur.fetchall()

            self.student_table.delete(
                *self.student_table.get_children()
            )

            for row in rows:
                self.student_table.insert("", tk.END, values=row)

        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # SEARCH STUDENTS
    # --------------------------------------------------
    def search_data(self):
        search_value = self.search_entry.get().strip()

        if not search_value:
            messagebox.showerror(
                "Search Error", "Enter a value to search.",
                parent=self.root
            )
            return

        search_fields = {
            "Roll_No": "roll",
            "Phone_No": "phone",
            "StudentID": "student_id"
        }
        field = search_fields.get(self.search_combo.get())

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    if field == "student_id":
                        try:
                            value = int(search_value)
                        except ValueError:
                            messagebox.showerror(
                                "Search Error",
                                "Student ID must be a whole number.",
                                parent=self.root
                            )
                            return
                    else:
                        value = search_value

                    cur.execute(
                        f"""
                        SELECT department, cource, year, semester,
                               student_id, name, division, roll, gender,
                               dob, email, phone, address, teacher,
                               photo_sample
                        FROM student
                        WHERE {field} = %s
                        ORDER BY student_id
                        """,
                        (value,)
                    )
                    rows = cur.fetchall()

            self.student_table.delete(
                *self.student_table.get_children()
            )

            for row in rows:
                self.student_table.insert("", tk.END, values=row)

            if not rows:
                messagebox.showinfo(
                    "Search", "No matching student found.",
                    parent=self.root
                )

        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # SELECT A ROW
    # --------------------------------------------------
    def get_cursor(self, event=None):
        selected = self.student_table.focus()
        if not selected:
            return

        data = self.student_table.item(selected, "values")
        if not data:
            return

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

        try:
            self.photo_var.set(int(data[14] or 0))
        except (ValueError, TypeError):
            self.photo_var.set(0)

    # --------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------
    def update_data(self):
        if not self.fields_valid():
            return

        if not messagebox.askyesno(
            "Update", "Update this student record?",
            parent=self.root
        ):
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE student
                        SET department=%s, cource=%s, year=%s,
                            semester=%s, name=%s, division=%s,
                            roll=%s, gender=%s, dob=%s, email=%s,
                            phone=%s, address=%s, teacher=%s,
                            photo_sample=%s
                        WHERE student_id=%s
                        """,
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get().strip(),
                            self.var_div.get(),
                            self.var_roll.get().strip(),
                            self.var_gender.get(),
                            self.var_dob.get().strip(),
                            self.var_email.get().strip(),
                            self.var_phone.get().strip(),
                            self.var_address.get().strip(),
                            self.var_teacher.get().strip(),
                            str(self.photo_var.get()),
                            int(self.var_std_id.get())
                        )
                    )

                    if cur.rowcount == 0:
                        messagebox.showerror(
                            "Error", "Student ID not found.",
                            parent=self.root
                        )
                        return

            self.fetch_data()
            messagebox.showinfo(
                "Success", "Student record updated!",
                parent=self.root
            )

        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------
    def delete_data(self):
        student_id = self.var_std_id.get().strip()

        if not student_id:
            messagebox.showerror(
                "Error", "Student ID is required.",
                parent=self.root
            )
            return

        try:
            student_id = int(student_id)
        except ValueError:
            messagebox.showerror(
                "Error", "Student ID must be a whole number.",
                parent=self.root
            )
            return

        if not messagebox.askyesno(
            "Delete", "Delete this student record?",
            parent=self.root
        ):
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "DELETE FROM student WHERE student_id = %s",
                        (student_id,)
                    )

                    if cur.rowcount == 0:
                        messagebox.showerror(
                            "Error", "Student ID not found.",
                            parent=self.root
                        )
                        return

            self.fetch_data()
            self.reset_data()

            messagebox.showinfo(
                "Success", "Student record deleted!",
                parent=self.root
            )

        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # RESET FORM
    # --------------------------------------------------
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

    # --------------------------------------------------
    # CAPTURE FACE DATASET
    # --------------------------------------------------
    def generate_dataset(self):
        if not self.fields_valid():
            return

        student_id = int(self.var_std_id.get())

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT student_id FROM student WHERE student_id=%s",
                        (student_id,)
                    )
                    result = cur.fetchone()

                    if result is None:
                        messagebox.showerror(
                            "Error",
                            "Save the student record before taking photos.",
                            parent=self.root
                        )
                        return

                    cur.execute(
                        """
                        UPDATE student
                        SET department=%s, cource=%s, year=%s,
                            semester=%s, name=%s, division=%s,
                            roll=%s, gender=%s, dob=%s, email=%s,
                            phone=%s, address=%s, teacher=%s,
                            photo_sample=%s
                        WHERE student_id=%s
                        """,
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get().strip(),
                            self.var_div.get(),
                            self.var_roll.get().strip(),
                            self.var_gender.get(),
                            self.var_dob.get().strip(),
                            self.var_email.get().strip(),
                            self.var_phone.get().strip(),
                            self.var_address.get().strip(),
                            self.var_teacher.get().strip(),
                            "1",
                            student_id
                        )
                    )

            self.fetch_data()

            cascade_path = os.path.join(
                BASE_DIR, "haarcascade_frontalface_default.xml"
            )
            if not os.path.isfile(cascade_path):
                cascade_path = os.path.join(
                    cv2.data.haarcascades,
                    "haarcascade_frontalface_default.xml"
                )

            face_classifier = cv2.CascadeClassifier(cascade_path)
            if face_classifier.empty():
                raise RuntimeError("Could not load face-detection cascade.")

            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                cap.release()
                raise RuntimeError(
                    "Camera could not be opened. Check camera permissions."
                )

            img_id = 0

            try:
                while img_id < 100:
                    ret, frame = cap.read()
                    if not ret:
                        messagebox.showerror(
                            "Camera Error", "Could not read from camera.",
                            parent=self.root
                        )
                        break

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, scaleFactor=1.3, minNeighbors=5
                    )

                    for (x, y, w, h) in faces:
                        face = gray[y:y + h, x:x + w]
                        face = cv2.resize(face, (450, 450))
                        img_id += 1

                        filename = os.path.join(
                            DATA_DIR,
                            f"user.{student_id}.{img_id}.jpg"
                        )
                        if not cv2.imwrite(filename, face):
                            raise RuntimeError(
                                f"Could not save image: {filename}"
                            )

                        cv2.putText(
                            frame, str(img_id), (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1,
                            (0, 255, 0), 2
                        )
                        cv2.rectangle(
                            frame, (x, y), (x + w, y + h),
                            (0, 255, 0), 2
                        )
                        break

                    cv2.imshow("Face Dataset Capture", frame)

                    if cv2.waitKey(1) & 0xFF == 27:
                        break

            finally:
                cap.release()
                cv2.destroyAllWindows()

            self.photo_var.set(1)
            messagebox.showinfo(
                "Result",
                f"Face dataset capture finished. Images captured: {img_id}",
                parent=self.root
            )

        except Exception as exc:
            messagebox.showerror(
                "Error", str(exc), parent=self.root
            )

    # --------------------------------------------------
    # UPDATE PHOTO FLAG
    # --------------------------------------------------
    def update_photo(self):
        student_id = self.var_std_id.get().strip()

        if not student_id:
            messagebox.showerror(
                "Error", "Student ID is required.", parent=self.root
            )
            return

        try:
            student_id = int(student_id)
        except ValueError:
            messagebox.showerror(
                "Error", "Student ID must be a whole number.",
                parent=self.root
            )
            return

        try:
            with db_connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE student
                        SET photo_sample=%s
                        WHERE student_id=%s
                        """,
                        (str(self.photo_var.get()), student_id)
                    )

                    if cur.rowcount == 0:
                        messagebox.showerror(
                            "Error", "Student ID not found.",
                            parent=self.root
                        )
                        return

            self.fetch_data()
            messagebox.showinfo(
                "Success", "Photo sample status updated!",
                parent=self.root
            )

        except Exception as exc:
            messagebox.showerror(
                "Database Error", str(exc), parent=self.root
            )


if __name__ == "__main__":
    root = tk.Tk()

    try:
        obj = Student(root)
        root.mainloop()
    except Exception as exc:
        messagebox.showerror(
            "Application Error",
            f"Could not start Student Management window:\n{exc}",
            parent=root
        )
        root.destroy()
