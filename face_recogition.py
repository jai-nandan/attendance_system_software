from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        # ===== TITLE =====
        Label(self.root, text="FACE RECOGNITION",
              font=("times new roman", 35, "bold"),
              bg="white", fg="green").place(x=0, y=0, width=1530, height=45)

        # ===== LEFT IMAGE =====
        img_left = Image.open(r"D:\project of ai engineer\attendance system\college_images\face_dector.png")
        img_left = img_left.resize((650, 700), Image.Resampling.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_left)
        Label(self.root, image=self.photo_left).place(x=0, y=55, width=650, height=700)

        # ===== RIGHT IMAGE =====
        img_right = Image.open(r"D:\project of ai engineer\attendance system\college_images\FACE.jpg")
        img_right = img_right.resize((950, 700), Image.Resampling.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(img_right)

        right_lbl = Label(self.root, image=self.photo_right)
        right_lbl.place(x=650, y=55, width=950, height=700)

        # ===== BUTTON =====
        Button(right_lbl, text="Face Recognition",
               command=self.face_recog,
               font=("times new roman", 18, "bold"),
               bg="darkgreen", fg="white",
               cursor="hand2").place(x=365, y=620, width=200, height=40)

    # ===================== ATTENDANCE ======================
    def mark_attendance(self, sid, name, roll, dep):

        file_path = "Attendance.csv"

        # create file if not exists
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("ID,Name,Roll,Department,Time,Status\n")

        with open(file_path, "r+", newline="\n") as f:
            myDataList = f.readlines()
            entry_ids = []

            for line in myDataList:
                entry = line.split(",")
                entry_ids.append(entry[0])

            # avoid duplicate entry
            if str(sid) not in entry_ids:
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                date = now.strftime("%d/%m/%Y")

                f.writelines(f"{sid},{name},{roll},{dep},{dtString},{date},Present\n")

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        def recognize(img, faceCascade, recognizer):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.1, 10)

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]

                id, distance = recognizer.predict(face_roi)
                print("ID:", id, "Distance:", distance)

                if distance < 70:
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

                        # ✅ MARK ATTENDANCE
                        self.mark_attendance(sid, name, roll, dep)

                    else:
                        cv2.putText(img, "No Data Found", (x, y-10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

            return img  # ✅ moved outside loop

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Camera not working")
            return

        while True:
            ret, img = cap.read()

            if not ret or img is None:
                print("Frame error")
                break

            img = recognize(img, faceCascade, recognizer)

            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        cap.release()
        cv2.destroyAllWindows()


# ===== MAIN =====
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()