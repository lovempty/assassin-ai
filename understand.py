# Version 1.0
# Start creating Assassin's brain
import speak
import common

speak = speak.speak
def understand(question = ""):
  # Hello  
  if question == "":
      assassin_brain = "I'm listening to you, say something my boy :)"
  elif "hello" in question:
      assassin_brain = "Hi Synth"
  elif "thank you" in question:
      assassin_brain = "You're welcome"
  elif "who are you" in question:
      assassin_brain = "I am assassin - Synth's friend."
  elif "i love you" in question:
      assassin_brain = "aw. I love you too"
  # common information
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
      speak("copy that")
      common.open("https://google.com")
  elif "youtube" in question:
      speak("Yes sir")
      common.open("https://youtube.com")
  elif "facebook" in question:
      speak("Easy")
      common.open("https://facebook.com")
  # tell some jokes
  elif "joke" in question: 
      assassin_brain = common.getAJoke()
  # get an advice
  elif "should i" in question or "do you think " in question:
      assassin_brain = common.yesOrNo()
  elif "bye" in question:
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
      try:
        assassin_brain = common.getWolfAnswer(question)
      except:
        assassin_brain = "Sorry. I have no idea about that." 

  return assassin_brain
