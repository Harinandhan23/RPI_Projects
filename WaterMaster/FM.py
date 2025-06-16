# FM - File Management module
from os import mkdir, path, scandir
import json

template = {
    "completed":"NULL",
    "tomorrow":"NULL",
    "manual":"NULL",
    "currentQueue":"NULL",
    "cleanUpFlag":"False"
}

def CreateFolder(folderName):
    try:
        mkdir(folderName)
        print(f"{folderName} folder creation success")
    except FileExistsError:
        print(f"{folderName} already exists")
    except PermissionError:
        print("permission denied :(")
    except Exception as e:
        print("error occured: {e}")
    
def IsFolderExist(folderName):
    status = False
    if path.isdir(folderName):
        status = True
    return status
    
def CreateNewJSON(fileName):
    if IsFolderExist("Data") == False:
        CreateFolder("Data")
    newTemplate = json.dumps(template, indent = 4)
    with open("Data\\" + fileName + ".json", "w") as newFile:
        newFile.write(newTemplate)
    
def UpdateJsonFile(fileName, data):
    dataDump = json.dumps(data, indent = 4)
    with open("Data\\" + fileName + ".json", 'w') as outFile:
              outFile.write(dataDump)

def ReadJsonFile(fileName):
    with open("Data\\" + fileName + ".json", 'r') as openfile:
        readData = json.load(openfile)  
    return readData

def CountItems(path):
    count = 0
    for path in scandir(path):
        if path.is_file():
            count += 1
    return count