import shutil
import sys
import os


def main():

    #Make directories
    try:
        os.mkdir("../corpora")
        print("corpora created!")
    except FileExistsError:
        print("directory already exists")

    try:
        os.mkdir("../corpora/books+letters")
        print("corpora/books+letters successfully created!")
    except FileExistsError:
        print("directory already exists")

    try:
        os.mkdir("../corpora/letters+pages")
        print("corpora/letters+pages successfully created!")
    except FileExistsError:
        print("directory already exists")

    #copy files
    files = os.listdir("../Jefferson Papers/To_Jefferson")
    for f in files:
        shutil.copyfile("../Jefferson Papers/To_Jefferson/"+f, "../corpora/books+letters/"+f)
        shutil.copyfile("../Jefferson Papers/To_Jefferson/"+f, "../corpora/letters+pages/"+f)

    files = os.listdir("../Jefferson Papers/From_Jefferson")
    for f in files:
        shutil.copyfile("../Jefferson Papers/From_Jefferson/"+f, "../corpora/books+letters/"+f)
        shutil.copyfile("../Jefferson Papers/From_Jefferson/"+f, "../corpora/letters+pages/"+f)


    for root, dirs, files in os.walk("../HRTC Books/TJBooks"):
        for directory in dirs:
            shutil.copytree("../HRTC Books/TJBooks/" + directory, "../corpora/books+letters/"+directory)
            files = os.listdir("../HRTC Books/TJBooks/"+directory)
            for f in files:
                newName = directory+f
                shutil.copyfile("../HRTC Books/TJBooks/"+directory+"/"+f, "../corpora/letters+pages/"+newName)

    shutil.rmtree("../Jefferson Papers/")
    shutil.rmtree("../jeff")

if __name__ == '__main__':
    main()
