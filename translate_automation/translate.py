 
from gtts import gTTS
import os
def speak1(target_languag, translated_text):
    combined_text = f"Your translated text is {translated_text}"
    tts = gTTS(combined_text, lang=target_languag) # Use 'ne' for Nepali
    tts.save("temp.mp3")
    os.system("start temp.mp3")
def translate_text(query):
    from main import speak,take_user_input
    from mtranslate import translate 
    start_keywords = [
                    "translate the word", "translate the words", "translate words", "convert the words",
                    "change the words", "translate the texts", "translate this text", "translate text",
                    "translate this sentence", "translate these sentences", "translate this line", "translate these words",
                    "convert these words", "convert this word", "change this line", "change these lines",
                    "change words", "translate that", "translate it", "translate texts", "convert this line",
                    "translate these lines", "translate", "translate the sentence", "convert sentence",
                    "convert sentences", "translate into another form", "translate this word",
                    "change to another form", "translate this content", "convert the paragraph",
                    "convert paragraphs", "translate paragraphs", "translate a word", "translate this phrase",
                    "translate phrases", "change the text", "convert the text", "convert the content",
                    "translate this", "translate that", "convert it", "convert the message",
                    "turn this into a different style", "translate the phrase", "transform this content",
                    "convert this into something else", "change the structure", "translate the passage",
                    "convert this to a new form", "change this expression", "turn this into new words",
                    "translate and rewrite", "convert and rewrite", "translate into a different format",
                    "convert this input", "transform the paragraph",
                    "change the phrase", "reword this text", "adjust these sentences",
                    "interpret this text", "rewrite in another way", "make this into new sentences",
                    "change the paragraph", "translate the input", "rephrase this content",
                    "convert words to another language", "translate my input", "convert to another language",
                    "interpret this", "transform this line", "translate these lines",
                    "rephrase the input", "transform and rewrite", "make this into something else",
                    "adjust the wording", "turn this sentence into another form"
]

    languages = {
        "english": "en", "mandarin": "zh", "spanish": "es", "hindi": "hi", "arabic": "ar",
        "portuguese": "pt", "bengali": "bn", "russian": "ru", "japanese": "ja", "punjabi": "pa",
        "german": "de", "javanese": "jw", "korean": "ko", "french": "fr", "telugu": "te",
        "marathi": "mr", "turkish": "tr", "tamil": "ta", "vietnamese": "vi", "urdu": "ur",
        "italian": "it", "gujarati": "gu", "polish": "pl", "ukrainian": "uk", "persian": "fa",
        "malay": "ms", "dutch": "nl", "greek": "el", "czech": "cs", "swedish": "sv",
        "hungarian": "hu", "hebrew": "he", "danish": "da", "finnish": "fi", "norwegian": "no",
        "slovak": "sk", "bulgarian": "bg", "serbian": "sr", "croatian": "hr", "lithuanian": "lt",
        "latvian": "lv", "estonian": "et", "icelandic": "is", "maltese": "mt", "albanian": "sq",
        "bosnian": "bs", "macedonian": "mk", "montenegrin": "me", "luxembourgish": "lb", "afrikaans": "af",
        "swahili": "sw", "amharic": "am", "zulu": "zu", "xhosa": "xh", "somali": "so",
        "hausa": "ha", "igbo": "ig", "yoruba": "yo", "kiswahili": "sw", "pashto": "ps",
        "sindhi": "sd", "nepali": "ne", "sinhalese": "si", "burmese": "my", "khmer": "km",
        "lao": "lo", "thai": "th", "malayalam": "ml", "kannada": "kn", "oriya": "or",
        "assamese": "as", "maithili": "mai", "bhili": "bhb", "santali": "sat", "kurdish": "ku",
        "azerbaijani": "az", "georgian": "ka", "armenian": "hy", "kazakh": "kk", "uzbek": "uz",
        "turkmen": "tk", "tajik": "tg", "mongolian": "mn", "tibetan": "bo", "uyghur": "ug",
        "dzongkha": "dz", "sanskrit": "sa", "pali": "pi", "avestan": "ae", "bashkir": "ba",
        "chuvash": "cv", "komi": "kv", "mari": "chm", "udmurt": "udm", "tatar": "tt",
        "chechen": "ce", "inuktitut": "iu", "greenlandic": "kl", "sami": "se", "faroese": "fo",
        "breton": "br", "welsh": "cy", "irish": "ga", "scots gaelic": "gd", "nepali":"ne"
    } 
    query_lower = query.lower().strip()
    words = query_lower.split()
    i = 0
    while i < len(words):
        potential_keyword = " ".join(words[i:])
        matched = False
        for keyword in start_keywords:
            if potential_keyword.startswith(keyword):
                # Remove the matched keyword and any preceding words
                words = words[i + len(keyword.split()):]
                query_lower = " ".join(words)
                matched = True
                break
        if matched:
            i = 0  # Reset index to start checking again from the beginning
        else:
            i += 1  # Move to the next word if no match found
    # Reconstruct the query after removing leading phrases and keywords
    try:
        search_query = " ".join(words).strip()
        speak("can you say the language that you want to translate in?")
        target_language = take_user_input().lower().split()
        target_languag = ""
        for i, wordss in enumerate(target_language):
            if wordss in languages:
                target_languag = languages[wordss]
        if not target_languag:
            speak("Sorry sir, I am not trained to translate in the language that you want to translate in.")
            return "Sorry sir, I am not trained to translate in the language that you want to translate in."
        speak("Selected Language is ", target_languag)
        translated_text = translate(search_query,target_languag)
        print("Texts to translate: ",search_query)
        speak1(target_languag, translated_text)
        return(f"Translated text is  {translated_text}")
    except Exception as e:
        speak("Sorry I could not perform this action now.")
        return "Sorry I could not perform this action now."
    

