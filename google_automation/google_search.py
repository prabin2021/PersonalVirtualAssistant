
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup

def search_google(query):
    from main import speak
    start_keywords = ["search for","search for the topic","search for the name","search for the title","search" ,"look for", "find that", "find out"," information about","idea about" "search about", "show me", "watch", "search that", "tell me","search",
                      "give me the idea about","give me idea about","google that","google search that","my query is","my question is","for","about","find"]
    words = query.lower().split()
    search_query = ""
    for i, word in enumerate(words):
        if word in start_keywords:
            search_query = " ".join(words[i + 1:])
    print(search_query)

    if not search_query:
        speak("Please specify properly what you want to search for.")
        return

    kit.search(search_query)
    speak("Ok sir, here is your search result.")

    google_url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(google_url)
    if response.status_code != 200:
        speak("I am unable to fetch the search results right now sir.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    speak("I have collected 2 results sir.")
    snippets = soup.select('div.BNeawe.s3v9rd.AP7Wnd')[:2]
    if not snippets:
        speak("No results found.")
        return

    result_texts = [snippet.get_text() for snippet in snippets]

    for i, result in enumerate(result_texts):
        print(result)
        speak(f"Result {i+1}: {result}")
        return result
def open_google():
    kit.search("www.google.com")
    return"Google opened sir"

