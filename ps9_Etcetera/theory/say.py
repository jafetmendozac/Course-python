import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Often female voice
engine.setProperty('rate', 150)
engine.say(this)
engine.runAndWait()