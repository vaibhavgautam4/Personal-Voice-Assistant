import datetime
import openai
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# initialise text to speech engine
engine = pyttsx3.init()


def speak_text(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # <--- voice id can be male(0) or female(1) 
    engine.say(text)
    engine.runAndWait()

# audio to text transcription

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("skipping unknown error!!")


def generate_response(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt= prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].text

    # print(message)
    return message


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        print('        good morning sir!')
        speak_text('good morning sir!')

    elif hour>12 and hour<18:
        print('         good afternoon sir!')
        speak_text('good afternoon sir!')

    elif hour>18 and hour<20:
        print('      good evening sir!')
        speak_text('good evening sir!')

    print("I'm Jarvis. How can I help you today!")
    speak_text("I'm Jarvis. How can I help you today!")


def wikipedia_search(query):
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=4)
    speak_text('Wikipedia says..')
    print(results)
    speak_text(results)


def open_sites(site):
    sites = { 'YouTube':'www.youtube.com', 'google':'www.google.com', 'Linkedin':'www.linkedin.com' }
    word = site.split()
    site = word[1]
    for s in sites:
        if s == site:
            print(f"opening {sites[s]}")
            speak_text(f"opening {s}")
            webbrowser.open(sites[s])


def play_song(song):
    music_dir = ''
    songs = os.path.join(music_dir,'*.mp3')
    song = music_dir + '\\' + song
    for s in songs:
        if s == song:
            print('Playing {s}')
            speak_text('playing {s}')
            os.open(s)

def introduce():
    print('Sure sir!')
    print("I'm JARVIS! Just Another Really Very intelligent System! ")
    speak_text('         Sure sir!')
    speak_text("I'm JARVIS! Just Another Really Very intelligent System! ")

introduce()