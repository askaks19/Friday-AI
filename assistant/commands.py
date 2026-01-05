import webbrowser
import time
import requests
import musicLibrary

from assistant.speech import speak
from assistant.ai import ai_process

NEWS_API_KEY = "your_news_api_key"

def process_command(command: str):
    c = command.lower()

    if c == "open youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif c == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif c == "open stackoverflow":
        speak("Opening Stack Overflow")
        webbrowser.open("https://www.stackoverflow.com")

    elif c == "open linkedin":
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif c == "what's your name":
        speak("My name is Friday")

    elif c == "how are you":
        speak("I'm doing great!")

    elif c.startswith("play "):
        song = c[5:].strip().lower()
        link = musicLibrary.music.get(song)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find that song")

    elif "news" in c:
        speak("Here are the latest headlines")
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        )
        if r.status_code == 200:
            for article in r.json().get("articles", [])[:5]:
                speak(article["title"])
                time.sleep(1)

    else:
        response = ai_process(c)
        speak(response)
        print("AI:", response)
