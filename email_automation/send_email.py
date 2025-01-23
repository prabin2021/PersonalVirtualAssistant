# import os
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import smtplib

# def send_email():
#         from main import speak
#         from main import take_user_input
#         recipient_done = False
#         subject_done = False
#         message_done = False
#         try:
#             speak("Sure sir. I need recipient's email address.")
#             speak("How would you like to provide recipient's email address?")
#             choice_in_recipient = take_user_input()
#             if choice_in_recipient != None:
#                 if any(keyword in choice_in_recipient.lower() for keyword in ("tell", "say","mouth","speak","announce","provide")):
#                     if "exit" in choice_in_recipient.lower():
#                             return 
#                     print("Recipient address: ")
#                     recipient_email = take_user_input()
#                     recipient_email = recipient_email.strip().lower()
#                     recipient_email = recipient_email.replace(" ", "")
#                     print("Recipient address: ", recipient_email)
#                     recipient_done = True
#                 elif any(keyword in choice_in_recipient.lower() for keyword in ("type", "write","writing","typing")):
#                     if "exit" in choice_in_recipient.lower():
#                             return 
#                     recipient_email = input("Recipient's Email Address: ")
#                     print("Recipient address: ", recipient_email)
#                     recipient_done = True
#                 else:
#                     speak("I didn't understand sir, you can provide me email address either by typing or by saying it.")
#                     return
#             if recipient_done == True:
#                 speak("I need subject of your email.")
#                 speak("How would you like to provide subject?")
#                 choice_in_subject = take_user_input()
#                 if choice_in_subject != None:
#                     if any(keyword in choice_in_subject.lower() for keyword in ("tell", "say","mouth","speak","announce","provide")):
#                         if "exit" in choice_in_subject.lower():
#                             return 
#                         print("Listening for subject...")
#                         subject =  take_user_input()
#                         print("Your Subject: ", subject)
#                         subject_done = True
#                     elif any(keyword in choice_in_subject.lower() for keyword in ("type", "write","writing","typing")):
#                         if "exit" in choice_in_subject.lower():
#                             return 
#                         subject = input("Write your subject: ")
#                         print("Subject: ", subject)
#                         subject_done = True
#                     else:
#                         speak("Unable to create subject of your email sir. Please try to send again.")
#                         return
#             else:
#                         speak("Unable to understand your given recipient address. Please try to send again.")
#                         return
#             if subject_done == True:
#                 speak("How will you provide me the message sir?")
#                 choice_in_message = take_user_input()
#                 if choice_in_message != None:
#                     if any(keyword in choice_in_message.lower() for keyword in ("tell", "say","mouth","speak","announce","provide")):
#                         if "exit" in choice_in_message.lower():
#                             return 
#                         print("Listening for message...")
#                         message =  take_user_input()
#                         print("Message: ", message)
#                         message_done = True
#                     elif any(keyword in choice_in_message.lower() for keyword in ("type", "write","writing","typing")):
#                         if "exit" in choice_in_message.lower():
#                             return 
#                         message = input("Write your message: ")
#                         print("Message: ", message)
#                         message_done = True
#                 else:
#                     speak("Unable to create message of your email sir.")
#                     return
#             else:
#                 speak("Unable to understand your given subject. Please try to send again.")
#                 return
#             if message_done:
#             # Your email credentials and SMTP server details
#                 sender_email = "sigdelprabin321@gmail.com"
#                 ohoo = "omet osmk kavu tlrw"
#                 smtp_server = "smtp.gmail.com"
#                 smtp_port = 587  # or 465 for SSL
#                 # Create MIMEMultipart message
#                 message_content = MIMEMultipart()
#                 message_content['From'] = sender_email
#                 message_content['To'] = recipient_email
#                 message_content['Subject'] = subject
#                 # Attach message content
#                 message_content.attach(MIMEText(message, 'plain'))
#                 # Attachment functionality
#                 speak("Do you have anything to attach here sir ?")
#                 attach_choice = take_user_input()
#                 if attach_choice != None:
#                     if any(keyword in attach_choice.lower() for keyword in ("yeah", "off course","of course","yes","need to attach","have to attach","want to attach")):
#                         print("Please provide the file path sir")
#                         file_path = input("Enter your file path:\n")
#                         if os.path.exists(file_path):
#                             # Open the file in binary mode
#                             with open(file_path, 'rb') as attachment:
#                                 # Add file as application/octet-stream
#                                 # Email client can usually download this automatically as attachment
#                                 part = MIMEBase('application', 'octet-stream')
#                                 part.set_payload(attachment.read())

#                             # Encode file in ASCII characters to send via email
#                             encoders.encode_base64(part)
#                             # Add header as key/value pair to attachment part
#                             part.add_header(
#                                 'Content-Disposition',
#                                 f'attachment; filename= {os.path.basename(file_path)}'
#                             )
#                             # Add attachment to message and convert message to string
#                             message_content.attach(part)
#                         else:
#                             print("File not found. Attachment skipped.")

#                 # Create SMTP server connection
#                 server = smtplib.SMTP(smtp_server, smtp_port)
#                 server.starttls()  # Secure the connection
#                 server.login(sender_email, ohoo)  # Login to your email account

#                 # Construct the email message
#                 email_message = message_content.as_string()

#                 speak("Please confirm the email content. Subject: {}. Message: {}. Do you want to proceed? (Yes or No)".format(subject, message))
#                 confirm = take_user_input()
#                 if confirm != None:
#                     if any(keyword in confirm.lower() for keyword in ("yeah", "sure","ok","yes","okay","you can send","yes send")):
#                         server.sendmail(sender_email, recipient_email, email_message)
#                         server.quit()
#                         print("Sir, Email is sent successfully!")
#                         speak("Sir, Email is sent successfully!")
#                     else:
#                         print("Email sending cancelled.")
#                         speak("Email sending cancelled.")

#         except Exception as e:
#                 print("An error occurred while sending the email:", e)
#                 speak("Sorry, I couldn't send the email. Please try again.")

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
            sender_password = "YOue email specific password"
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
