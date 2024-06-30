import os


def all_photos(path: str):
    for photo in os.scandir(path):
        if photo.path.endswith(".jpg") or photo.path.endswith(".JPG"):
            yield photo
