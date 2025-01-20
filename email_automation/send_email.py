
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from tkinter import Toplevel, Label, Button, Entry, Text, StringVar, filedialog, END

def send_email():
    from main import speak, take_user_input

    def send_email_logic(recipient_email, subject, message, file_path):
        try:
            sender_email = "Your email"
            sender_password = "Your email specific password"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Create MIMEMultipart message
            email_message = MIMEMultipart()
            email_message['From'] = sender_email
            email_message['To'] = recipient_email
            email_message['Subject'] = subject
            email_message.attach(MIMEText(message, 'plain'))

            # Attach file if provided
            if file_path and os.path.exists(file_path):
                with open(file_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(file_path)}'
                )
                email_message.attach(part)

            # Send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, email_message.as_string())
            server.quit()
            speak("Email sent successfully!")
        except Exception as e:
            speak(f"An error occurred")
            print("Error")

    def open_email_popup():
        def browse_file():
            file_path.set(filedialog.askopenfilename())

        def handle_send():
            recipient_email = recipient_entry.get().strip()
            subject = subject_entry.get().strip()
            message = message_text.get("1.0", END).strip()
            file_path_value = file_path.get().strip()
            popup.destroy()
            send_email_logic(recipient_email, subject, message, file_path_value)

        def handle_cancel():
            popup.destroy()

        popup = Toplevel()
        popup.title("Send Email")
        popup.geometry("400x600")

        Label(popup, text="Recipient Email:").pack(pady=5)
        recipient_entry = Entry(popup, width=50)
        recipient_entry.pack(pady=5)

        Label(popup, text="Subject:").pack(pady=5)
        subject_entry = Entry(popup, width=50)
        subject_entry.pack(pady=5)

        Label(popup, text="Message:").pack(pady=5)
        message_text = Text(popup, height=10, width=50)
        message_text.pack(pady=5)

        file_path = StringVar()
        Button(popup, text="Browse File", command=browse_file).pack(pady=5)
        Label(popup, textvariable=file_path).pack(pady=5)

        Button(popup, text="Send", command=handle_send).pack(side="left", padx=20, pady=10)
        Button(popup, text="Cancel", command=handle_cancel).pack(side="right", padx=20, pady=10)

    speak("Please fill all the fields.")
    open_email_popup()
