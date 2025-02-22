import speech_recognition as sr
import urllib.parse
import subprocess

def extract_search_query(query):
        start_keywords = ["search for","find me","search","for"," seek for","look for", "find", "search that",
                           "about","search about","show me","watch","i want to","i need"]
        words = query.lower().split()
        search_query = ""
        for i, word in enumerate(words):
            if word in start_keywords:
                search_query = " ".join(words[i + 1:])
        return search_query

def search_youtube(query):
            from main import speak
            try:
                speak("Okay sir,I am working for it.")
                base_url = "https://www.youtube.com/results?search_query="
                search_query = extract_search_query(query)
                print("Search query:",search_query)
                query_encoded = urllib.parse.quote(search_query)
                search_url = base_url + query_encoded
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
                subprocess.Popen([chrome_path, search_url])
            except sr.RequestError:
                speak("Sorry, I can't perform this action right now")
            except Exception as e:
                print("An error occurred:", e)
            return "For query :", search_query , "youtube search is done"

def open_youtube():
        from main import speak,take_user_input
        try:
            speak("Okay sir,I am working for it.")
            base_url = "https://www.youtube.com/"
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            subprocess.Popen([chrome_path,base_url])
            speak("Would you like to watch something specific on YouTube?")
            userquery = take_user_input()
            youtube_searched = False
            if userquery == "exit":
                return "Exit command detected"
            start_keywords = ["i want","search for","search","for"," seek for","look for", "find", "find me","search that", "about","search about","show me","watch","i need","i want to","play","can you play"]
            for keyword in start_keywords:
                if keyword in userquery:
                    if not youtube_searched:
                        search_youtube(userquery)
                        youtube_searched = True
        except sr.RequestError:
            speak("Sorry, I can't perform this action right now")
            return "An error occurred:"
        except Exception as e:
            return "An error occurred:", e
        return "Youtube opened"