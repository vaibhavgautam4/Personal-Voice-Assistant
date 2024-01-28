# import speech_recognition as sr
# import os 
# import pyttsx3
import openai

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
