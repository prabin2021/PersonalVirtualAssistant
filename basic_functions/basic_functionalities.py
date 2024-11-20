import pyautogui
import os
import datetime
from datetime import datetime
def open_notepad():
        os.system('start notepad')

def open_cmd():
        os.system('start cmd')
def tell_time():
        from main import speak
        strTime = datetime.now().strftime("%H:%M:%S")
        speak("Sir, the time is " + strTime)
        return strTime
def minimize_screen():
        from main import speak
        speak("Ok sir, I am minimizing it.")
        pyautogui.hotkey('win','down','down')
        return "Window minimized sir"
def maximize_screen():
        from main import speak
        speak("Ok sir, I am maximizing it.")
        pyautogui.hotkey('win','up')
        return "Window maximized sir"
def close_window():
        from main import speak
        speak("Ok sir, I am closing it.")
        pyautogui.hotkey('ctrl','w')
        return "Window closed sir"
def exit():
        from main import speak
        current_hour = datetime.now().hour
        if current_hour >= 21 or current_hour < 6:
                speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
        else:
                speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
        return "exit"

