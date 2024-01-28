import speech_recognition as sr
import pyttsx3
import os
import openai as ai
from chat_search import generate_response
from voicegpt import transcribe_audio_to_text, speak_text

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        # print(query)
        return query
    

if __name__ == '__main__':
    print("listening.....")
    engine = pyttsx3.init('sapi5')           # <--- sapi 5 is for Windows
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # <--- voice id can be male(0) or female(1) 
    def speak():
        engine.say("audio")
        engine.runAndWait()

    speak()



