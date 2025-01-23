import pyautogui as pi
import time
import pygetwindow as gw
def open_whatsapp():
    from main import speak
    from main import take_user_input
    # pi.hotkey('win','up')
    # pi.moveTo(750,1050,1)
    pi.press('win')
    time.sleep(1)
    pi.typewrite("whatsapp")
    time.sleep(1)
    # # pi.moveTo(730,270,1)
    pi.press('enter')
    time.sleep(1)
    open_windows = gw.getAllTitles()
    print(open_windows)
    for window in open_windows:
        if "WhatsApp" in window:
            speak("Do you want to send message to anyone sir? If yes whom do you want to send?")
            choice = take_user_input()
            if any(keyword in choice.lower() for keyword in ("yes","yeah","i had to","can you open","can i see","i need to","search for","can you search","can you provide",
                                                            "search for the name","i have to","look for","seek for","search for","can you find","will you","can i have","search by typing")if choice is not None):
                speak("Ok sir.")
                start_keywords = ["search for"," seek for","look for", "find", "to", "about","at","from","with", "for", "of", "by", "too","search", "on", "in", "off"]
                words = choice.lower().split()
                search_query = ""
                # # Iterate over words to extract search query
                for i, word in enumerate(words):
                    if word in start_keywords:
                        search_query = " ".join(words[i + 1:])
                
                pi.hotkey('ctrl','f')
                time.sleep(1)
                pi.write(search_query)
                time.sleep(1)
                # pi.moveTo(200,240)
                speak("Is this the person whom you want to connect?")
                person = take_user_input()
                if any(keyword in person.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","yep","click")if person is not None):
                    pi.press("tab")
                    time.sleep(1)
                    pi.press("enter")
                    speak("Can you say your message sir?")
                    message = take_user_input()
                    pi.write(message)
                    speak("Can i send it sir?")
                    final_ans = take_user_input()
                    if any(keyword in final_ans.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","ok","you can send it","let's go","ok you can","yes you can")if final_ans is not None):
                        pi.press("enter")
                        speak(f"Message sent sucessfully.")
                        return "Whatsapp message sent sucessfully"
                    else:
                        speak("Ok sir, message discarded.")
                        return "Whatsapp message discarded"
                else:
                    speak("Sorry sir, I couldn't find the person. You can search manually from here.")
                    return "Whatsapp Opened"
            else:
                speak("Ok as your wish sir.")
                return "Whatsapp Opened"
        
    speak("PLease install whatsapp applications first")
    return "Whatsapp is not installed on your device"


def send_whatsapp_message():
    from main import speak
    from main import take_user_input
    pi.press('win')
    pi.typewrite("whatsapp")
    time.sleep(1)
    pi.press('enter')
    time.sleep(1)
    open_windows = gw.getAllTitles()
    print(open_windows)
    for window in open_windows:
        if "WhatsApp" in window:
            speak("Whom do you want to send message sir?")
            choice = take_user_input()
            if any(keyword in choice.lower() for keyword in ("yes","yeah","i had to","can you open","can i see","i need to","search for","can you search","can you provide",
                                                            "search for the name","i have to","look for","seek for","search for","can you find","will you","can i have","search by typing","i want to")if choice is not None):
                speak("Ok sir, I am searching.")
                start_keywords = ["search for"," seek for","look for", "find", "to", "about","at","from","with", "for", "of", "by", "too","search", "on", "in", "off","name"]
                words = choice.lower().split()
                search_query = ""
                # # Iterate over words to extract search query
                for i, word in enumerate(words):
                    if word in start_keywords:
                        search_query = " ".join(words[i + 1:])
                
                pi.hotkey('ctrl','f')
                pi.write(search_query)
                time.sleep(1)
                speak("Is this the person whom you want to connect with?")
                person = take_user_input()
                if any(keyword in person.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","yep","click","you can","right")if person is not None):
                    pi.press("tab")
                    time.sleep(1)
                    pi.press("enter")
                    speak("Can you say your message sir?")
                    message = take_user_input()
                    pi.write(message)
                    speak("Can i send it sir?")
                    final_ans = take_user_input()
                    if any(keyword in final_ans.lower() for keyword in ("yes","yeah","sure","of course","off course","ofcourse","okay","okey","yep","click","you can","right")if final_ans is not None):
                        pi.press("enter")
                        speak(f"Message sent sucessfully.")
                        return "Whatsapp message sent sucessfully"
                    else:
                        speak("Ok sir, message discarded.")
                        return "Whatsapp message discarded"
                else:
                    speak("Sorry sir, I couldn't find the person. You can search manually from here.")
                    return "Whatsapp Opened"

            else:
                speak("Sorry sir, I couldn't find the person. You can search manually from here.")
                return "Automation of message sending  discarded"

    
    speak("PLease install whatsapp applications first")
    return "Whatsapp is not installed on your device"