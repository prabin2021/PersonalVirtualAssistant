import wikipedia
import re

def extract_search_Query(query):
        start_keywords = ["search","for","look for","find","find that","about","search about","tell me","that","answer of","question","questions"]
        future_query = query
        words = query.split()
        search_query = ""
        for i, word in enumerate(words):
            if word in start_keywords:
                search_query1 = " ".join(words[i + 1:])
        search_query = re.sub(r"\s?(in|at|on|with|from)\s?wikipedia", "", search_query1)
        if search_query == "":
            search_query = future_query
        get_wikipedia_summary(search_query)
def get_wikipedia_summary(query):
    from main import speak
    try:
        results = wikipedia.summary(query,sentences=3)
        speak("According to wikipedia")
        speak(results)
        return f"According to wikipedia:{results}"
    except Exception as e:
        speak("Unable to find from wikipedia sir, can you modify your question pattern again?")
        return "Unable to find from wikipedia sir, can you modify your question pattern again?"



            


