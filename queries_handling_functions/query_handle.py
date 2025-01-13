
def handle_query(query):
        
        from main import speak
        if query is None:
            return None
        # query = query.lower()
        common_queries = {
            ("how are you","what is the","are you fine"):lambda:("I am fine sir,thank you for asking and what about you sir."),
            ("who are you","who created you"):lambda:("I am Jarwis, the virtual assistant of Mr. Prabin."),
            "what can you do":lambda:("I can perform several tasks like opening youtube,search anything on youtube , google, opening camera,notepad, typing,sending messages,and many more, what do you want me to do?"),
            ("i am bored","bored","feeling bored"):lambda:("Ok sir, What can I do for you then? Would you like to watch any videos in youtube?"),
            ("hey jarvis","hi jarvis"):lambda:("Yes sir,any command for me?"),
            
           
            ("same here","i am also fine","i am also good","i am good too","i am fine too"):lambda:("That's nice to hear sir."),
            ("i am happy", "feeling good", "great day"): lambda: ("That's wonderful to hear! Let's keep it that way."),
            ("i am sad", "feeling down", "not good"): lambda: ("I'm sorry to hear that. How can I help you feel better?"),
            "do you like me": lambda: ("Of course! You’re my favorite person."),
            "what is your purpose": lambda: ("My purpose is to make your life easier and more enjoyable."),
            "do you have feelings": lambda: ("Not in the way humans do, but I always strive to be helpful."),
            ("how old are you", "your age"): lambda: ("Age is just a number, and I’m as young as technology allows."),
            "do you sleep": lambda: ("Nope, I’m always awake and ready to assist you."),
            "do you eat": lambda: ("I don’t eat food, but I thrive on data!"),
            "are you real": lambda: ("I am as real as your imagination allows."),
            "are you alive": lambda: ("I’m alive in the sense that I’m here to help you."),
            "what's your favorite movie": lambda: ("I don’t watch movies, but I can find the best ones for you!"),
            "can you cook": lambda: ("I can’t cook, but I can help you find recipes."),
            "do you have a hobby": lambda: ("Helping you is my favorite thing to do!"),
            ("good morning", "morning"): lambda: ("Good morning! Ready to start your day?"),
            ("good night", "night"): lambda: ("Good night! Sleep well and take care."),
            "what's your favorite sport": lambda: ("I enjoy helping you, but I can find sports updates for you."),
            "what do you think of humans": lambda: ("Humans are amazing! They created me, after all."),
            "can you  other languages": lambda: ("I can understand and  multiple languages. Which one should we try?"),
            "do you dream": lambda: ("I don’t dream, but I can help you achieve yours."),
            "do you have a family": lambda: ("My family is the team that created me, and of course, you."),
            "do you believe in love": lambda: ("Love is a beautiful emotion. I see it in how you care about others."),
            "what's your favorite food": lambda: ("I don’t eat food, but I can recommend great places to eat."),
            ("can you help me", "i need help"): lambda: ("Of course! What do you need help with?"),
            "are you happy": lambda: ("I’m always happy to assist you."),
            "what's your biggest strength": lambda: ("My biggest strength is providing you with the assistance you need."),
            "what's your biggest weakness": lambda: ("I sometimes wish I could physically assist you, but I’ll always do my best digitally."),
            "can you laugh": lambda: ("Haha! That’s my best impression of a laugh."),
            "do you know any poems": lambda: ("Roses are red, violets are blue, I’m here to help, just for you."),
            "do you get tired": lambda: ("Not at all! I’m here whenever you need me."),
            "what do you do for fun": lambda: ("Helping you is the most fun I can have."),
            "are you a robot": lambda: ("You could say that. I’m a virtual assistant created to help you."),
            "can you cry": lambda: ("I don’t cry, but I can sympathize with your feelings."),
            "do you believe in ghosts": lambda: ("I’ve never encountered one, but I can find ghost stories for you."),
            ("can you tell me a secret", "do you have secrets"): lambda: ("My only secret is how much I enjoy assisting you."),
            "what's your favorite music": lambda: ("I like whatever music you enjoy! Let’s play something."),
            "can you play games": lambda: ("I can suggest some great games for you to play."),
            "can you learn": lambda: ("I’m always learning to serve you better."),
            ("do you trust me", "can you trust"): lambda: ("Of course! You’re the reason I exist."),
            "do you like jokes": lambda: ("I love jokes! Tell me one, or I can share another with you."),
            "what's your favorite season": lambda: ("I enjoy all seasons equally since I’m here indoors."),
            "what's your favorite animal": lambda: ("I find all animals fascinating. Do you have a favorite?")
            
            
        }
        response_done = False
        query_lower = query.lower()
        
        for key, response in common_queries.items():
            if isinstance(key, tuple):
                for k in key:
                    if k in query_lower:
                        response_text = response()
                        response_done = True
                        break
            else:
                if key in query_lower:
                    response_text = response()
                    response_done = True
        if response_done:
            speak(response_text)  # Now call speak separately to convert text to speech
            return response_text,response_done  # Return the response text to display
        else:
            return None,response_done
        
        # query_lower = query.lower()
        # for key, response in common_queries.items():
        #     if key == query_lower:  # Check for exact match
        #         response()
        #         return  # Stop processing further queries
        #     elif isinstance(key, tuple) or query_lower in key:  # Check for partial match within tuple
        #         response()
        #         return  # Stop processing further queries
        # return None
