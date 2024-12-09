import psutil

def battey_persentage():
        from main import speak

        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        speak(f"the device is running on {percent}% battery power")
        secsleft = battery.secsleft
        time_left_message = ""
        if secsleft == psutil.POWER_TIME_UNLIMITED:
            speak("Battery is fully charged.")
        elif secsleft == psutil.POWER_TIME_UNKNOWN:
            speak("Battery time left is unknown.")
        else:
            hours, remainder = divmod(secsleft, 3600)
            minutes, _ = divmod(remainder, 60)
            time_left_message = f"if you normally use your device then you will be able to use about: {hours} hours and {minutes} minutes sir."
            speak(time_left_message)
        return f"You have percent{percent}in your device{time_left_message}"