import os
import glob
import json
from upload import upload_image
from auth import authenticate



currentFiles = glob.glob("*png")


imagesToUpload=[]

def updateFiles():
    with open('lastFiles.txt', 'w+') as filehandle:
        json.dump(currentFiles, filehandle)

if len(currentFiles) == 0:
    updateFiles()

with open('lastFiles.txt', 'r') as filehandle:
    lastFiles = json.load(filehandle)

newImages = list(set(currentFiles) - set(lastFiles))

if len(newImages) > 0:
    client = authenticate()
    for imagen in newImages:
        print("Nueva imagen detectada: "+ imagen)
        image = upload_image(client,imagen)
        print("Image was posted!")
        imageURL = str("{0}".format(image['link']))
        imagesToUpload.append(imageURL)

    print("Image links are:")
    for item in imagesToUpload:
        print(item)

    updateFiles()
else:
    print("There are no new images")
