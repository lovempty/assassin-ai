# Version 1.0
# Start creating Assassin's brain
import speak

def understand(you = ""):
  if you == "":
      assassin_brain = "I'm listening to you, say something my boy :)"
  elif "hello" in you:
      assassin_brain = "Hi Synth"
  elif "today" in you:
      assassin_brain = common.getCurrentDate() + " my friend"
  elif "time" in you:
      assassin_brain = "It's " + common.getCurrentTime() + " now"
  elif "bye" in you:
      assassin_brain = "See you :)"
      print("Assassin: " + assassin_brain)
      speak.speak(assassin_brain)
      return -1
  else:
      assassin_brain = "Sorry, I have no idea about that"
  return assassin_brain
