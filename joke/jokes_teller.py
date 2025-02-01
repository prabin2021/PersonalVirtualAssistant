import pyjokes

def tell_random_joke():
    from main import speak
    joke = pyjokes.get_joke()
    speak(f"{joke} You can read it also sir.")
    return joke
