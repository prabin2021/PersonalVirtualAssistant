import math
from collections import Counter
import re
import pyttsx3
import speech_recognition as sr
from basic_functions.basic_functionalities import *
from battery_status.battery_check import *
from camera_automation.open_camera import *
from greetings.greeting import *
from joke.jokes_teller import *
from queries_handling_functions.query_handle import *
from routine_handling.routine_sayer import *
from sentiment_analyzer.sentiment_analyze import *
from data_required.dialogues import *
from youtube_automation.search_on_youtube import *
from email_automation.send_email import *
from google_automation.google_search import *
from wikipedia_search_automation.wiki_search import *
from whatsapp_automation.whatsapp_automate import *
from translate_automation.translate import *
from last_activity_automation.last_actitivty_track import *
from Face_Verification.face_samples.newfaceverify import *
from Face_Verification.face_samples.takesample import *
from data_required.dataforNLP import *
import tkinter as tk
from mtranslate import translate
import threading
import logging
import types
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[0].id)
logging.basicConfig(level=logging.INFO)
recognizer = sr.Recognizer()
microphone = sr.Microphone()
sentiment_checked = False
listening = True

def toggle_jarwis_mode(mode):
        global listening
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
        audio = recognizer.listen(source,150,10)
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
            activity_thread = threading.Thread(target=monitor_activities)
            activity_thread.daemon = True
            activity_thread.start()
            return True
        else:
            speak("Unable to understand.")
            return False

def faceverify(status):
            speak("Let me verify your face please.")
            if status:
                verified = verifyface()
                if verified == True: 
                    speak("Face verified sir")  
                    pyautogui.press('escape')
                    cv2.destroyAllWindows()
                    return True
            else:
                speak("Unable to understand.")
                return False

def check_status(query):
    global sentiment_checked
    if not sentiment_checked:
            sentiment, confidence = analyze_sentiment(query)
            print(f"Your Sentiment: {sentiment}, Your Confidence: {confidence:.2f}")
            if sentiment == 'NEGATIVE' and confidence > 0.7:
                speak("I sense some negativity in your voice. Is everything alright sir?")
            sentiment_checked = True
            return f"Your Sentiment: {sentiment}, Your Confidence: {confidence:.2f}"
    else:
        return None

def advance_tokenize(text):
    tokens = re.findall(r"\b\w+(?:'\w+)?\b|\d+", text.lower())
    return tokens
    
def remove_stopwords(tokens):
    
    return [token for token in tokens if token not in dynamic_stop_words]

def advanced_stemmer(word):

    for suffix, replacement in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)] + replacement
    return word

def compute_tf(words):
    words = [word for word in words if isinstance(word, str)]
    tf = Counter(words)
    doc_len = len(words)
    if doc_len == 0: 
        return {}
    return {word: freq / doc_len for word, freq in tf.items()}

def compute_idf(words):
    import math
    idf = {}
    total_docs = len(words)
    all_words = set(word for document in words for word in set(document))
    for word in all_words:
        doc_count = sum(1 for document in words if word in document)
        idf[word] = math.log((total_docs + 1) / (doc_count + 1)) + 1
        
    return idf

def compute_tfidf(words):
    idf = compute_idf(words)
    tfidf_vectors = []
    for document in words:
        tf = compute_tf(document)
        tfidf = {word: tf[word] * idf.get(word, 0) for word in tf}
        tfidf_vectors.append(tfidf)
    return tfidf_vectors

def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[word]* vec2.get(word,0) for word in vec1 if vec2.get(word, 0) != 0)
    norm_vec1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
    norm_vec2 = math.sqrt(sum(value ** 2 for value in vec2.values()))
    return dot_product / (norm_vec1 * norm_vec2) if norm_vec1 and norm_vec2 else 0.0

def generate_dataset_from_commands(commands):
    dataset = []
    for intent, variations in commands.items():
        for command in variations:
            dataset.append({'question': command, 'answer': intent})
    return dataset

def preprocess_text(text):
    tokens = advance_tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = [advanced_stemmer(token) for token in tokens]
    return tokens

corpus = []
answers = []
dataset = generate_dataset_from_commands(commands)
for entry in dataset:
        corpus.append(preprocess_text(entry['question']))  
        answers.append(entry['answer'])
tfidf_vectors_command = compute_tfidf(corpus)

def get_answer(query,dataset):
    from data_required.intenstmatching import intent_to_function
    global listening
    try:
        query1 = query
        processed_query = preprocess_text(query)
        query_tfidf = compute_tfidf([processed_query])[0] 
        similarities = [cosine_similarity(query_tfidf, doc_vector) for doc_vector in tfidf_vectors_command]
        if max(similarities) < 0.5:
            return "Sorry, I didn't understand that. Could you rephrase?"
        best_match_index = similarities.index(max(similarities))
        intent = dataset[best_match_index]['answer']

        if intent in intent_to_function and listening:
            func = intent_to_function[intent]
            if callable(func):
                result = func(query1) if 'lambda' in str(func) else func()
                return result
        elif not listening and intent == "jarwis_status_wakeup":
            toggle_jarwis_mode("wakeup")
        elif not listening:
            print("Sleeping mode. Discarding the commands.")
            return "Jarwis is currently in sleep mode."
        else:
            speak("Sorry, I am not trained for this function, sir.")
            return "Sorry, I am not trained for this function."

    except Exception as e:
        print("error occured")
        pass

def mind(text,response_check):
    response_done = response_check
    
    if response_done == False:
        answer = get_answer(text, dataset)  # Possible generator function
        if isinstance(answer, types.GeneratorType):  # Check if it's a generator
            answer = "".join(answer)  # Consume generator to a single string
        return answer
    else:
        return None

# def main2():
#         # remind_last_activity()  
#     while True:
#         facestatus = faceverify(status="True")
#         if facestatus:
#             greet_user()
#             while True:
#                 user_input = take_user_input()
#                 if user_input:
#                     result_query,response_check = handle_query(user_input)
#                     result_mind = mind(user_input,response_check)
#                     if result_mind == "exit":
#                         break
#                 else:
#                     continue
#                 return result_query,result_mind
#         else:
#             speak("Face not verified. Please try again.")
#         response_check = False
#         return None, "Face not verified"

def main2():
    interactions = []
    retry_limit = 3
    retry_count = 0

    while retry_count < retry_limit:
        facestatus = faceverify(status="True")
        if facestatus:
            greet_user()
            say_last_activity()
            activity_thread = threading.Thread(target=monitor_activities)
            activity_thread.daemon = True
            activity_thread.start()
            while True:
                user_input = take_user_input()  # Assuming this method gets new input
                if user_input:
                    userstatus = check_status(user_input)
                    if userstatus :
                        interactions.append(("Jarvis", userstatus))
                        yield "Jarvis", userstatus  
                    interactions.append(("User", user_input))
                    # Yield after the user input to display it in the UI
                    yield "User", user_input
                    
                    # Process the user's input (query and mind)
                    result_query, response_check = handle_query(user_input)
                    result_mind = mind(user_input, response_check)

                    if result_query:
                        interactions.append(("Jarvis", result_query))
                        yield "Jarvis", result_query  # Yield Jarvis's response
                    elif result_mind:
                        interactions.append(("Jarvis", result_mind))
                        yield "Jarvis", result_mind  # Yield Jarvis's response

                    # Check if the user wants to exit
                    if result_mind == "exit":
                        interactions.append(("Jarvis", "Goodbye!"))
                        yield "Jarvis", "Goodbye!"  # Yield exit message
                        break
                else:
                    continue

        else:
            retry_count += 1
            speak("Face not verified. Please try again.")
            interactions.append(("Jarvis", "Face verification failed. Please try again."))
            yield "Jarvis", "Face verification failed. Please try again."
    return "exit"

def main3():
    interactions = []
    greet_user()
    say_last_activity()
    activity_thread = threading.Thread(target=monitor_activities)
    activity_thread.daemon = True
    activity_thread.start()
    while True:
        user_input = take_user_input()  # Assuming this method gets new input
        if user_input:
            userstatus = check_status(user_input)
            if userstatus :
                interactions.append(("Jarvis", userstatus))
                yield "Jarvis", userstatus  
            interactions.append(("User", user_input))
            # Yield after the user input to display it in the UI
            yield "User", user_input
            
            # Process the user's input (query and mind)
            result_query, response_check = handle_query(user_input)
            result_mind = mind(user_input, response_check)

            if result_query:
                interactions.append(("Jarvis", result_query))
                yield "Jarvis", result_query  # Yield Jarvis's response
            elif result_mind:
                interactions.append(("Jarvis", result_mind))
                yield "Jarvis", result_mind  # Yield Jarvis's response

            # Check if the user wants to exit
            if result_mind == "exit":
                interactions.append(("Jarvis", "Goodbye!"))
                yield "Jarvis", "Goodbye!"  # Yield exit message
                break
        else:
            continue
    return "exit"


# def main():
#     while True:
#         user_input = take_user_input()
#         if user_input:
#             # Send the user's input as an interaction
#             yield "User", user_input
            
#             # Process the input
#             result_query, response_check = handle_query(user_input)
#             result_mind = mind(user_input, response_check)
            
#             # Send Jarvis's response (query or mind)
#             if result_query:
#                 yield "Jarvis", result_query
#             elif result_mind:
#                 yield "Jarvis", result_mind
            
#             # Handle exit condition
#             if result_mind == "exit":
#                 yield "Jarvis", "Goodbye!"
#                 break
#         else:
#             continue

        # response_check = False
        # return interactions
        

# if __name__ == "__main__":
#     status = activate_assistant()
#     if status == True:
#         facestatus =faceverify(status)
#         if facestatus:
#             greet_user()
#             main()
#         else:
#             speak("Face not verified")
            