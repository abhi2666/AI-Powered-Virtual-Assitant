import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
