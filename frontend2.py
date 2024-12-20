import os
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock
from kivymd.app import MDApp

KV = """
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"

    FloatLayout:
        # Background gif image
        Image:
            source: "D:/New_Virtual_Assistant/QNBH.gif"
            anim_delay: 0.05
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text: "Jarvis"
            text: "The Virtual Assistant"
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.24, "center_y": 0.95}
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: "Custom"
            text_color: (55/255, 15/255, 200/255, 1)

        # Start button
        MDRaisedButton:
            text: "Start"
            pos_hint: {"center_x": 0.1, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.start_jarvis()

        # Stop button
        MDRaisedButton:
            text: "Stop"
            pos_hint: {"center_x": 0.2, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.stop_jarvis()

        # Email button
        MDRaisedButton:
            text: "Send Email"
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.open_email_popup()

        # Conversation label area
        ScrollView:
            id: scroll_view
            size_hint: 0.9, 0.5
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

            MDLabel:
                id: conversation_label
                font_size: "16sp"
                halign: "left"
                valign: "top"
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None 

        # Clear button
        MDRaisedButton:
            text: "Clear"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.clear_conversation()
"""

class MainScreen(Screen):
    pass

class JarvisApp(MDApp):
    file_path = None  # To store file path for email attachments

    def build(self):
        self.title = "Jarvis Assistant"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def start_jarvis(self):
        self.update_conversation("Jarvis started...")

    def stop_jarvis(self):
        self.update_conversation("Stopping Jarvis...")

    def open_email_popup(self):
        # Popup Layout
        content = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Input fields
        self.recipient_input = TextInput(hint_text="Recipient Email", multiline=False)
        self.subject_input = TextInput(hint_text="Subject", multiline=False)
        self.message_input = TextInput(hint_text="Message", multiline=True, size_hint=(1, 0.5))
        
        # File selection button
        file_btn = Button(text="Attach File", size_hint=(1, 0.2))
        file_btn.bind(on_press=self.select_file)

        # Send Button
        send_btn = Button(text="Send Email", size_hint=(1, 0.2))
        send_btn.bind(on_press=self.send_email)

        # Add widgets to popup
        content.add_widget(Label(text="Send Email", font_size="20sp", size_hint=(1, 0.2)))
        content.add_widget(self.recipient_input)
        content.add_widget(self.subject_input)
        content.add_widget(self.message_input)
        content.add_widget(file_btn)
        content.add_widget(send_btn)

        # Create Popup
        self.email_popup = Popup(title="Email Form", content=content, size_hint=(0.8, 0.8))
        self.email_popup.open()

    def select_file(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title="Select a file", content=filechooser, size_hint=(0.9, 0.9))
        
        def on_file_selection(*args):
            self.file_path = filechooser.selection[0] if filechooser.selection else None
            popup.dismiss()
        
        filechooser.bind(on_submit=on_file_selection)
        popup.open()

    def send_email(self, instance):
        # Fetch data
        recipient = self.recipient_input.text
        subject = self.subject_input.text
        message = self.message_input.text

        # Check required fields
        if not recipient or not subject or not message:
            self.update_conversation("All fields are required!")
            return

        # Email sending in a separate thread
        def email_thread():
            try:
                sender_email = "sigdelprabin321@gmail.com"
                password = "omet osmk kavu tlrw"

                # Email Setup
                email_message = MIMEMultipart()
                email_message["From"] = sender_email
                email_message["To"] = recipient
                email_message["Subject"] = subject
                email_message.attach(MIMEText(message, "plain"))

                # File attachment
                if self.file_path:
                    with open(self.file_path, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(self.file_path)}")
                    email_message.attach(part)

                # SMTP Connection
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient, email_message.as_string())
                server.quit()

                Clock.schedule_once(lambda dt: self.update_conversation("Email sent successfully!"))

            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_conversation(f"Failed to send email: {str(e)}"))

        threading.Thread(target=email_thread, daemon=True).start()
        self.email_popup.dismiss()

    def update_conversation(self, text):
        label = self.root.get_screen("main").ids.conversation_label
        label.text += f"\n{text}"
        label.height = label.texture_size[1]

    def clear_conversation(self):
        label = self.root.get_screen("main").ids.conversation_label
        label.text = "Jarvis: Hello! How can I assist you today?"

if __name__ == "__main__":
    JarvisApp().run()
