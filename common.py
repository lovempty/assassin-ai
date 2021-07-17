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
  return wikipedia.summary(keyword, sentences = 2) 

def open(link = ""):
  webbrowser.open(link)

def getAJoke():
  return pyjokes.get_joke(language="en", category="all")

def getWolfAnswer(question):    
  app_id = '7G3EKL-JG5WXVA89K'
  client = wolframalpha.Client(app_id)
  res = client.query(question)
  return next(res.results).text

def yesOrNo():
  n = random.randint(0,1)
  return ['yes','no'][n]