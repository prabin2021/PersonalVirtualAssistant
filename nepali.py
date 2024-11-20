
# import os
# import pygame
# import pygame
# import speech_recognition as sr
# from gtts import gTTS
# import os
# def speak_nepali(text):
#     tts = gTTS(text=text, lang='ne', slow=False)
#     filename = "voice.mp3"
#     tts.save(filename)

#     pygame.mixer.init()
#     pygame.mixer.music.load(filename)
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         continue

#     os.remove(filename)
# def recognize_speech_in_nepali(timeout=3, ):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("कृपया बोल्नुहोस्...")
#         recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust based on the environment
#         recognizer.energy_threshold = 4000
#         audio = recognizer.listen(source, timeout=timeout)

#     try:
#         print("पर्खनुहोस्...")
#         # Using Google Web Speech API for recognition
#         result = recognizer.recognize_google(audio, language='ne-NP')
#         print(f"तपाईंले भन्नुभयो: {result}")
#         return result
#     except sr.UnknownValueError:
#         print("माफ गर्नुहोस्, मैले बुझ्न सकिन।")
#         speak_nepali("माफ गर्नुहोस्, मैले बुझ्न सकिन।")
#     except sr.RequestError as e:
#         print(f"सेवामा समस्या देखियो; {e}")
#         speak_nepali("सेवामा समस्या देखियो।")

# if __name__ == "__main__":
#     while True:
#         command = recognize_speech_in_nepali()
#         if command:
#             if "बन्द" in command or "बन्द गर्नुहोस्" in command:
#                 speak_nepali("ठिक छ, प्रणाली बन्द गर्दै छु।")
#                 break
#             else:
#                 speak_nepali(f"तपाईंले भन्नुभएको कुरा: {command}")
   