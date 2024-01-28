import pyttsx3
import speech_recognition as sr
import openai
import time
import os
from chat_search import generate_response


# setting openai api key (put your api key here)
openai.api_key = "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"


# initialise text to speech engine
engine = pyttsx3.init()

# audio to text transcription

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("skipping unknown error!!")

def speak_text(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # <--- voice id can be male(0) or female(1) 
    engine.say(text)
    engine.runAndWait()

def main():
    while(1):
        # wait for user to say jarvis
        print('say "jarvis" to start recording!')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "jarvis":
                    # record audio
                    filename = "input.wav"
                    print("ask questions to jarvis...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        recognizer.pause_threshold = 0.7
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                # transcribe audio to text
                text = transcribe_audio_to_text(filename)
                # print(text)
                if text:
                    print(f"You said {text}")

                    # generate responses
                    response = generate_response(text)
                    print(f"gpt says: {response}")

                    # read responses out
                    speak_text(response)
                    # speak_text(text)

            except Exception as e:
                print("An error occured: {}".format(e))

if __name__ == "__main__":
    main()