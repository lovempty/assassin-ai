# Assassin Version 1
import speak
import understand
import listen

assassin_brain = ""
speak = speak.speak
listen = listen.listen
understand = understand.understand

print('Hi. I am assassin - A smart AI created by Synth. Nice to meet you!')
speak('hi. i am assassin - a smart AI created by Synth. nice to meet you!')
try:
    while True:
        answer = listen()
        # answer = input("Question: ")
        # Understand
        assassin_brain = understand(answer)
        if(assassin_brain == -1): break
        print("Assassin: " + assassin_brain)
        # Speak
        speak(assassin_brain)
except: 
    print('Please check your micro Synth. It is not working properly.')
    speak('Please check your micro Synth. It is not working properly.')

