
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import webbrowser
import os


class Help_Support:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x768+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#020c1b")

        # Project directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Email
        self.email = "Jainandan2409@gmail.com"

        # Splash screen
        self.splash()

        # Load main UI after 2 seconds
        self.root.after(2000, self.main_ui)

    # ================= SPLASH SCREEN =================
    def splash(self):
        self.splash_frame = Frame(self.root, bg="black")
        self.splash_frame.place(
            x=0, y=0, width=1530, height=768
        )

        text = Label(
            self.splash_frame,
            text="LOADING HELP CENTER...",
            font=("Segoe UI", 28, "bold"),
            fg="#00ffff",
            bg="black"
        )
        text.place(relx=0.5, rely=0.5, anchor=CENTER)

    # ================= MAIN UI =================
    def main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title = Label(
            self.root,
            text="HELP CENTER",
            font=("Segoe UI", 34, "bold"),
            bg="#020c1b",
            fg="#00ffff"
        )
        title.pack(fill=X)

        # Background image path
        img_path = os.path.join(
            self.base_dir,
            "college_images",
            "1_5TRuG7tG0KrZJXKoFtHlSg.jpeg"
        )

        # Load background image
        try:
            img_bg = Image.open(img_path)
            img_bg = img_bg.resize(
                (1530, 720),
                Image.Resampling.LANCZOS
            )
            self.bg = ImageTk.PhotoImage(img_bg)

        except (FileNotFoundError, OSError) as error:
            msg.showerror(
                "Image Error",
                f"Background image could not be loaded.\n\n"
                f"Expected path:\n{img_path}\n\n"
                f"Details: {error}"
            )

            self.bg = None

        # Background container
        self.bg_label = Label(
            self.root,
            image=self.bg if self.bg else "",
            bg="#020c1b"
        )
        self.bg_label.place(
            x=0, y=60, width=1530, height=720
        )

        # Glow border
        self.glow = Frame(
            self.bg_label,
            bg="#00ffff"
        )
        self.glow.place(
            relx=0.5,
            rely=0.5,
            anchor=CENTER,
            width=720,
            height=520
        )

        # Main card
        self.main_frame = Frame(
            self.bg_label,
            bg="#0a192f"
        )
        self.main_frame.place(
            relx=0.5,
            rely=0.5,
            anchor=CENTER,
            width=700,
            height=500
        )

        # Heading
        heading = Label(
            self.main_frame,
            text="Need Help?",
            font=("Segoe UI", 26, "bold"),
            bg="#0a192f",
            fg="#00ffff"
        )
        heading.pack(pady=20)

        # Email
        email_label = Label(
            self.main_frame,
            text="Email: " + self.email,
            font=("Segoe UI", 14, "bold"),
            bg="#0a192f",
            fg="white"
        )
        email_label.pack(pady=10)

        # Buttons
        btn_frame = Frame(
            self.main_frame,
            bg="#0a192f"
        )
        btn_frame.pack(pady=10)

        self.create_btn(
            btn_frame, "Copy Email",
            self.copy_email, 0
        )

        self.create_btn(
            btn_frame, "Open Gmail",
            self.open_gmail, 1
        )

        # AI Assistant heading
        chat_label = Label(
            self.main_frame,
            text="AI Assistant",
            font=("Segoe UI", 16, "bold"),
            bg="#0a192f",
            fg="#00ffff"
        )
        chat_label.pack(pady=10)

        # Chat display
        self.chat_box = Text(
            self.main_frame,
            height=6,
            width=70,
            bg="#020c1b",
            fg="white",
            insertbackground="white",
            wrap=WORD
        )
        self.chat_box.pack()

        # User input
        self.entry = Entry(
            self.main_frame,
            width=50,
            font=("Segoe UI", 11)
        )
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.reply())

        # Send button
        send_btn = Button(
            self.main_frame,
            text="Send",
            command=self.reply,
            bg="#00ffff",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )
        send_btn.pack()

        # Animation settings
        self.colors = [
            "#00ffff",
            "#00ccff",
            "#0099ff",
            "#00ccff"
        ]
        self.i = 0

        self.animate()

    # ================= BUTTON CREATION =================
    def create_btn(self, frame, text, cmd, col):
        btn = Button(
            frame,
            text=text,
            command=cmd,
            font=("Segoe UI", 11, "bold"),
            bg="#00ffff",
            fg="black",
            width=15,
            cursor="hand2"
        )
        btn.grid(row=0, column=col, padx=10)

        btn.bind(
            "<Enter>",
            lambda event: btn.config(bg="#00cccc")
        )
        btn.bind(
            "<Leave>",
            lambda event: btn.config(bg="#00ffff")
        )

    # ================= AI REPLY =================
    def reply(self):
        user = self.entry.get().strip()

        if not user:
            msg.showwarning(
                "Empty Message",
                "Please enter your question."
            )
            return

        self.chat_box.insert(
            END, "You: " + user + "\n"
        )

        question = user.lower()

        if "error" in question or "problem" in question:
            response = (
                "Try restarting the system, checking "
                "camera permissions, and reading the error message."
            )

        elif "email" in question or "contact" in question:
            response = (
                "You can contact us at: " + self.email
            )

        elif "camera" in question:
            response = (
                "Check whether your camera is connected "
                "and camera permissions are enabled."
            )

        elif "image" in question or "photo" in question:
            response = (
                "Check that the image exists in the "
                "college_images folder and its filename is correct."
            )

        else:
            response = (
                "Our help center can assist you. "
                "Please describe your issue in more detail."
            )

        self.chat_box.insert(
            END, "AI: " + response + "\n\n"
        )

        self.chat_box.see(END)
        self.entry.delete(0, END)

    # ================= COPY EMAIL =================
    def copy_email(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.email)
        self.root.update()

        msg.showinfo(
            "Copied",
            "Email copied to clipboard!"
        )

    # ================= OPEN GMAIL =================
    def open_gmail(self):
        webbrowser.open("https://mail.google.com/")

    # ================= GLOW ANIMATION =================
    def animate(self):
        if not self.root.winfo_exists():
            return

        try:
            self.glow.config(
                bg=self.colors[self.i]
            )

            self.i = (
                self.i + 1
            ) % len(self.colors)

            self.root.after(300, self.animate)

        except TclError:
            pass


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = Help_Support(root)
    root.mainloop()
