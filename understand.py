# Version 1.0
# Start creating Assassin's brain
import speak
import common
import subprocess


speak = speak.speak
def understand(question = ""):
  # Hello  
  if question == "":
      assassin_brain = "I'm listening to you, say something my boy"
  elif "what" in question and "can" in question and "you" in question and "do" in question:
      assassin_brain= """I can do something like: 
                        give you information about today date, time. 
                        I can open google, youtube or facebook for you. 
                        If you are bored, I can tell some jokes.
                        Answer "do you know" questions. 
                        Sometime answer your weird questions..."""
  elif "hello" in question:
      assassin_brain = "Hi Synth"
  elif "how" in question and "old" in question and "you" in question:
      assassin_brain = common.calAge()
  elif "thank you" in question:
      assassin_brain = "You're welcome"
  elif "who are you" in question:
      assassin_brain = "I am assassin - Synth's friend."
  elif "i love you" in question:
      assassin_brain = "aw. I love you too"
  #operating with compututer system
  elif "shutdown pc" in question or "shutdown computer" in question or "turn off pc"  in question:
      assassin_brain = "Your computer is on its way to shutdown in few seconds"
      subprocess.call('shutdown / p /f')
  elif "restart" in question and "pc" in question:
      assassin_brain = "Your computer is on its way to restart in few seconds"
      subprocess.call(["shutdown", "/r"])
  # common information
  elif ("who" in question and "create" in question) or ("who"  in question and "made" in question) or ("who" in question and "make" in question):
      assassin_brain = "It's Synth"
  elif "when " in question and "create" in question:
      assassin_brain = "15/07/2021"
  elif "today" in question:
      assassin_brain = common.getCurrentDate() + " my friend"
  elif "time" in question:
      assassin_brain = "It's " + common.getCurrentTime() + " now"
  # Wikipedia
  elif "do you know" in question:
      keyword = question.split("do you know")[1];
      assassin_brain = common.wiki(keyword)
  # Open browser youtube, facebook
  elif "google" in question:
      assassin_brain = "copy that"
      common.open("https://google.com")
  elif "youtube" in question:
      assassin_brain = "yes sir"
      common.open("https://youtube.com")
  elif "facebook" in question:
      assassin_brain = "easy"
      common.open("https://facebook.com")
  # tell some jokes
  elif "joke" in question: 
      assassin_brain = common.getAJoke()
  # get an advice
  elif question.startswith("should i") or question.startswith("do you think"):
      assassin_brain = common.yesOrNo()
  elif "bye" in question or "see you" in question:
      assassin_brain = "See you!"
      print("Assassin: " + assassin_brain)
      speak(assassin_brain)
      return -1
  elif question == "no_sound":
      assassin_brain = "Sorry, I cannot hear you"
      print("Assassin: " + assassin_brain)
      speak(assassin_brain)
      return -1
  else:
      assassin_brain = common.getWolfAnswer(question)


  return assassin_brain
