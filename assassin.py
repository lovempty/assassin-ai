# Assassin Version 1
import pyttsx3
import speech_recognition
import common
import speak
import understand
import listen
# Listen
assassin_ear = speech_recognition.Recognizer()
# assassin_mouth = pyttsx3.init()
# assassin_mouth.setProperty("rate", 178)
assassin_brain = ""
speak = speak.speak()
understand = understand.understand()

print('Hi. I am assassin - A smart AI created by Synth. Nice to meet you!')
speak('hi. i am assassin - a smart AI created by Synth. nice to meet you!')
try:
    while True:
        with speech_recognition.Microphone() as mic:
            print("Assassin: I'm listening to you, say something my boy")
            print("Listening...")
            audio = assassin_ear.record(mic, duration=3)

        try:
            you = assassin_ear.recognize_google(audio)
        except:
            you = "Sorry. I cannot hear you :("
            print("Assassin: " + you)
            speak('Sorry. I cannot hear you.')
            break
        # Understand
        assassin_brain = understand(you)
        if(assassin_brain == -1): break
        print("Assassin: " + assassin_brain)
        # Speak
        speak(assassin_brain)
except: 
    print('Please check your micro Synth. It is may not working.')
    speak('Please check your micro Synth. It is may not working.')

