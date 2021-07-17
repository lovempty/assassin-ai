import pyttsx3
assassin_mouth = pyttsx3.init()
assassin_mouth.setProperty("rate", 178)

def speak(assassin_brain = ""):
    assassin_mouth.say(assassin_brain)
    assassin_mouth.runAndWait()