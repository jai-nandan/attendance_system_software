from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import webbrowser
import time


class Help_Support:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")

        # ================= SPLASH SCREEN =================
        self.splash()

        # Delay then load main UI
        self.root.after(2000, self.main_ui)

    # ================= SPLASH =================
    def splash(self):
        splash_frame = Frame(self.root, bg="black")
        splash_frame.place(x=0, y=0, width=1530, height=768)

        text = Label(splash_frame, text="LOADING HELP CENTER...",
                     font=("Segoe UI", 28, "bold"),
                     fg="#00ffff", bg="black")
        text.place(relx=0.5, rely=0.5, anchor=CENTER)

    # ================= MAIN UI =================
    def main_ui(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        # TITLE
        title = Label(self.root, text="HELP CENTER",
                      font=("Segoe UI", 34, "bold"),
                      bg="#020c1b", fg="#00ffff")
        title.pack(fill=X)

        # BACKGROUND
        img_bg = Image.open(r"D:\project of ai engineer\attendance system\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_bg = img_bg.resize((1530, 720), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img_bg)

        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=60, width=1530, height=720)

        # GLOW BORDER
        self.glow = Frame(bg_label, bg="#00ffff")
        self.glow.place(relx=0.5, rely=0.5, anchor=CENTER, width=720, height=520)

        # MAIN CARD
        self.main_frame = Frame(bg_label, bg="#0a192f")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=500)

        # HEADING
        heading = Label(self.main_frame, text="Need Help?",
                        font=("Segoe UI", 26, "bold"),
                        bg="#0a192f", fg="#00ffff")
        heading.pack(pady=20)

        # EMAIL
        self.email = "Jainandan2409@gmail.com"
        email = Label(self.main_frame,
                      text="📧 " + self.email,
                      font=("Segoe UI", 14, "bold"),
                      bg="#0a192f", fg="white")
        email.pack(pady=10)

        # BUTTONS
        btn_frame = Frame(self.main_frame, bg="#0a192f")
        btn_frame.pack(pady=10)

        self.create_btn(btn_frame, "Copy Email", self.copy_email, 0)
        self.create_btn(btn_frame, "Open Gmail", self.open_gmail, 1)

        # ================= AI CHAT =================
        chat_label = Label(self.main_frame, text="AI Assistant",
                           font=("Segoe UI", 16, "bold"),
                           bg="#0a192f", fg="#00ffff")
        chat_label.pack(pady=10)

        self.chat_box = Text(self.main_frame, height=6, width=70,
                             bg="#020c1b", fg="white")
        self.chat_box.pack()

        self.entry = Entry(self.main_frame, width=50)
        self.entry.pack(pady=5)

        send_btn = Button(self.main_frame, text="Send",
                          command=self.reply,
                          bg="#00ffff")
        send_btn.pack()

        # START ANIMATION
        self.colors = ["#00ffff", "#00ccff", "#0099ff", "#00ccff"]
        self.i = 0
        self.animate()

    # ================= BUTTON FUNCTION =================
    def create_btn(self, frame, text, cmd, col):
        btn = Button(frame, text=text, command=cmd,
                     font=("Segoe UI", 11, "bold"),
                     bg="#00ffff", fg="black",
                     width=15, cursor="hand2")
        btn.grid(row=0, column=col, padx=10)

        btn.bind("<Enter>", lambda e: btn.config(bg="#00cccc"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#00ffff"))

    # ================= AI REPLY =================
    def reply(self):
        user = self.entry.get()
        self.chat_box.insert(END, "You: " + user + "\n")

        if "error" in user.lower():
            response = "Try restarting the system or check camera permissions."
        elif "email" in user.lower():
            response = "You can contact us at: " + self.email
        else:
            response = "Our team will assist you soon!"

        self.chat_box.insert(END, "AI: " + response + "\n\n")
        self.entry.delete(0, END)

    # ================= FUNCTIONS =================
    def copy_email(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.email)
        msg.showinfo("Copied", "Email copied!")

    def open_gmail(self):
        webbrowser.open("https://mail.google.com/")

    # ================= GLOW ANIMATION =================
    def animate(self):
        self.glow.config(bg=self.colors[self.i])
        self.i = (self.i + 1) % len(self.colors)
        self.root.after(300, self.animate)


if __name__ == "__main__":
    root = Tk()
    obj = Help_Support(root)
    root.mainloop()