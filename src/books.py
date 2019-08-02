import os
import os.path
import shutil

def bookConversion():
    # Make a folder for all of the new txt files
    try:
        os.mkdir("HRTC Converted Books")
    except FileExistsError:
        print("aw shucks it already exists")

    # For each book's directory, compile all of the pages into one txt file
    path = "./"+'HRTC Books'+"/TJBooks/"
    for root, dirs, files in os.walk(path):
        for directory in sorted(dirs):
            book_name = "./" + "HRTC Converted Books/" + directory +".txt"
            with open(book_name, "ab") as outfile:
                for x, y, z in os.walk(path + directory):
                    for name in sorted(z):
                        with open(os.path.join(x, name), 'rb') as infile:
                            shutil.copyfileobj(infile, outfile)

    # Make a folder for the new corpus
    try:
        os.mkdir("corpora/books+letters")
        print("corpora/books+letters successfully created!")
    except FileExistsError:
        print("directory already exists")

    # Copy the Jefferson letters to the corpora folder
    files = os.listdir("Jefferson Papers/From_Jefferson")
    for f in files:
        shutil.copyfile("Jefferson Papers/From_Jefferson/"+f, "corpora/books+letters/"+f)

    # Copy files from 'HRTC Converted Books' to the new corpora folder
    files = os.listdir("HRTC Converted Books/")
    for f in files:
        shutil.copyfile("HRTC Converted Books/" + f, "corpora/books+letters/" + f)

    # Delete 'HRTC Converted Books'
    shutil.rmtree("HRTC Converted Books/")


if __name__ == '__main__':
    bookConversion()
