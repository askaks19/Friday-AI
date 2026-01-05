import pyttsx3
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()

def speak_old(text: str):
    engine.say(text)
    engine.runAndWait()

def speak(text: str):
    tts = gTTS(text)
    tts.save("response.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("response.mp3")
