import eyed3
import os

path = "/home/gergely/Music"
files = os.listdir(path)
errors = []

for _ ,file in enumerate(files):
    try:
        audiofile = eyed3.load(os.path.join(path, file))
        # Expected file name: Artist - Title.mp3
        title = (file.split(".mp3")[0]).split(" - ")[1]
        artist = (file.split(".mp3")[0]).split(" - ")[0]

        if audiofile.tag.title != artist or audiofile.tag.artist != title:
            print(artist, "-", title)
        
        if audiofile.tag.title != title:
            audiofile.tag.title = title
            audiofile.tag.save()
        
        if audiofile.tag.artist != artist:
            audiofile.tag.artist = artist
            audiofile.tag.save()
    except:
        errors.append(file)
        continue

if len(errors) > 0:
    print("------------------")
    print("Errors:")

    for file in files:
        print(file)