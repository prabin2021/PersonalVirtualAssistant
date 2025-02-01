import pyautogui as pi
import time
import pygetwindow as gw
def open_discord():
    from main import speak
    pi.press('win')
    time.sleep(1)
    pi.typewrite("discord")
    time.sleep(1)
    pi.press('enter')
    time.sleep(1)
    open_windows = gw.getAllTitles()
    for window in open_windows:
        if "Discord" in window:
            return "Whatsapp Opened"
    speak("PLease install discord applications first")
    return "Discord is not installed on your device"