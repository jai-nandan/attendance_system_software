from tkinter import *
from tkinter import ttk
from unittest import result
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")


        title_lb1 = Label(self.root, text="TRAIN DATASET", font=("new times roman", 35, "bold"),bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

         #==================TOP IMAGE=================
               
        img_top = Image.open(r"D:\project of ai engineer\attendance system\college_images\facialrecognition.jpg")
        img = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(img)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=55, width=1530, height=325)

        #==================BUTTON=================

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("new times roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

          #==================BOTTOM IMAGE=================


        img_bottom = Image.open(r"D:\project of ai engineer\attendance system\college_images\person.png")
        img = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.bg_photo_bottom = ImageTk.PhotoImage(img)

        bg_label = Label(self.root, image=self.bg_photo_bottom)
        bg_label.place(x=0, y=440, width=1530, height=325)

        #==================FUNCTION  Of BUTTON=================
    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        #=============Train the classifier and save=============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!", parent=self.root)


        


















if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()