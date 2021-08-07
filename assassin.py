# Assassin Version 1.1
import speak
import understand
import listen
import common

assassin_brain = ""
speak = speak.speak
listen = listen.listen
understand = understand.understand

print(common.wishMe())
speak(common.wishMe())
try:
    while True:
        # answer = listen()
        answer = input("Question: ")
        # Understand
        assassin_brain = understand(answer)
        if(assassin_brain == -1): break
        if(assassin_brain == 0): continue
        print("Assassin: " + assassin_brain)
        # Speak
        speak(assassin_brain)
except: 
    print('Please check your micro Synth. It is not working properly.')
    speak('Please check your micro Synth. It is not working properly.')

