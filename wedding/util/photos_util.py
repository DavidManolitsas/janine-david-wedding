import os


def all_photos(path: str):
    for photo in os.scandir(path):
        yield photo
