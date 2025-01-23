from tkinter import Tk, Label, Button, Text,Entry, Frame, Toplevel,PhotoImage, END
from datetime import datetime
import threading
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import main2,main3
class JarvisUI:
  
    def __init__(self, root,intent_callback = None):
        self.root = root
        icon = PhotoImage(file="D:/New_Virtual_Assistant/Images/logo.png")  # Replace with your image file path
        self.root.wm_iconphoto(True, icon)
        self.intent_callback = intent_callback
        self.root.title("Jarvis - Personal Assistant")
        self.root.geometry("1150x950")
        self.root.configure(bg="#1c1c1c")
        self.current_input = ""
        self.is_active = False
        self.conversation = []
        # === Added: Load GIF image ===
        self.gif_image_path = "D:/New_Virtual_Assistant/Images/jarvis.gif"
        self.gif_image = None
        if os.path.exists(self.gif_image_path):
            self.gif_image = PhotoImage(file=self.gif_image_path)  # Load the GIF image
        # Header Section
        self.header_frame = Frame(self.root, bg="#292929", height=70)
        self.header_frame.pack(fill="x", side="top")

        self.title_label = Label(
            self.header_frame, text="Personal Assistant", font=("Consolas", 24, "bold"), fg="#00FF7F", bg="#292929",
        )
        self.title_label.pack(pady=7)

        self.time_label = Label(
            self.header_frame, text="", font=("Arial", 12), fg="white", bg="#292929"
        )
        self.time_label.pack()
        self.update_time()

        # Conversation Area
        self.conversation_frame = Frame(self.root, bg="#1c1c1c", bd=2,relief="solid", highlightbackground="RED", highlightthickness=2)
        self.conversation_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.conversation_display = Text(
            self.conversation_frame, wrap="word", font=("Courier New", 12), bg="#333333", fg="white", state="disabled"
        )
        self.conversation_display.pack(fill="both", expand=True, padx=10, pady=10)

        self.footer_frame = Frame(self.root, bg="#292929", height=50 ,bd=2,relief="solid", highlightbackground="RED", highlightthickness=2)
        self.footer_frame.pack(fill="x", side="bottom", pady=5)

        self.start_button = Button(
            self.footer_frame, text="Start", font=("Arial", 12, "bold"), bg="#00FF7F", fg="white",border="10px 100px / 120px 100px",
            command=self.start_jarvis
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=5)

        self.stop_button = Button(
            self.footer_frame, text="Stop", font=("Arial", 12, "bold"), bg="#FF0000", fg="white",border="10px 100px / 120px 100px",
            command=self.terminate_ui
        )
        self.stop_button.grid(row=0, column=1, padx=10, pady=5)

        self.clear_button = Button(
            self.footer_frame, text="Clear", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",border="10px 100px / 120px 100px",
            command=self.clear_conversation
        )
        self.clear_button.grid(row=0, column=2, padx=10, pady=5)

        self.accuracy_button = Button(
            self.footer_frame, text="Accuracy", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",border="10px 100px / 120px 100px",
            command=self.show_accuracy_popup
        )
        self.accuracy_button.grid(row=0, column=3, padx=10, pady=5)
        self.status_label = Label(
            self.footer_frame, text="Unactivated", font=("Arial", 12), bg="#292929", fg="red"
        )
        self.status_label.grid(row=0, column=4, padx=10, pady=5)
        
        self.password_button = Button(
            self.footer_frame, text="Password", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",border="10px 100px / 120px 100px",
            command=self.handle_password
        )
        self.password_button.grid(row=0, column=5, padx=10, pady=5)

        self.face_button = Button(
            self.footer_frame, text="Change Face", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",border="10px 100px / 120px 100px",
            command=self.change_face_sample
        )
        self.face_button.grid(row=0, column=6, padx=10, pady=5)

        self.terminate_button = Button(
            self.footer_frame, text="Terminate", font=("Arial", 12, "bold"), bg="#A40000", fg="white",border="10px 100px / 120px 100px",
            command=sys.exit
        )
        self.terminate_button.grid(row=0, column=7, padx=10, pady=5)

        if self.gif_image:
            self.add_gif_to_conversation()

    def add_gif_to_conversation(self):
        """Add the GIF image to the conversation display."""
        if self.gif_image:
            self.conversation_display.config(state="normal")
            self.conversation_display.image_create("end", image=self.gif_image)
            self.conversation_display.config(state="disabled")


    def remove_gif_from_conversation(self):
        """Remove the GIF image from the conversation display."""
        self.conversation_display.config(state="normal")
        self.conversation_display.delete("1.0", "end")
        self.conversation_display.config(state="disabled")

    def update_status(self, status_message):
    # Change the color based on the status message
        if status_message.lower() == "activated":
            self.status_label.config(text=status_message, fg="green")  # Set text to green for "Activated"
        elif status_message.lower() == "unactivated":
            self.status_label.config(text=status_message, fg="red")  # Set text to red for "Unactivated"
        else:
            self.status_label.config(text=status_message, fg="red")  # Default color for other statuses
        
        self.root.update_idletasks()  # Ensure the UI updates immediately

    def update_time(self):
    # Get the current time
        current_time = datetime.now().strftime("%H %M %S")  # Without separators
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Blinking colon animation
        separator = ":" if int(datetime.now().strftime("%S")) % 2 == 0 else " "  # Blink every second
        formatted_time = f"🕒 {current_time[:2]}{separator}{current_time[3:5]}{separator}{current_time[6:]}"
        formatted_date = f"📅 {current_date}"

        self.time_label.config(
            text=f"{formatted_time}\n{formatted_date}",
            font=("Helvetica", 16, "bold"),
            fg="#FFD700",
            bg="#292929",
        )

        self.root.after(500, self.update_time)  # Refresh every 500ms for smooth animation

    def add_to_conversation(self, sender, message):
        self.conversation.append(f"{sender}: {message}")
        self.conversation_display.config(state="normal")
        self.conversation_display.insert(END, f"{sender}: {message}\n")
        self.conversation_display.config(state="disabled")
        self.conversation_display.see(END)

    def start_jarvis(self):
        if not self.is_active:
            self.update_status("Activated")
            self.is_active = True
            self.add_to_conversation("System", "Jarvis is now active.")
            self.remove_gif_from_conversation()
            # Start the assistant in a separate thread
            threading.Thread(target=self.run_jarvis, daemon=True).start()
            self.start_button.config(state="disabled")  # Disable Start button while active
    def run_jarvis(self):
        self.update_status("Activated")
        for speaker, message in main2():
            if not self.is_active:
                break
            self.add_to_conversation(speaker, message)
            if isinstance(message, str) and speaker == "Jarvis" and message.lower() == "goodbye!":
                break
        self.is_active = False
        self.update_status("Unactivated")
        self.start_button.config(state="normal")

    def start_jarvis2(self):
        if not self.is_active:
            self.update_status("Activated")
            self.is_active = True
            self.add_to_conversation("System", "Jarvis is now active.")
            self.remove_gif_from_conversation()
            # Start the assistant in a separate thread
            threading.Thread(target=self.run_jarvis2, daemon=True).start()
            self.start_button.config(state="disabled")  # Disable Start button while active
    def run_jarvis2(self):
        self.update_status("Activated")
        for speaker, message in main3():
            if not self.is_active:
                break
            self.add_to_conversation(speaker, message)
            if isinstance(message, str) and speaker == "Jarvis" and message.lower() == "goodbye!":
                break
        self.is_active = False
        self.update_status("Unactivated")
        self.start_button.config(state="normal")
    def change_face_samples(self):
        if not self.is_active:
            self.update_status("Changing face sample")
            self.remove_gif_from_conversation()
            self.add_to_conversation("System", "Changing your face samples...")
            self.add_to_conversation("System", "Please look in camera")
            # Start the assistant in a separate thread
            threading.Thread(target=self.change_sample, daemon=True).start()
    def change_sample(self):
        from Face_Verification.takesample import take_sample
        take_sample()
        self.add_to_conversation("System", "Face samples changed sucessfully.")
        self.update_status("Unactivated")
    def terminate_ui(self):
        if self.is_active:
            self.add_to_conversation("System", "Stopping Jarvis...")
            self.is_active = False  # Set to False to signal the thread to stop
            self.update_status("Unactivated")  # Update UI status
            self.start_button.config(state="normal")  # Re-enable the Start button
            self.root.after(1000,self.clear_conversation2)
        else:
            # self.add_to_conversation("System", "Jarvis is stopped.")
            self.root.after(1000,self.clear_conversation2)

    def clear_conversation(self):
        self.conversation = []
        self.conversation_display.config(state="normal")
        self.conversation_display.delete("1.0", END)
        self.conversation_display.config(state="disabled")
    def clear_conversation2(self):
        self.conversation = []
        self.conversation_display.config(state="normal")
        self.conversation_display.delete("1.0", END)
        self.conversation_display.config(state="disabled")
        self.root.after(1000,self.add_gif_to_conversation)
        
    def show_accuracy_popup(self):
        accuracy = "Face Recognition: 95%\nIntent Classification: 92%\nText Translation: 89%"
        popup = Toplevel(self.root)
        popup.title("Accuracy Metrics")
        popup.geometry("300x200")
        popup.configure(bg="#292929")

        accuracy_label = Label(
            popup, text=accuracy, font=("Arial", 12), bg="#292929", fg="white", justify="left"
        )
        accuracy_label.pack(pady=20, padx=20)

        close_button = Button(
            popup, text="Close", font=("Arial", 12), bg="#FF0000", fg="white",
            command=popup.destroy
        )
        close_button.pack(pady=10)
    def custom_hash(self,password):
                """Custom hashing algorithm to encrypt the password."""
                hash_value = 0
                prime = 31  # Use a small prime number for hashing

                # Loop through each character in the password manually
                position = 1
                for char in password:
                    # Calculate ASCII value manually
                    ascii_value = 0
                    for byte in char.encode("utf-8"):  # Convert character to its raw byte value
                        ascii_value += byte

                    # Custom multiplication logic: ASCII value * position * prime
                    hash_value += ascii_value * position * prime
                    position += 1

                # Manually convert to hexadecimal
                hex_result = ""
                hex_characters = "0123456789abcdef"
                while hash_value > 0:
                    remainder = hash_value % 16
                    hex_result = hex_characters[remainder] + hex_result
                    hash_value //= 16

                return hex_result
    
    def handle_password(self):
        if not self.is_active:
            """Handle password verification or setup."""
            popup = Toplevel(self.root)
            popup.title("Enter Password")
            popup.geometry("500x150")
            popup.configure(bg="#292929")

            Label(popup, text="Enter Password To Proceed:", font=("Arial", 12), bg="#292929", fg="white").pack(pady=10)
            password_entry = Entry(popup, show="*", font=("Arial", 12), bg="white", fg="black")
            password_entry.pack(pady=5)
            

            def check_password():
                entered_password = password_entry.get()
                file_path = "D:/New_Virtual_Assistant/Password/password.txt"
                hashed_entered_password = self.custom_hash(entered_password)
                if os.path.exists(file_path):
                    # Check if the password matches
                    with open(file_path, "r") as file:
                        stored_password = file.read().strip()
                        if hashed_entered_password == stored_password:
                            popup.destroy()
                            self.clear_conversation()
                            self.start_jarvis2()  # Call main function
                            self.add_to_conversation("System", "Password verified! Activating system...")
                        else:
                            self.clear_conversation()
                            self.add_to_conversation("System", "Incorrect password!")
                else:
                    with open(file_path, "w") as file:
                        file.write(hashed_entered_password)
                    popup.destroy()
                    self.clear_conversation()
                    self.start_jarvis2()  # Call main function
                    self.add_to_conversation("System", "Password set! Activating system...")

            Button(
                popup, text="Submit", font=("Arial", 12,"bold"), bg="#00FF7F", fg="white", command=check_password
            ).pack(pady=10)
    def change_face_sample(self):
        if not self.is_active:
            """Handle password verification or setup."""
            popup = Toplevel(self.root)
            popup.title("Enter Password To Change Face Samples")
            popup.geometry("500x150")
            popup.configure(bg="#292929")
            Label(popup, text="Enter Password:", font=("Arial", 12), bg="#292929", fg="white").pack(pady=10)
            password_entry = Entry(popup, show="*", font=("Arial", 12), bg="white", fg="black")
            password_entry.pack(pady=5)

            def check_password():
                entered_password = password_entry.get()
                file_path = "D:/New_Virtual_Assistant/Password/password.txt"
                hashed_entered_password = self.custom_hash(entered_password)
                if os.path.exists(file_path):
                    # Check if the password matches
                    with open(file_path, "r") as file:
                        stored_password = file.read().strip()
                        if hashed_entered_password == stored_password:
                            popup.destroy()
                            self.clear_conversation()
                            self.change_face_samples()
                        else:
                            self.clear_conversation()
                            self.add_to_conversation("System", "Incorrect password!")
                else:
                    # Create the file and store the password
                    with open(file_path, "w") as file:
                        file.write(hashed_entered_password)
                    popup.destroy()
                    self.clear_conversation()
                    self.change_face_samples()  # Call main function


            Button(
                popup, text="Submit", font=("Arial", 12,"bold"), bg="#00FF7F", fg="white", command=check_password
            ).pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    app = JarvisUI(root)
    root.mainloop()
