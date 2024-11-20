from basic_functions.basic_functionalities import *
from battery_status.battery_check import *
from camera_automation.open_camera import *
from email_automation.send_email import *
from google_automation.google_search import *
from greetings.greeting import *
from jarvis_status.jarvis_mode import *
from joke.jokes_teller import *
from queries_handling_functions.query_handle import *
from routine_handling.routine_sayer import *
from sentiment_analyzer.sentiment_analyze import *
from youtube_automation.search_on_youtube import *
from data_required.dialogues import *
from wikipedia_search_automation.wiki_search import *
from whatsapp_automation.whatsapp_automate import *
from translate_automation.translate import *
from last_activity_automation.last_actitivty_track import *
import pyttsx3
import speech_recognition as sr
import pyautogui
import urllib.parse
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess as sp
import cv2
import smtplib
import tkinter as tk
import pywhatkit as kit
import webbrowser
from datetime import datetime
from sketchpy import library as lib
from random import choice
from PIL import Image, ImageTk
import requests
import wikipedia
import sys
import subprocess
from mtranslate import translate
from colorama import Fore,Style,init
import threading
import psutil
import re
from transformers import pipeline
import logging
import time
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
engine.setProperty('voice', voices[0].id)
logging.basicConfig(level=logging.INFO)
recognizer = sr.Recognizer()
microphone = sr.Microphone()
sentiment_checked = False


listening = True
def toggle_jarwis_mode(mode):
        global listening
        from main import speak
        if mode == "sleep":
            speak("Now I will be in sleeping mode. I won't listen to any commands.")
            listening = False
            print("sleep status",listening)
            return listening
        elif mode == "wakeup":
            speak("I am now awake. Welcome back sir.")
            print("Wake up command detected")
            listening = True
            return listening

def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_user_input():
    with microphone as source:
        print("Listening...\n", end="", flush=True)
        recognizer.adjust_for_ambient_noise(source,duration=1)
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 250
        recognizer.phrase_threshold = 0.3
        recognizer.sample_rate = 48000
        recognizer.dynamic_energy_threshold = True
        recognizer.non_speaking_duration = 0.5
        audio = recognizer.listen(source,5,10)
    query = None
    try:
        
        print("Trying to recognize as Nepali language...")   
        query1 = recognizer.recognize_google(audio, language="ne")
        query_translated = translate(query1,to_language="en")
        print("You said:",query_translated)
        query = query_translated.lower()
    except sr.UnknownValueError:
        try:           
            print("Trying to recognize as English language...")         
            query1 = recognizer.recognize_google(audio, language="en")
            print("You said:",query1)
            query= query1.lower()
        except sr.UnknownValueError:
            print("Unable to recognize...")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service. Please try again.")
            return None
    if not query:
        return None
    
    return query
   
def activate_assistant():
    speak("Sir, I am your virtual assistant Jarvis. Can I activate, sir?")
    activate_command = take_user_input()
    activation_phrases = [
        "yes bro you can activate",
        "okay sure",
        "i need you",
        "let's work together",
        "yes",
        "sure",
        "off course",
        "of course",
        "ofcourse",
        "go ahead",
        "activate now",
        "ok you can",
        "yes you can",
        "switch on",
        "activate and work",
        "you can start",
        "let's start",
        "you can activate",
    ]

    if activate_command is None:
        speak("Assistant not activated. Let me know when you need me, sir.")
        return False
    else:
        if any(phrase in activate_command for phrase in activation_phrases):
            speak("Activating now with face verification sir!")
            import threading
            from Face_Verification.newfaceverify import verifyface
            activity_thread = threading.Thread(target=monitor_activities)
            activity_thread.daemon = True
            activity_thread.start()
            verified = verifyface()
            while verified != True: 
                speak("Face verified sir")  
                pyautogui.press('escape')
                cv2.destroyAllWindows()
                return True
        else:
            speak("Unable to understand.")
            return False

commands = {
    "open_email": [
        "open my email", "check my email", "read my e-mail", "access my inbox", "open e-mail","i need email","launch email","can i have email","show me my email"
    ],
    "send_whatsapp_message": [
        "send a message on WhatsApp", "message someone on WhatsApp", "text on WhatsApp","i want to message through whatsapp"
        "send WhatsApp message", "WhatsApp message","want to text someone through whatsapp"
    ],
    "open_whatsapp": [
        "open WhatsApp", "launch WhatsApp", "start WhatsApp", "access WhatsApp", "can i have whatsapp","i need whatsapp","show whatsapp"
    ],
    "open_command prompt": [
        "open command prompt", "launch command prompt", "start command prompt", "access command prompt", "use social media","can i have command prompt","i need command prompt","show my command prompt"
    ],
    "open_camera": [
        "open camera", "launch camera", "start camera", "access camera", "use social media","can i have camera","i need camera","show my camera"
    ],
    "capture_photo": [
        "click my pictures", "capture photo", "click photos", "capture pictures", "click our picture","click our photos","take the shots"
    ],
    "open_notepad": [
        "open notepad", "launch notepad", "start notepad", "access notepad", "use social media","can i have notepad","i need notepad","show my notepad"
    ],
    "jarwis_status_sleep": [
        "bro sleep now", "sleep for a while", "don't disturb me for a while", "go away", "keep silent","don't make noise","activate sleep mode","can you sleep","leave me alone for a while"
    ],
    "jarwis_status_wakeup": [
        "bro wake up now", "wakeup now", "i need you", "stand up please", "bro start up ","can you wake up","raise up bro","let's work together","wake up"
    ],
    "open_facebook": [
        "open Facebook", "launch Facebook", "start Facebook", "access Facebook", "use social media","can i have facebook","i need facebook","show my facebook"
    ],
    "send_email": [
        "send an email", "send a mail", "e-mail someone", "dispatch an email", "send email to","help me to send email"
    ],
    "tell_joke": [
        "tell me a joke", "tell me some jokes", "say joke", "i want jokes", "provide me some jokes","make me laugh"
    ],
    "translate_text": [
        "translate the text", "convert the text","change the text","change this sentence into another language", "translate the words into another language", "can you convert ", "can you translate this", "convert these sentences","convert this sentences into another language", "translate these sentences"
    ],
    "open_google": [
        "open Google", "launch Google", "start Google", "access Google", " want to use Google","show me google","can i have google  ", "i need google"
    ],
    "search_wikipedia": [
        "search in wikipedia", "search for something in wikipedia", "wikipedia search about", "access information about something through wikipedia", "use wikipedia to search for anything"
    ],
    "search_google": [
        "search in Google", "search for something in Google", "google search Google", "access information about something through Google", "use Google to search for anything","using google search for"
    ],
    "open_youtub": [
        "open YouTube", "launch YouTube", "start YouTube", "watch videos on YouTube", "show YouTube ","can i have youtube ", "i need youtube"
    ],
    "open_calculator": [
        "open calculator", "launch calculator", "start calculator", "access calculator", "open the calculator"
    ],
    "check_battery": [
        "check battery status", "battery percentage", "how much battery is left", "battery level", "what's my battery"
    ],
    "play_game": [
        "play a game", "open a game", "start a game", "launch a game", "let's play a game", "i want game"
    ],
    "open_settings": [
        "open settings", "launch settings", "start settings", "go to settings", "open system settings"
    ],
    "previous_activities": [
        "show my previous activities","what were my previous works", "what we were doing last time", " in which project we were working last time", "want to see my previous tasks", "trace my previous works"
    ],
    "exit": [
        "exit now","you can exit now", "you can terminate now", " shut the system", "shut down your system", "terminate now", "leave now", "will you leave now"
    ],
    "previous_activities": [
        "show my previous activities","what were my previous works", "what we were doing last time", " in which project we were working last time", "want to see my previous tasks", "trace my previous works"
    ],
    "minimize_window": [
        "minimize the window", "can you minimize this window", "minimize my current window", "please minimize the screen", "make the window smaller",
    ],
    "maximize_window": [
        "maximize the window", "can you maximize this window", "maximize now", "please maximize the screen", "make the window full screen", "expand the window"
    ],
    "close_window": [
        "close the window", "can you close this window", "close current window", "please close the screen", "remove this window", " this window"
    ],
    "tell_time": [
        "tell me the time", "what time is it now", "can you tell me the time", "what's the current time", "show the time", "say me the time", "what is time now", "current time please", "can you show me the time", "i need the time"
    ]
}


def generate_dataset_from_commands(commands):
    dataset = []
    for intent, variations in commands.items():
        for command in variations:
            dataset.append({'question': command, 'answer': intent})
    return dataset

lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words]
    print("Tokens:",tokens)
    return ' '.join(tokens)

def check_status(query):
    global sentiment_checked
    if not sentiment_checked:
            sentiment, confidence = analyze_sentiment(query)
            print(f"Your Sentiment: {sentiment}, Your Confidence: {confidence:.2f}")
            if sentiment == 'NEGATIVE' and confidence > 0.7:
                speak("I sense some negativity in your voice. Is everything alright sir?")
            sentiment_checked = True


def get_answer(question, vectorizer, x, dataset):
    
    global listening
    original_question = question
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, x)
    print("similarities:", similarities)
    if similarities.max() < 0.6:
        return "Sorry, I didn't understand that. Could you rephrase?"
    best_match_index = similarities.argmax()
    intent = dataset[best_match_index]['answer']
    print("This is your intent that you will match",intent)
    print(dataset[best_match_index]['answer'])
    
    if intent in intent_to_function and listening:
        func = intent_to_function[intent]
        if callable(func):
            print("Executing command as Jarwis is awake")
            result = func(original_question) if 'lambda' in str(func) else func()
            print(f"Executed command: {intent}")
            return result
    elif not listening and intent == "jarwis_status_wakeup":
        toggle_jarwis_mode("wakeup")
    elif not listening:
        print("Jarvis is sleeping. Discarding command.")
        return "Jarwis is currently in sleep mode."
    else:
            speak("Sorry, I am not trained for this function, sir.")
            return "Sorry, I am not trained for this function."
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    x= vectorizer.fit_transform(corpus)
    print("Vectorizer and x value:" ,vectorizer, x)
    return vectorizer, x

intent_to_function = {
    "open_email": send_email,
    "send_whatsapp_message":lambda query: send_whatsapp_message(query),
    "open_whatsapp": open_whatsapp,
    "open_command_prompt": open_cmd,
    "open_camera": open_camera,
    "capture_photo": capture_photo,
    "open_notepad": open_notepad,
    "jarwis_status_sleep":lambda _: toggle_jarwis_mode("sleep"),
    "jarwis_status_wakeup":lambda _: toggle_jarwis_mode("wakeup"),
    # "open_facebook": open_facebook,
    "send_email": send_email,
    "tell_joke": tell_random_joke,
    "translate_text": translate_text,
    "open_google": open_google,
    "search_wikipedia":lambda query: get_wikipedia_summary(query),
    "search_google":lambda query: search_google(query),
    "open_youtub":lambda query: search_youtube(query),
    "check_battery": battey_persentage,
    "previous_activities": remind_last_activity,
    "minimize_window": minimize_screen,
    "maximize_window": maximize_screen,
    "close_window":close_window,
    "tell_time":tell_time,
    "exit":exit,

}

def mind(text,response_check):
    response_done = response_check
    dataset = generate_dataset_from_commands(commands)
    vectorizer, x = train_tfidf_vectorizer(dataset)
    print(response_done)
    if response_done == False:
        answer = get_answer(text, vectorizer, x, dataset)
        print(answer) 
        return answer
    else:
        # response_done = False
        return
def main():
        # remind_last_activity()      
        while True:
            user_input = take_user_input()
            if user_input:
        
                result_query,response_check = handle_query(user_input)
                result_mind = mind(user_input,response_check)
                if result_mind == "exit":
                    break
            else:
                continue
            response_check = False
if __name__ == "__main__":
    status = activate_assistant()
    if status == True:
        greet_user()
        main()
    else:
        pass