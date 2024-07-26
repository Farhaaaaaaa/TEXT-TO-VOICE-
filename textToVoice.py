import pyttsx3
engine = pyttsx3.init()
a=input("type what you want to convert to voice   :")
engine.say(a)
engine.runAndWait()