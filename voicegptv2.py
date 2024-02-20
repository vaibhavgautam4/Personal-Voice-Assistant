import speech_recognition as sr
import pyttsx3
import os
import openai as ai
# from search import generate_response
from search import wish, wikipedia_search, speak_text, open_sites, play_song, introduce
from voicegpt import transcribe_audio_to_text

def takeCommand():
    r = sr.Recognizer()
    print("listening.....")
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language="en-in")
            # print(query)
            return query
        except:
            print('Can you please repeat sir!!!')
            speak_text('Can you please repeat sir!!!')
    

if __name__ == '__main__':
    # print("listening.....")
    engine = pyttsx3.init('sapi5')           # <--- sapi 5 is for Windows
    wish()
    query = takeCommand()

    if 'Wikipedia' in query:
        speak_text('Searching Wikipedia....')
        wikipedia_search(query)

    elif 'open' in query:
        open_sites(query)

    elif 'play' in query:
        play_song(query)

    elif 'introduce youself' in query:
        introduce()
