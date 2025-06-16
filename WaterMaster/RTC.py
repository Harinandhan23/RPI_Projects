from datetime import datetime, date, timedelta

def GetTime():
    currentTime = datetime.now()
    time = currentTime.strftime("%H:%M") #24 hr format
    return time

def GetDate():
    currentDate = datetime.now()
    date = currentDate.strftime("%d_%m")
    return date

def GetYesterdayDate():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    dateOfYesterday = yesterday.strftime("%d_%m")
    return dateOfYesterday