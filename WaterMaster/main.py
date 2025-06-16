import RTC
import FM
from time import sleep
from os import system, popen

newData = {
    "completed":"0xFFFF",
    "tomorrow":"0xFFFF",
    "manual":"0xFFFF",
    "currentQueue":"0xFFFF",
    "cleanUpFlag":"False"
}

def main():
    print("Date:", RTC.GetDate())
    print("Time:", RTC.GetTime())
    print("yesterday date:", RTC.GetYesterdayDate())
    # FM.CreateNewJSON("10_6")
    print(FM.ReadJsonFile("10_6"))
    FM.UpdateJsonFile("10_6", newData)
    print(FM.ReadJsonFile("10_6"))
    print("Number of items in 'Data' Folder:", FM.CountItems("Data\\"))

    startTime = RTC.GetTime()
    if(startTime == str("10:46")):
        print("comparison works")

    netStatus = CheckInternetConnection()
    if(netStatus == True):
        print("Internet available")
    else:
        print("No internet!!")


    sleep(5)
    system('cls')

def CheckCurrentQueue():
    pass

def CheckCleanUpFlag():
    pass

def UpdateManualValve():
    pass

def CheckInternetConnection():
    connectionStatus    = False
    stream              = popen(f'ping -n 4 {"www.google.com"}') # For Windows
    output              = stream.read()
    resultPosition      = output.find("0% loss")
    packetLoss          = output[resultPosition : resultPosition + 7]
    
    if (packetLoss == "0% loss"):
        connectionStatus = True

    return connectionStatus
    



if __name__ == "__main__":
    main()