
from datetime import datetime

album = None

def upload_image(client, image):

    config = {
    'album': album,
    'name' : "New photo",
    'title': "Screenshot",
    'description': "Another game screnshot: {0}".format(datetime.now())
    }

    print("Uploading image...")
    image = client.upload_from_path(image, config = config, anon=False)
    print("Done")
    print()

    return image
