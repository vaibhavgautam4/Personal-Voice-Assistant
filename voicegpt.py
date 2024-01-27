import pyttsx3
import speech_recognition as sr
import openai
import time

# setting openai api key
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

def speak_text(text):
    engine.say(text)
    engine.runAndWait

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
                        source.pause_threshold = 1
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

            except Exception as e:
                print("An error occured: {}".format(e))

if __name__ == "__main__":
    main()