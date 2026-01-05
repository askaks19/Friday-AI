import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def aiProcess(command):
    genai.configure(api_key="[your api key]")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a virtual assistant named Jarvis, skilled in general tasks like Alexa or Siri., give short responses",)

    response = model.generate_content(command)
    return response.text

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("response.mp3")

def processCommand(c):
    c = c.lower()
    if c == "open youtube":
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    
    elif c == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif c == "open stackoverflow":
        speak("Opening Stackoverflow")
        webbrowser.open("https://www.stackoverflow.com")

    elif c == "what's your name":
        speak("My name is Friday")

    elif c == "how are you":
        speak("I am fine, thank you")


    elif c == "open linkedin":
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif c.startswith("play "):
     song = c[5:].strip().lower()
     if song:
        speak(f"Playing {song}")
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find the song.")

    elif "news" in c.lower():
        speak("Here are some latest news headlines.")
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={eef46cf3b2df44028fd2e69757de54a3}")
        if r.status_code==200:
            data=r.json()
            articles = data.get('articles', [])
            for ar in articles[:5]:
                speak(ar["title"])
                time.sleep(1)
    else:
        #Let Google Gemini handle the request
        output=aiProcess(c)
        speak(output)
        print("AI: "+output)
        


if __name__ == "__main__":
    speak("Initializing Friday....")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'Friday'...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("You said: " + word)
            if word.lower() in ["friday", "freddy", "fridayy"]:
            # proceed
                speak("Hey!")
                time.sleep(1)
                print("Friday is now active...")
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2)
                    audio2 = r.listen(source2)
                    command2 = r.recognize_google(audio2)
                    print("Command recognized: " + command2)
                    processCommand(command2)
        except Exception as e:
            print("Error: {0}".format(e))

