#speech recognition
import speech_recognition

assassin_ear = speech_recognition.Recognizer()
def listen():
  with speech_recognition.Microphone() as mic:
    print("Listening...")
    audio =assassin_ear.record(mic, duration=3)
  try:
    question = assassin_ear.recognize_google(audio)
    print("Synth: " + question)
  except:
    question = "no_sound"
  return question
  