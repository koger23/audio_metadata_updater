import eyed3
import os

path = "/home/gergely/Music"
files = os.listdir(path)
errors = []

for _ ,file in enumerate(files):
    try:
        audiofile = eyed3.load(os.path.join(path, file))
        # Expected file name: Artist - Title.mp3
        artist = (file.split(".mp3")[0]).split(" - ")[1]
        title = (file.split(".mp3")[0]).split(" - ")[0]
        print(artist, "-", title)
        audiofile.tag.title = artist
        audiofile.tag.artist = title
        audiofile.tag.save()
    except:
        errors.append(file)
        continue

if len(errors) > 0:
    for file in files:
        print(file)