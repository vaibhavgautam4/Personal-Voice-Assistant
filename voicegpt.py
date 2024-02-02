
import speech_recognition as sr
import openai
import time
import os
from search import speak_text, transcribe_audio_to_text, generate_response


# setting openai api key (put your api key here)
openai.api_key = "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"

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