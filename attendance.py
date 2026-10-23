
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import psycopg
import cv2
import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "college_images")
CSV_PATH = os.path.join(BASE_DIR, "Attendance.csv")

# Use the same working PostgreSQL settings as test_db.py
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "face_recognition",
    "user": "postgres",
    "password": "jai5911"
}


def get_db_connection():
    return psycopg.connect(**DB_CONFIG)


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        self.var_attendance_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()

        # Header images
        self.header_right = self.load_image(
            "gettyimages-1022573162.jpg", (800, 130)
        )
        Label(self.root, image=self.header_right).place(
            x=0, y=0, width=800, height=130
        )

        self.header_left = self.load_image(
            "smart-attendance.jpg", (800, 130)
        )
        Label(self.root, image=self.header_left).place(
            x=800, y=0, width=800, height=130
        )

        # Background
        self.bg_photo = self.load_image("background.png", (1530, 768))
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=130, width=1530, height=638)

        Label(
            bg_label,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue"
        ).place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=580)

        # Left frame
        left_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE,
            text="Student Attendance",
            font=("times new roman", 12, "bold")
        )
        left_frame.place(x=5, y=10, width=730, height=560)

        self.photo_left = self.load_image("attendance.png", (720, 130))
        Label(left_frame, image=self.photo_left).place(
            x=5, y=0, width=720, height=130
        )

        inside = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        inside.place(x=0, y=135, width=720, height=400)

        fields = [
            ("Attendance ID:", self.var_attendance_id, 0, 0),
            ("Student Name:", self.var_name, 0, 2),
            ("Roll No:", self.var_roll, 1, 0),
            ("Department:", self.var_department, 1, 2),
            ("Time:", self.var_time, 2, 0),
            ("Date:", self.var_date, 2, 2),
        ]

        for label, variable, row, col in fields:
            Label(
                inside, text=label,
                font=("times new roman", 12, "bold"),
                bg="white"
            ).grid(row=row, column=col, padx=10, pady=8, sticky=W)

            ttk.Entry(
                inside, textvariable=variable, width=20,
                font=("times new roman", 12, "bold")
            ).grid(row=row, column=col + 1, padx=10, pady=8, sticky=W)

        Label(
            inside, text="Attendance Status:",
            font=("times new roman", 12, "bold"), bg="white"
        ).grid(row=3, column=0, padx=10, pady=8, sticky=W)

        self.attendance_status_entry = ttk.Combobox(
            inside, textvariable=self.var_attendance_status,
            font=("times new roman", 12, "bold"),
            state="readonly", width=18,
            values=("Present", "Absent")
        )
        self.attendance_status_entry.grid(
            row=3, column=1, padx=10, pady=8, sticky=W
        )
        self.attendance_status_entry.current(0)

        btn_frame = Frame(inside, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        Button(
            btn_frame, text="Import CSV", command=self.importcsv,
            font=("times new roman", 12, "bold"),
            bg="blue", fg="white", width=19
        ).grid(row=0, column=0, padx=1)

        Button(
            btn_frame, text="Export CSV", command=self.exportcsv,
            font=("times new roman", 12, "bold"),
            bg="blue", fg="white", width=19
        ).grid(row=0, column=1, padx=1)

        Button(
            btn_frame, text="Update", command=self.update_data,
            font=("times new roman", 12, "bold"),
            bg="blue", fg="white", width=19
        ).grid(row=0, column=2, padx=1)

        Button(
            btn_frame, text="Reset", command=self.reset_data,
            font=("times new roman", 12, "bold"),
            bg="blue", fg="white", width=19
        ).grid(row=0, column=3, padx=1)

        # Right frame
        right_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 12, "bold")
        )
        right_frame.place(x=750, y=10, width=720, height=560)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=710, height=540)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(
            table_frame,
            columns=(
                "id", "name", "roll", "department",
                "time", "date", "attendance"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings"
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        headings = {
            "id": "Attendance ID",
            "name": "Name",
            "roll": "Roll No",
            "department": "Department",
            "time": "Time",
            "date": "Date",
            "attendance": "Attendance Status"
        }

        for column, heading in headings.items():
            self.attendance_table.heading(column, text=heading)
            self.attendance_table.column(column, width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def load_image(self, filename, size):
        path = os.path.join(IMAGE_DIR, filename)
        try:
            image = Image.open(path)
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            messagebox.showerror(
                "Image Error",
                f"Could not load {filename}\n{e}",
                parent=self.root
            )
            raise

    def fetch_data(self):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT attendance_id, name, roll, department,
                               attendance_time, attendance_date,
                               attendance_status
                        FROM attendance
                        ORDER BY attendance_id
                    """)
                    rows = cur.fetchall()

            self.attendance_table.delete(
                *self.attendance_table.get_children()
            )
            for row in rows:
                self.attendance_table.insert("", END, values=row)

        except Exception as e:
            messagebox.showerror(
                "Database Error", str(e), parent=self.root
            )

    def importcsv(self):
        path = filedialog.askopenfilename(
            parent=self.root,
            title="Select attendance CSV",
            filetypes=[("CSV files", "*.csv")]
        )
        if not path:
            return

        try:
            with open(path, "r", newline="", encoding="utf-8-sig") as file:
                rows = list(csv.reader(file))

            if not rows:
                messagebox.showinfo("CSV", "The selected CSV is empty.")
                return

            # Accept either a header row or raw data.
            if rows[0] and rows[0][0].strip().lower() in (
                "attendance_id", "attendance id", "id"
            ):
                rows = rows[1:]

            inserted = 0
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    for row in rows:
                        if len(row) < 7:
                            continue

                        cur.execute("""
                            INSERT INTO attendance
                                (name, roll, department, attendance_time,
                                 attendance_date, attendance_status)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, (
                            row[1].strip() if len(row) >= 7 else "",
                            row[2].strip(),
                            row[3].strip(),
                            row[4].strip(),
                            row[5].strip(),
                            row[6].strip()
                        ))
                        inserted += 1

            self.fetch_data()
            messagebox.showinfo(
                "Import CSV", f"Imported {inserted} attendance records.",
                parent=self.root
            )

        except Exception as e:
            messagebox.showerror(
                "Import Error", str(e), parent=self.root
            )

    def exportcsv(self):
        path = filedialog.asksaveasfilename(
            parent=self.root,
            title="Save attendance CSV",
            defaultextension=".csv",
            initialfile="Attendance.csv",
            filetypes=[("CSV files", "*.csv")]
        )
        if not path:
            return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT attendance_id, name, roll, department,
                               attendance_time, attendance_date,
                               attendance_status
                        FROM attendance
                        ORDER BY attendance_id
                    """)
                    rows = cur.fetchall()

            with open(path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Attendance ID", "Name", "Roll No", "Department",
                    "Time", "Date", "Attendance Status"
                ])
                writer.writerows(rows)

            messagebox.showinfo(
                "Export CSV", "Attendance exported successfully.",
                parent=self.root
            )

        except Exception as e:
            messagebox.showerror(
                "Export Error", str(e), parent=self.root
            )

    def get_cursor(self, event=""):
        selected = self.attendance_table.focus()
        if not selected:
            return

        data = self.attendance_table.item(selected, "values")
        if not data:
            return

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
        self.var_attendance_status.set("Present")
        self.attendance_table.selection_remove(
            self.attendance_table.selection()
        )

    def update_data(self):
        attendance_id = self.var_attendance_id.get().strip()

        if not attendance_id.isdigit():
            messagebox.showerror(
                "Validation Error",
                "Select a valid attendance record first.",
                parent=self.root
            )
            return

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        UPDATE attendance
                        SET name = %s,
                            roll = %s,
                            department = %s,
                            attendance_time = %s,
                            attendance_date = %s,
                            attendance_status = %s
                        WHERE attendance_id = %s
                    """, (
                        self.var_name.get().strip(),
                        self.var_roll.get().strip(),
                        self.var_department.get().strip(),
                        self.var_time.get().strip(),
                        self.var_date.get().strip(),
                        self.var_attendance_status.get().strip(),
                        int(attendance_id)
                    ))

                    if cur.rowcount == 0:
                        messagebox.showwarning(
                            "Not Found", "Attendance record not found.",
                            parent=self.root
                        )
                        return

            self.fetch_data()
            messagebox.showinfo(
                "Success", "Attendance updated successfully.",
                parent=self.root
            )

        except Exception as e:
            messagebox.showerror(
                "Update Error", str(e), parent=self.root
            )


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
