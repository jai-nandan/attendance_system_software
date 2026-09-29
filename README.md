# 🚀 Face Recognition Attendance System

A desktop Tkinter application that uses OpenCV face recognition to mark student attendance and manage student records.

## 📌 Overview

This project is a Python desktop GUI application (built with Tkinter) that automates classroom attendance using face recognition. It lets an admin register students with their photos, train a face classifier on the captured images, then run live face recognition via webcam to automatically mark attendance, which is logged to a CSV file and a MySQL database.

## ✨ Features

* **Login system** backed by MySQL (`mysql.connector`)
* **Main dashboard** with panel buttons for Student Panel, Face Detector, Attendance, Help Support, Data Train, Photo Sample, Developers, and Exit
* **Student Panel** — register and manage student details
* **Photo Sample capture** — stores per-student face image samples (visible in `data/`, with hundreds of `user.<id>.<n>.jpg` training images already captured for multiple student IDs)
* **Data Train** — trains a Haar Cascade-based face classifier (`haarcascade_frontalface_default.xml`, `classifier.xml`) from the captured photo samples using OpenCV
* **Face Detector / Face Recognition** — runs real-time webcam-based face detection and recognition using OpenCV (`cv2`), with a stability mechanism requiring a face to be recognized consistently across several frames before confirming an identity
* **Attendance marking** — automatically appends a new entry (ID, Name, Roll, Department, Time, Date, Status) to `Attendance.csv` when a registered face is recognized, avoiding duplicate same-day entries
* **Attendance viewer** module to review logged records
* **Help/Support** and **Developers** info windows

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* OpenCV (`cv2`) — face detection/recognition and classifier training
* NumPy
* Pillow (`PIL`) — image handling in the GUI
* MySQL (`mysql.connector`) — student/login data storage
* CSV — attendance log storage

## 📂 Project Structure

```text
attendance_system_software/
├── main.py                 # Main dashboard window
├── login.py                 # Login screen (MySQL-backed)
├── register.py               # Registration flow
├── student.py                 # Student panel
├── train.py                     # Classifier training
├── face_recogition.py            # Live face detection/recognition + attendance marking
├── attendance.py                   # Attendance record viewer
├── developer.py                      # Developer info window
├── help_me.py                          # Help/support window
├── classifier.xml                        # Trained face classifier
├── haarcascade_frontalface_default.xml     # OpenCV Haar Cascade model
├── Attendance.csv                            # Logged attendance records
├── data/                                       # Captured student face photo samples
└── college_images/                               # UI banner/button images
```

## ⚙️ Installation

```bash
git clone https://github.com/jai-nandan/attendance_system_software.git
cd attendance_system_software
pip install opencv-python numpy pillow mysql-connector-python
```

A `requirements.txt` file is not present in this project — the dependency list above is inferred directly from the `import` statements in the source files.

## ▶️ How to Run

1. Set up a local MySQL database and update the connection details used by `login.py` / `student.py` (database configuration is not specified in the current project files).
2. Run the application:
   ```bash
   python main.py
   ```
3. Use the dashboard buttons to register students, capture photo samples, train the classifier, and run live face recognition to mark attendance.

## 💡 How It Works

* **Input:** Webcam video feed and student photo samples captured through the GUI.
* **Training:** `train.py` uses OpenCV's classifier training utilities on the images stored in `data/` (named `user.<id>.<sample_number>.jpg`) to build/update `classifier.xml`.
* **Recognition:** `face_recogition.py` uses OpenCV's Haar Cascade (`haarcascade_frontalface_default.xml`) to detect faces in the live camera feed, then matches them against the trained classifier. A face must be recognized consistently for a set number of frames (`required_frames = 5`) before it is confirmed, reducing false positives.
* **Output:** On a confirmed match, `mark_attendance()` writes a new row (ID, Name, Roll, Department, Time, Date, Status) to `Attendance.csv`, checking first that the same student hasn't already been marked that day.

## 🎯 Learning Outcomes

* Building a desktop GUI application with Tkinter
* Real-time face detection and recognition using OpenCV Haar Cascades
* Integrating a GUI application with a MySQL database
* Designing a stability/confirmation mechanism to reduce false-positive recognitions
* File-based (CSV) logging alongside database-backed student records

## 🔮 Future Improvements

* Replace hardcoded absolute Windows file paths (`D:\project of ai engineer\...`) with relative paths for portability
* Move database credentials out of source code into a config/environment file
* Upgrade from Haar Cascade to a deep-learning-based face recognition model for improved accuracy
* Add a proper `requirements.txt` for reproducible installs
* Add unit tests for the attendance-marking logic

## ⚠️ Limitations

* Contains hardcoded absolute file paths (`D:\project of ai engineer\attendance system\...`) that must be updated to run on another machine
* Requires a working MySQL server and the exact schema expected by `login.py`/`student.py`, which is not documented in the project
* Uses Haar Cascade-based recognition, which is less accurate than modern deep-learning face recognition approaches
* Windows-specific calls (`os.startfile`) are used in a few places, limiting cross-platform compatibility

## 👨‍💻 Author

**Jai Nandan**

GitHub: `https://github.com/jai-nandan`

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
