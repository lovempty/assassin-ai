from datetime import date, datetime

def getCurrentDate(): 
  today = date.today()
  d2 = today.strftime("%B %d, %Y")
  return d2

def getCurrentTime(): 
    now = datetime.now()
    return now.strftime("%H hours %M minutes")