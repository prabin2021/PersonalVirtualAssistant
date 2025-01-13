from tkinter import Tk, Label, Button, Text, Frame, Toplevel, StringVar, END
from datetime import datetime
import threading
import time
import sys
from main import main2

class FuturisticJarvisUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis - Personal Assistant")
        self.root.geometry("1100x900")
        self.root.configure(bg="#1c1c1c")

        self.is_active = False
        self.conversation = []

        # Header Section
        self.header_frame = Frame(self.root, bg="#292929", height=70)
        self.header_frame.pack(fill="x", side="top")

        self.title_label = Label(
            self.header_frame, text="Jarvis Assistant", font=("Arial", 20, "bold"), fg="#00FF7F", bg="#292929"
        )
        self.title_label.pack(pady=10)

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
            self.footer_frame, text="Show Accuracy", font=("Arial", 12, "bold"), bg="#FFA500", fg="white",
            command=self.show_accuracy_popup
        )
        self.accuracy_button.grid(row=0, column=3, padx=10, pady=5)

       

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S | %A, %d %B %Y")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def process_user_input(self):
        user_input = self.input_text.get("1.0", END).strip()
        self.input_text.delete("1.0", END)
        if user_input:
            self.add_to_conversation("User", user_input)
            if user_input.lower() == "terminate":
                self.add_to_conversation("System", "Program termination requested but UI will remain active.")
                self.is_active = False
            else:
                threading.Thread(target=self.simulate_response, args=(user_input,), daemon=True).start()

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
            self.is_active = True
            self.add_to_conversation("System", "Jarvis is now active.")
            print("Calling main2 function...")  # Debugging line
            
            # Start the generator function in a separate thread
            threading.Thread(target=self.run_jarvis, daemon=True).start()

    def run_jarvis(self):
        for speaker, message in main2():
            self.add_to_conversation(speaker, message)
            if speaker == "Jarvis" and message.lower() == "goodbye!":
                break  # Exit condition

            


    def terminate_ui(self):
        self.add_to_conversation("System", "Terminating UI and Program.")
        self.root.quit()
        sys.exit()

    def clear_conversation(self):
        self.conversation = []
        self.conversation_display.config(state="normal")
        self.conversation_display.delete("1.0", END)
        self.conversation_display.config(state="disabled")

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
    app = FuturisticJarvisUI(root)
    root.mainloop()
