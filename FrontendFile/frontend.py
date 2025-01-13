from tkinter import Tk, Label, Button, Text, Frame, Toplevel,PhotoImage, END
from datetime import datetime
import threading
import time
import sys
import os
from PIL import Image, ImageTk  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import main2
class JarvisUI:
  
    def __init__(self, root,intent_callback = None):
        self.root = root
        self.intent_callback = intent_callback
        self.root.title("Jarvis - Personal Assistant")
        self.root.geometry("1100x940")
        self.root.configure(bg="#1c1c1c")
        self.current_input = ""
        self.is_active = False
        self.conversation = []
         # === Added: Load GIF image ===
        self.gif_image_path = "D:/New_Virtual_Assistant/QNBH.gif"  # Replace with your GIF path
        self.gif_image = None
        if os.path.exists(self.gif_image_path):
            self.gif_image = PhotoImage(file=self.gif_image_path)  # Load the GIF image
        # Header Section
        self.header_frame = Frame(self.root, bg="#292929", height=70)
        self.header_frame.pack(fill="x", side="top")

        self.title_label = Label(
            self.header_frame, text="Jarvis Assistant", font=("Arial", 24, "bold"), fg="#00FF7F", bg="#292929"
        )
        self.title_label.pack(pady=7)

        self.time_label = Label(
            self.header_frame, text="", font=("Arial", 12), fg="white", bg="#292929"
        )
        self.time_label.pack()
        self.update_time()

        # Conversation Area
        self.conversation_frame = Frame(self.root, bg="#1c1c1c")
        self.conversation_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.conversation_display = Text(
            self.conversation_frame, wrap="word", font=("Courier New", 12), bg="#333333", fg="white", state="disabled"
        )
        self.conversation_display.pack(fill="both", expand=True, padx=10, pady=10)

        # Input and Controls
        self.controls_frame = Frame(self.root, bg="#292929")
        self.controls_frame.pack(fill="x", side="bottom")

        self.input_text = Text(
            self.controls_frame, height=3, font=("Courier New", 12), bg="#1c1c1c", fg="white"
        )
        self.input_text.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.send_button = Button(
            self.controls_frame, text="Send", font=("Arial", 12, "bold"), bg="#00FF7F", fg="#1c1c1c",
            command=self.process_user_input
        )
        self.send_button.pack(side="right", padx=10, pady=10)
                # Footer Controls
        self.footer_frame = Frame(self.root, bg="#292929", height=50)
        self.footer_frame.pack(fill="x", side="bottom", pady=5)

        self.start_button = Button(
            self.footer_frame, text="Start", font=("Arial", 12, "bold"), bg="#0078FF", fg="white",
            command=self.start_jarvis
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=5)

        self.stop_button = Button(
            self.footer_frame, text="Stop", font=("Arial", 12, "bold"), bg="#FF0000", fg="white",
            command=self.terminate_ui
        )
        self.stop_button.grid(row=0, column=1, padx=10, pady=5)

        self.clear_button = Button(
            self.footer_frame, text="Clear", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",
            command=self.clear_conversation
        )
        self.clear_button.grid(row=0, column=2, padx=10, pady=5)

        self.accuracy_button = Button(
            self.footer_frame, text="Accuracy", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",
            command=self.show_accuracy_popup
        )
        self.accuracy_button.grid(row=0, column=3, padx=10, pady=5)
        self.status_label = Label(
            self.footer_frame, text="Unactivated", font=("Arial", 12), bg="#292929", fg="red"
        )
        self.status_label.grid(row=0, column=4, padx=10, pady=5)
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

    def process_user_input(self):
        # self.update_status("Recognizing...")
        user_input = self.input_text.get("1.0", END).strip()
        self.input_text.delete("1.0", END)
        if user_input:
            self.add_to_conversation("User", user_input)
            if user_input.lower() == "terminate":
                self.add_to_conversation("System", "Program termination requested but UI will remain active.")
                self.is_active = False
            else:
                threading.Thread(target=self.simulate_response, args=(user_input,), daemon=True).start()
        # self.update_status("Listening")
    def simulate_response(self, user_input):
        # Simulating complex logic or API response
        time.sleep(2)  # Simulate processing delay
        jarvis_response = f"Jarvis processed: {user_input}"
        self.add_to_conversation("Jarvis", jarvis_response)

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
            if speaker == "Jarvis" and message.lower() == "goodbye!":
                break  # Exit condition
        self.is_active = False
        self.update_status("Unactivated")
        self.start_button.config(state="normal")

            
    def terminate_ui(self):
        if self.is_active:
            self.add_to_conversation("System", "Stopping Jarvis...")
            self.is_active = False  # Set to False to signal the thread to stop
            self.update_status("Unactivated")  # Update UI status
            self.start_button.config(state="normal")  # Re-enable the Start button
            self.root.after(1000,self.clear_conversation2)
        else:
            self.add_to_conversation("System", "Jarvis is already stopped.")
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

if __name__ == "__main__":
    root = Tk()
    app = JarvisUI(root)
    root.mainloop()
