#speech recognition
import speech_recognition

assassin_ear = speech_recognition.Recognizer()
def listen():
  with speech_recognition.Microphone() as mic:
    print("Assassin: I'm listening to you, say something my boy")
    print("Listening...")
    audio =assassin_ear.record(mic, duration=3)
  try:
    you = assassin_ear.recognize_google(audio)
  except:
    you = "Sorry. I cannot hear you :("
  return you
  