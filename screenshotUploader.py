import os
import glob
import json
import mv

currentFiles = glob.glob("*png")

imagesToUpload=[]

final =

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

    for item in imagesToUpload:
        itemtopost = "[IMG]" + item + "[/IMG]"
        final.append(itemtopost)
    updateFiles()
else:
    print("There are no new images")
