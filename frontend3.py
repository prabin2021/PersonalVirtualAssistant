import threading
from kivy.metrics import dp
from main import *
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
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
            font_style: "H4"  # Predefined font style for titles
            halign: "center"  # Align the text to the center
            pos_hint: {"center_x": 0.24, "center_y": 0.95}  # Adjust position near the top
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: "Custom"  # Enable custom color
            text_color: (55/255, 15/255, 200/255, 1)  # Gold-like color (RGBA)

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

        # Password button
        MDRaisedButton:
            text: "Password"
            pos_hint: {"center_x": 0.75, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.stop_jarvis()

        # Face sample button
        MDRaisedButton:
            text: "Face Sample"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.collect_face_sample()


        # Conversation label area
        ScrollView:
            id: scroll_view
            size_hint: 0.9, 0.5
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

            MDLabel:
                id: conversation_label
                font_size: "16sp"
                halign: "left"
                valign: "top"  # Align text to the top
                size_hint_y: None
                height: self.texture_size[1]  # Dynamically adjust height
                text_size: self.width, None 

        # Clear button
        MDRaisedButton:
            text: "Clear"
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            size_hint: None, None
            size: dp(120), dp(50)
            on_press: app.clear_conversation()
"""

class MainScreen(Screen):
    pass

class JarvisApp(MDApp):
    def build(self):
        self.title = "Jarvis Assistant"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def start_jarvis(self):
        def jarvis_thread():
            facestatus = faceverify(status="True")
            if facestatus:
                greet_user()
                try:
                    for sender, message in main():  # Iterate through interactions one by one
                        # Update the UI from a separate thread
                        Clock.schedule_once(lambda dt: self.update_conversation(f"{sender}: {message}"))
                        if message.lower() == "goodbye!":  # Exit the loop on "goodbye"
                            break
                except Exception as e:
                    Clock.schedule_once(lambda dt: self.update_conversation(f"Error: {e}"))
            else:
                Clock.schedule_once(lambda dt: self.update_conversation("Face not verified. Please try again."))
                speak("Face not verified. Please try again.")

        # Start the thread
        threading.Thread(target=jarvis_thread, daemon=True).start()



    def stop_jarvis(self):
        self.update_conversation("Stopping Jarvis...")

    def collect_face_sample(self):
        self.update_conversation("Collecting face sample...")

    def update_conversation(self, text):
        def _update(dt):
            conversation_label = self.root.get_screen("main").ids.conversation_label
            conversation_label.text += f"\n{text}"
            conversation_label.height = conversation_label.texture_size[1]
        
        Clock.schedule_once(_update)




    def clear_conversation(self):
        conversation_label = self.root.get_screen("main").ids.conversation_label
        conversation_label.text = "Jarvis: Hello! How can I assist you today?"

if __name__ == "__main__":
    JarvisApp().run()
