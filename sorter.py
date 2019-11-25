import glob
import json

currentFiles = glob.glob("*")

def updateFiles():
    with open('lastFiles.txt', 'w+') as filehandle:
        json.dump(currentFiles, filehandle)

with open('lastFiles.txt', 'r') as filehandle:
    lastFiles = json.load(filehandle)

newImages = list(set(currentFiles) - set(lastFiles))

if len(newImages) > 0:
    for image in newImages:
        print(image)
        #Do something with those files
        updateFiles()
else:
    print("There are no new images")
