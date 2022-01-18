import eyed3
import os


def applyMetadataToSingeFile(filename):
    artist = filename.split("-")[0]
    song = filename.split("-")[1][:-4]
    audiof = eyed3.load(filename)
    if not audiof.tag:
        audiof.initTag()
    audiof.tag.artist = artist
    audiof.tag.title = song
    audiof.tag.save()


def applyMetadataToFolder(folderName):
    prefix = "./"
    folder = prefix + folderName
    os.chdir(folder)
    for i in os.listdir():
        try:            
            if i.find("-") == -1 and i.find(".mp3") == -1:
                continue
            artist = i.split("-")[0]
            song = i.split("-")[1][:-4]
            audiof = eyed3.load(i)
            if not audiof.tag:
                audiof.initTag()
            audiof.tag.artist = artist
            audiof.tag.title = song
            audiof.tag.save()
        except:
            continue


choice = input("Apply metadata on Folder/File: ")
choice = choice.lower()
if choice == "folder":
    fldnm = input ("Enter child folder name: ")
    applyMetadataToFolder(fldnm)
elif choice == "file":
    flnm = input ("Enter file name: ")
    if flnm.find(".mp3")==-1:
        flnm+=".mp3"
    applyMetadataToSingeFile(flnm)
else:
    print ("Incorrect name")
