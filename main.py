from typing import Any
from urllib import response

from openai import OpenAI
import speech_recognition as sr
import webbrowser
import requests
import pyttsx3
import pygame
from gtts import gTTS
import musicLibrary
r = sr.Recognizer()
engine = pyttsx3.init()
newsApi = 'pub_783f13c55a8a49fc9259a51cbaf4c9b5'


def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_new(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

# Initialize pygame mixer
    pygame.mixer.init()

# Load MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the music
    pygame.mixer.music.play()

# Wait until the song finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def aiProcess(command):
    client = OpenAI(
    api_key = "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"
)
    completion = client.chat.completions.create(
    model="gpt-5-mini",
    messages = [
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
    {"role": "user", "content": command}
]
)
    return completion.choices[0].message


def processcommand(c):
    if "open youtube" in c:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in c:
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split("play")[1].strip()
        link = musicLibrary.music(song)
        webbrowser.open(link)
    elif "news" in c:
        speak("Opening News")
        
        params = {
            "apikey": newsApi,
            "language": "en"
        }
        r= requests.get(f"https://newsdata.io/api/1/latest? apikey=pub_783f13c55a8a49fc9259a51cbaf4c9b5 ", params=params)
        if r.status_code != 200:
            data = r.json()

            titles = []

            for article in data.get("results", []):

                titles.append(article.get("title"))

            print(titles)
            speak(titles)
    else:
        output = aiProcess(c)
        speak(compile)

if __name__ == "__main__":
    speak(" Hey sir! How may I help you? ")
    while True:
        r = sr.Recognizer()
        
        # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = r.listen(source, timeout =2, phrase_time_limit = 2)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Yes sir!")
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
