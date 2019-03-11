import os
import sys

def main():
    try:
        os.mkdir("jeff/from")
        print("from_jeff successfully created!")
    except FileExistsError:
        print("directory already exists")

    try:
        os.mkdir("jeff/to")
        print("jeff/to successfully created!")
    except FileExistsError:
        print("directory already exists")
    
    try:
        os.mkdir("jeff/other")
        print("jeff/other successfully created!")
    except FileExistsError:
        print("directory already exists")

    files = os.listdir("jeff/")
    for file in files:
        if file == "other" or file == "to" or file == "from":
            continue
        x = file.split("--")
        #print(x[len(x)-1].replace("_", " "))
        
        if x[len(x)-1][0:2] == "TO":
            os.rename("jeff/"+file, "jeff/to/"+x[len(x)-1].replace("_"," ").lower())
            #os.rename("jeff/"+file, "jeff/")
        elif x[len(x)-1][0:4] == "FROM":
            os.rename("jeff/"+file, "jeff/from/"+x[len(x)-1].replace("_"," ").lower())
        else:
            os.rename("jeff/"+file, "jeff/other/"+file.replace("_"," ").lower())

if __name__ == '__main__':
    main()