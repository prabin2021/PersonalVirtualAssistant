
dynamic_stop_words = {
    "the", "is", "in", "and", "to", "of", "a", "it", "that", "on", "for", "with",
    "as", "by", "an", "or", "be", "are", "from", "was", "at", "but", "not", "have",
    "has", "had", "which", "were", "you", "your", "their", "can", "we", "they", "i",
    "he", "she", "him", "her", "my", "me", "this", "there", "them", "how", "when", 
    "where", "why", "which", "all", "some", "any", "both", "each", "few", "more", 
    "most", "less", "own", "such", "one", "two", "three", "four", "five", "also", 
    "another", "these", "those", "that", "here", "there", "who", "whom", "whose", 
    "while", "during", "before", "after", "until", "then", "next", "now", "just", 
    "only", "but", "than", "too", "very", "more", "much", "no", "nor", "not", "own", 
    "same", "so", "like", "as", "will", "just", "don", "should", "could", "would", 
    "can", "ought", "i'm", "you're", "he's", "she's", "we're", "they're", "wasn't", 
    "weren't", "isn't", "aren't", "hasn't", "haven't", "don't", "doesn't", "didn't", 
    "hadn't", "won't", "wouldn't", "shouldn't", "can't", "couldn't", "might", "mightn't", 
    "must", "mustn't", "shall", "shan't", "shouldn't", "is", "it’s", "he’s", "she’s", 
    "it’s", "they’ve", "here's", "there’s", "where’s", "what’s", "who’s", "why’s", 
    "i’ve", "you’ve", "we’ve", "he'll", "she'll", "we'll", "they'll", "it's", "all", "each", 
    "every", "another", "few", "many", "several", "whole", "much", "more", "less", "few", 
    "long", "short", "above", "below", "under", "over", "through", "around", "before", "after"
}

suffixes = [
    ("ational", "ate"), ("tional", "tion"), ("enci", "ence"), ("anci", "ance"), 
    ("izer", "ize"), ("abli", "able"), ("alli", "al"), ("entli", "ent"), ("eli", "e"),
    ("ousli", "ous"), ("ization", "ize"), ("ation", "ate"), ("ator", "ate"), 
    ("alism", "al"), ("iveness", "ive"), ("fulness", "ful"), ("ousness", "ous"),
    ("aliti", "al"), ("iviti", "ive"), ("biliti", "ble"), ("logi", "log"),
    ("fullness", "ful"), ("lessness", "less"), ("ically", "ic"), ("ality", "al"),
    ("ivity", "ive"), ("ization", "ize"), ("isation", "ise"), ("fulness", "ful"),
    ("ousness", "ous"), ("ationally", "ate"), ("tionally", "tion"), ("iveness", "ive"),
    ("ization", "ize"), ("isation", "ise"), ("ic", "ic"), ("able", "able"), ("ible", "ible"),
    ("entment", "ent"), ("ational", "ate"), ("iveness", "ive"), ("ousity", "ous"),
    ("ibility", "ible"), ("cation", "cate"), ("logical", "log"), ("istion", "ist"),
    ("lessly", "less"), ("ational", "ate"), ("ity", "y"), ("ment", ""), 
    ("ization", "ize"), ("isation", "ise"), ("lessly", "less"), ("istical", "ist"),
    ("ianism", "ian"), ("arism", "ar"), ("itarian", "ity"), ("itional", "ition"),
    ("ography", "ograph"), ("ation", "ate"), ("orary", "ory"), ("iency", "ient"),
    ("estant", "est"), ("esting", "est"), ("ental", "ent"), ("anism", "an"),
    ("ivity", "ive"), ("ement", "e"), ("ency", "ent"), ("ity", "y"), ("ially", "ial"),
    ("ation", "ate"), ("lessly", "less"), ("ically", "ic"), ("etive", "et"),
    ("ionize", "ion"), ("arian", "ar"), ("ialist", "ial"), ("istic", "ist"),
    ("ology", "olog"), ("alize", "al"), ("atory", "ate"), ("esque", "esq"),
    ("ative", "ate"), ("ocity", "ous"), ("arity", "ar"), ("acity", "ac"),
    ("ative", "ate"), ("ously", "ous"), ("ifier", "ify"), ("ously", "ous"),
    ("ismic", "ism"), ("istic", "ist"), ("tive", "t"),
    ("astic", "ast"), ("arity", "ar"), ("ifier", "ify"), ("idity", "id"),
    ("itude", "it"), ("esque", "esq"), ("ation", "ate"), ("ingly", "ing"),
    ("antry", "ant"), ("lity", "l"), ("ismic", "ism"), ("alism", "al"),
    ("itary", "it"), ("ism", ""), ("ment", ""), ("tion", "t"),
    ("ance", "a"), ("ent", ""), ("able", "e"), ("ness", ""),
    ("ious", "y"), ("ful", ""), ("ence", "e"), ("ate", ""),
    ("ment", ""), ("ity", ""), ("ive", ""),
]



commands = {

    "uncomplete": [
        "help me","open", "check", "read","show", "launch", "need","display", "can", "bring","please", "load",
        "let", "start","send","want","access","text","take","write","search","find","last","turn","click"
    ],
    "open_whatsapp": [
        "open WhatsApp", "launch WhatsApp", "start WhatsApp", "access WhatsApp", "can i have whatsapp","i need whatsapp","show whatsapp","initiate WhatsApp", "WhatsApp app please", "where is WhatsApp", "WhatsApp window","can i get WhatsApp"
    ],
    "open_discord": [
        "open discord", "launch discord", "start discord", "access discord", "can i have discord","i need discord","show discord","initiate discord", "discord app please", "where is discord", "discord window","can i get discord"
    ],
    "send_whatsapp_message": [
        "help me to message in whatsapp","send a message on WhatsApp", "WhatsApp this message", "shoot a message on WhatsApp","message someone on WhatsApp", "text on WhatsApp","i want to message through whatsapp"
        "send WhatsApp message", "WhatsApp message","want to text someone through whatsapp","send a message in WhatsApp","send a message using WhatsApp"
    ],
    "open_command_prompt": [
        "can you start cmd", "can i have cmd prompt please", "can you run command prompt", "show me the cmd", "open terminal","can you open command prompt", "can you launch command prompt", "can you start command prompt", "i want to access command prompt","can i have command prompt","i need command prompt","show my command prompt", "ope command prompt"
    ],
    "open_camera": [
        "start the camera", "turn the camera on", "enable camera", "webcam please", "access my camera","open my camera", "turn on the camera", "launch camera", "start my camera",
        "open the webcam", "show my camera", "turn on webcam", "start webcam",
        "I need my camera", "camera on", "open the camera","open camera", "launch camera", "start camera", "access camera","can i have camera","i need camera","show my camera"
    ],
    "capture_photo": [
        "snap a picture", "take my photo", "snap a shot", "take a picture", "click the image","click my pictures", "capture photo", "click photos", "capture pictures", "click our picture","click our photos","take the shots"
    ],
    "open_notepad": [
        "bring up notepad", "access text editor", "where's notepad", "type in notepad", "launch text editor","open notepad", "launch notepad", "start notepad", "access notepad","can i have notepad","i need notepad","show my notepad"
    ],
    "jarwis_status_sleep": [
        "take a rest", "pause yourself", "relax for now", "sleep mode", "stay quiet","bro sleep now", "sleep for a while", "don't disturb me for a while", "go away", "keep silent","don't make noise","activate sleep mode","can you sleep","leave me alone for a while"
    ],
    "jarwis_status_wakeup": [
        "resume work", "ready up", "start your system", "active mode","bro wake up now", "wakeup now", "i need you", "stand up please", "bro start up ","can you wake up","raise up bro","let's work together","wake up"
    ],
    "open_facebook": [
        "facebook app", "social media access", "launch my Facebook", "Facebook login", "start my Facebook","open Facebook", "launch Facebook", "start Facebook", "access Facebook", "use social media","can i have facebook","i need facebook","show my facebook"
    ],
    "send_email": [
        "write an email", "draft a mail", "email someone", "send a message via email", "send an email", "send a mail", "e-mail someone", "dispatch an email", "send email to", "help me to send email", "i want to send email to my friend", "can i send email to someone", 
        "i need to email someone", "can you help me send an email", "how can i send an email to my colleague", "i wish to send an email", "send email to my family", "i want to send a message via email", "help me email a contact", "can i email my friend", "i want to write an email to someone", 
        "can you send an email for me", "help me dispatch an email", "is it possible to email someone", "can you compose an email for me", "i want to send a mail to my friend""help me to send email","compose email", "write an email", "draft a mail", "email someone", "send a message via email","send an email", "send a mail", "e-mail someone", "dispatch an email", "send email to","help me to send email"
    ],
    "tell_joke": [
        "make me giggle","i want to laugh" ,"say something funny", "give me a laugh", "share a funny line", "jokes please","tell me a joke","i want you to tell me joke","i want you to tell me another joke","tell me another joke", "tell me some jokes", "say joke", "i want jokes", "provide me some jokes","make me laugh", "can you make me laugh"
    ],
    "translate_text": [
        "help me to translate text","interpret this text", "convert text to another language", "translate this content", "switch the language", "language conversion","translate the text", "convert the text","change the text","change this sentence into another language", "translate the words into another language", "can you convert ", "can you translate this", "convert these sentences","convert this sentences into another language", "translate these sentences"
        "translate the word", "translate the words", "translate words", "convert the words","translate a text","convert words to another language", "translate my input", "convert to another language", "interpret this", "transform this line", "translate these lines",
    ],
    "open_google": [
        "help me to open google","launch search engine", "access Google search", "where's Google", "Google please","open Google", "launch Google", "start Google", "access Google", " want to use Google","show me google","can i have google  ", "i need google"
    ],
    "search_wikipedia": [
        "search in wikipedia", "search for something in wikipedia","find info on Wikipedia", "Wikipedia search for something", "Wikipedia lookup", "fetch from Wikipedia", "Wikipedia article about", "wikipedia search about", "access information about something through wikipedia", "use wikipedia to search for anything"
        "scrap information about something through wikipedia",
    ],
    "search_google": [
        "look up on Google", "Google lookup", "find via Google", "Google query", "search engine search","search in Google", "search for something in Google", "google search", "access information about something through Google", "use Google to search for anything","using google search for","scrap information using google","find information about something through Google","can you search about something in google","help me to search in google",
    ],
    "open_youtub": [
        "help me to open YouTube","YouTube access", "YouTube app", "start the YouTube", "show me YouTube","open YouTube", "launch YouTube", "start YouTube", "i want YouTube", "show YouTube ","can i have youtube ", "i need youtube", "bring youtube"
    ],
    "search_youtube": [
        "help me to search about in YouTube","look for videos on YouTube", "video search on YouTube", "explore on YouTube", "find songs on YouTube","search in YouTube", "find on YouTube", "search on YouTube", "watch videos on YouTube", "listen music in  YouTube ","want to search in youtube ", "find out in youtube"
    ],
    "open_calculator": [
        "calculator app", "math tool access", "open my calculator", "launch the calculator", "start calculations","open calculator", "launch calculator", "start calculator", "access calculator", "open the calculator"
    ],
    "check_battery": [
        "help me to check my battery life","show battery info", "current charge level", "battery details", "remaining battery", "battery capacity","check battery status", "battery percentage", "how much battery is left", "battery level", "what's my battery","what is my battery life"
    ],
    "open_settings": [
        "help me to open settings","settings menu", "system settings", "device settings", "access preferences", "configure settings","open settings", "launch settings", "start settings", "go to settings", "open system settings"
    ],
    "previous_activities": [
        "activity log", "what have I done earlier", "my tasks history", "what were we working on", "previous sessions","show my previous activities","what were my previous works", "what we were doing last time","what we were doing yesterday", " in which project we were working last time", "want to see my previous tasks", "trace my previous works"
    ],
    "exit": [
        "close the system", "stop now", "terminate the app","terminate yourself", "wrap up","exit now","you can exit now", "you can terminate now", " shut the system", "shut down your system", "terminate now", "leave now", "will you leave now"
    ],
    
    "minimize_window": [
        "can you minimise this window","reduce window", "hide this window", "make the screen smaller", "move the window down", "lower the window","minimize the window", "can you minimize this screen", "minimize my current window", "please minimize the screen", "make the window smaller","can you minimise this screen"
    ],
    "maximize_window": [
        "make the screen bigger", "can you maximise this window","bring the window up", "expand this window", "maximize the display","maximize the window", "can you maximize this window", "maximize now", "please maximize the screen", "make the window full screen", "expand the window"
    ],
    "close_window": [
        "shut this window", "terminate this screen", "dismiss the window", "close this tab","close the window", "can you close this window", "close current window", "please close the screen", "remove this window", " close this window"
    ],
    "tell_time": [
        "what hour is it", "how late is it", "check the clock", "give me the time", "show current hour","tell me the time", "what time is it now", "can you tell me the time", "what's the current time", "show the time", "say me the time", "what is time now", "current time please", "can you show me the time","i want to know the time"
    ],

}


