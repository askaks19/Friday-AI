import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(timeout=5, phrase_time_limit=None) -> str:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )
    return recognizer.recognize_google(audio)
