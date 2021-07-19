from datetime import date, datetime
import wikipedia 
import webbrowser
import pyjokes
import wolframalpha
import random

def getCurrentDate(): 
  today = date.today()
  d2 = today.strftime("%B %d, %Y")
  return d2

def getCurrentTime(): 
    now = datetime.now()
    return now.strftime("%H hours %M minutes")

def wiki(keyword = ""):
  try:
    return wikipedia.summary(keyword, sentences = 2) 
  except:
    return "I don't know that thing. Please give me more information. Maybe I can help"

def open(link = ""):
  webbrowser.open(link)

def getAJoke():
  return pyjokes.get_joke(language="en", category="all")

def getWolfAnswer(question):
  try:    
    app_id = '7G3EKL-JG5WXVA89K'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    return next(res.results).text
  except:
    return "Sorry. I have no idea about that."

def yesOrNo():
  n = random.randint(0,1)
  return ['yes','no'][n]

def wishMe():
  hour = int(datetime.now().hour)
  if hour>= 0 and hour<12:
      return "Good Morning Sir !"

  elif hour>= 12 and hour<18:
      return "Good Afternoon Sir !" 

  else:
      return "Good Evening Sir !"

def calAge():
  now = datetime.now();
  return str((now - datetime.strptime('Jul 15 2021', '%b %d %Y')).days) + " days"

