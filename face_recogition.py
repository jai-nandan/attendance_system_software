
from tkinter import *
from PIL import Image, ImageTk
import psycopg
import cv2
from datetime import datetime
import os
import csv


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        # Face recognition stability
        self.last_id = None
        self.same_frames = 0
        self.required_frames = 5

        # Database settings
        self.db_config = {
            "host": "localhost",
            "port": 5432,
            "dbname": "face_recognizer",
            "user": "postgres",
            "password": "jai5911"
        }

        # Project paths
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.attendance_file = os.path.join(
            self.base_dir, "Attendance.csv"
        )
        self.classifier_path = os.path.join(
            self.base_dir, "classifier.xml"
        )
        self.left_image_path = os.path.join(
            self.base_dir, "college_images", "face_dector.png"
        )
        self.right_image_path = os.path.join(
            self.base_dir, "college_images", "FACE.jpg"
        )

        # Title
        Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green"
        ).place(x=0, y=0, width=1530, height=45)

        # Left image
        try:
            img_left = Image.open(self.left_image_path)
            img_left = img_left.resize(
                (650, 700), Image.Resampling.LANCZOS
            )
            self.photo_left = ImageTk.PhotoImage(img_left)

            Label(
                self.root, image=self.photo_left
            ).place(x=0, y=55, width=650, height=700)

        except Exception as e:
            print("Left image error:", e)

        # Right image
        try:
            img_right = Image.open(self.right_image_path)
            img_right = img_right.resize(
                (880, 700), Image.Resampling.LANCZOS
            )
            self.photo_right = ImageTk.PhotoImage(img_right)

            right_lbl = Label(
                self.root, image=self.photo_right
            )
            right_lbl.place(x=650, y=55, width=880, height=700)

            Button(
                right_lbl,
                text="Face Recognition",
                command=self.face_recog,
                font=("times new roman", 18, "bold"),
                bg="darkgreen",
                fg="white"
            ).place(x=340, y=620, width=200, height=40)

        except Exception as e:
            print("Right image error:", e)

    # Database connection
    def db_connect(self):
        return psycopg.connect(**self.db_config)

    # Mark attendance once per student per day
    def mark_attendance(self, sid, name, roll, dep):
        date_today = datetime.now().strftime("%d/%m/%Y")
        time_now = datetime.now().strftime("%H:%M:%S")

        file_exists = os.path.exists(self.attendance_file)

        try:
            with open(
                self.attendance_file,
                "a",
                newline="",
                encoding="utf-8"
            ) as f:
                writer = csv.writer(f)

                if not file_exists or os.path.getsize(
                    self.attendance_file
                ) == 0:
                    writer.writerow([
                        "ID", "Name", "Roll", "Department",
                        "Time", "Date", "Status"
                    ])

                # Check whether attendance is already marked today
                already_marked = False

                if os.path.getsize(self.attendance_file) > 0:
                    with open(
                        self.attendance_file,
                        "r",
                        newline="",
                        encoding="utf-8"
                    ) as read_file:
                        reader = csv.reader(read_file)
                        next(reader, None)

                        for row in reader:
                            if (
                                len(row) >= 6
                                and row[0] == str(sid)
                                and row[5] == date_today
                            ):
                                already_marked = True
                                break

                if not already_marked:
                    writer.writerow([
                        sid, name, roll, dep,
                        time_now, date_today, "Present"
                    ])
                    print("Attendance marked:", sid, name)
                else:
                    print("Already marked today:", sid)

        except Exception as e:
            print("Attendance file error:", e)

    # Fetch student information from PostgreSQL
    def get_student(self, student_id):
        try:
            with self.db_connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT student_id, name, roll, department
                        FROM student
                        WHERE student_id = %s
                        """,
                        (int(student_id),)
                    )
                    return cursor.fetchone()

        except Exception as e:
            print("Database error:", e)
            return None

    # Face recognition
    def face_recog(self):
        if not os.path.exists(self.classifier_path):
            print(
                "Error: classifier.xml not found. "
                "Train the face recognizer first."
            )
            return

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades
            + "haarcascade_frontalface_default.xml"
        )

        if face_cascade.empty():
            print("Error: Face detection model could not load.")
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(self.classifier_path)
        except Exception as e:
            print("Recognizer error:", e)
            print(
                'Install the contrib package using: '
                'python -m pip install opencv-contrib-python'
            )
            return

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Camera could not be opened.")
            return

        try:
            while True:
                ret, frame = cap.read()

                if not ret:
                    print("Could not read from camera.")
                    break

                gray = cv2.cvtColor(
                    frame, cv2.COLOR_BGR2GRAY
                )
                faces = face_cascade.detectMultiScale(
                    gray, scaleFactor=1.2, minNeighbors=5
                )

                for (x, y, w, h) in faces:
                    roi = gray[y:y + h, x:x + w]
                    roi = cv2.resize(roi, (200, 200))
                    roi = cv2.equalizeHist(roi)

                    student_id, distance = recognizer.predict(roi)

                    print(
                        "ID:", student_id,
                        "Distance:", distance
                    )

                    # Lower distance generally means a closer match.
                    # Adjust this threshold after testing your model.
                    if distance < 50:
                        if self.last_id == student_id:
                            self.same_frames += 1
                        else:
                            self.last_id = student_id
                            self.same_frames = 1

                        if self.same_frames >= self.required_frames:
                            result = self.get_student(student_id)

                            if result:
                                sid, name, roll, dep = result

                                cv2.rectangle(
                                    frame, (x, y), (x + w, y + h),
                                    (0, 255, 0), 3
                                )
                                cv2.putText(
                                    frame, f"ID: {sid}",
                                    (x, max(y - 80, 20)),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    0.7, (255, 255, 255), 2
                                )
                                cv2.putText(
                                    frame, f"Name: {name}",
                                    (x, max(y - 55, 20)),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    0.7, (255, 255, 255), 2
                                )
                                cv2.putText(
                                    frame, f"Roll: {roll}",
                                    (x, max(y - 30, 20)),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    0.7, (255, 255, 255), 2
                                )
                                cv2.putText(
                                    frame, f"Dept: {dep}",
                                    (x, max(y - 5, 20)),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    0.7, (255, 255, 255), 2
                                )

                                self.mark_attendance(
                                    sid, name, roll, dep
                                )
                            else:
                                cv2.rectangle(
                                    frame, (x, y), (x + w, y + h),
                                    (0, 0, 255), 3
                                )
                                cv2.putText(
                                    frame, "Student ID not found",
                                    (x, max(y - 10, 20)),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (0, 0, 255), 2
                                )
                    else:
                        self.last_id = None
                        self.same_frames = 0

                        cv2.rectangle(
                            frame, (x, y), (x + w, y + h),
                            (0, 0, 255), 3
                        )
                        cv2.putText(
                            frame, "Unknown",
                            (x, max(y - 10, 20)),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8, (0, 0, 255), 2
                        )

                cv2.imshow("Face Recognition", frame)

                # Press ENTER or ESC to exit
                key = cv2.waitKey(1) & 0xFF
                if key == 13 or key == 27:
                    break

        finally:
            cap.release()
            cv2.destroyAllWindows()


# Main
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
