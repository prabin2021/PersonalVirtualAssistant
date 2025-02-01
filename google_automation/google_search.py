
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import re
def search_google(query):
    from main import speak
    query1 = query
    start_keywords = ["search for","search for the topic","search for the name","search for the title","search" ,"look for", "find that", "find out"," information about","idea about" "search about", "show me", "watch", "search that", "tell me","search",
                      "give me the idea about","give me idea about","google that","google search that","my query is","my question is","for","about","find"]
    query = re.sub(r"\b(on|in|from) google\b", "", query, flags=re.IGNORECASE).strip()
    words = query.lower().split()
    search_query = ""
    for i, word in enumerate(words):
        if word in start_keywords:
            search_query = " ".join(words[i + 1:])
    print(search_query)
    if search_query == "":
        search_query = query1
    if not search_query:
        speak("Please specify properly what you want to search for.")
        return
    kit.search(search_query)
    speak("Ok sir, here is your search result.")
    return "Ok sir, here is your search result."

def open_google():
    kit.search("www.google.com")
    return"Google opened sir"

