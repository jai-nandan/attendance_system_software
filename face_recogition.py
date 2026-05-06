from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
import os
import time


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        # 🔥 STABILITY FIX
        self.last_id = None
        self.same_frames = 0
        self.required_frames = 5

        # TITLE
        Label(self.root, text="FACE RECOGNITION",
              font=("times new roman", 35, "bold"),
              bg="white", fg="green").place(x=0, y=0, width=1530, height=45)

        img_left = Image.open(r"D:\project of ai engineer\attendance system\college_images\face_dector.png")
        img_left = img_left.resize((650, 700), Image.Resampling.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_left)
        Label(self.root, image=self.photo_left).place(x=0, y=55, width=650, height=700)

        img_right = Image.open(r"D:\project of ai engineer\attendance system\college_images\FACE.jpg")
        img_right = img_right.resize((950, 700), Image.Resampling.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(img_right)

        right_lbl = Label(self.root, image=self.photo_right)
        right_lbl.place(x=650, y=55, width=950, height=700)

        Button(right_lbl, text="Face Recognition",
               command=self.face_recog,
               font=("times new roman", 18, "bold"),
               bg="darkgreen", fg="white").place(x=365, y=620, width=200, height=40)

    # ================= ATTENDANCE =================
    def mark_attendance(self, sid, name, roll, dep):

        file = "Attendance.csv"

        # create file if not exists
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("ID,Name,Roll,Department,Time,Date,Status\n")

        now = datetime.now()
        date_today = now.strftime('%d/%m/%Y')

        with open(file, "r+") as f:
            data = f.readlines()

            entry_exists = False

            for line in data:
                entry = line.split(",")
                if len(entry) > 5:
                    if entry[0] == str(sid) and entry[5].strip() == date_today:
                        entry_exists = True
                        break

            if not entry_exists:
                f.writelines(f"{sid},{name},{roll},{dep},{now.strftime('%H:%M:%S')},{date_today},Present\n")
                print("✅ Attendance Marked:", sid, name)

                # small delay to avoid multiple writes
                time.sleep(1)
            else:
                print("⚠ Already Marked Today:", sid)

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        def recognize(img, faceCascade, recognizer):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)

            for (x, y, w, h) in faces:
                roi = gray[y:y+h, x:x+w]
                roi = cv2.resize(roi, (200, 200))
                roi = cv2.equalizeHist(roi)

                id, distance = recognizer.predict(roi)
                print("ID:", id, "Distance:", distance)

                # 🔥 STRICT CONDITION
                if distance < 50:

                    # stability check
                    if self.last_id == id:
                        self.same_frames += 1
                    else:
                        self.last_id = id
                        self.same_frames = 1

                    # confirm after few frames
                    if self.same_frames >= self.required_frames:

                        try:
                            conn = mysql.connector.connect(
                                host="localhost",
                                username="root",
                                password="jainandan",
                                database="attendancesystem"
                            )
                            cursor = conn.cursor()

                            cursor.execute(
                                "SELECT STUDENT_ID, NAME, ROLL, DEPARTMENT FROM student WHERE STUDENT_ID=%s",
                                (id,)
                            )
                            result = cursor.fetchone()
                            conn.close()

                        except Exception as e:
                            print("DB Error:", e)
                            result = None

                        if result:
                            sid, name, roll, dep = result

                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

                            cv2.putText(img, f"ID: {sid}", (x, y-80),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                            cv2.putText(img, f"Name: {name}", (x, y-55),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                            cv2.putText(img, f"Roll: {roll}", (x, y-30),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                            cv2.putText(img, f"Dept: {dep}", (x, y-5),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                            self.mark_attendance(sid, name, roll, dep)

                else:
                    # reset on unknown
                    self.last_id = None
                    self.same_frames = 0

                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown", (x, y-10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

            return img

        faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            if not ret:
                break

            img = cv2.resize(img, (800, 600))
            img = recognize(img, faceCascade, recognizer)

            cv2.imshow("Face Recognition", img)

            # press ENTER to exit
            if cv2.waitKey(1) == 13:
                break

        cap.release()
        cv2.destroyAllWindows()


# MAIN
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
