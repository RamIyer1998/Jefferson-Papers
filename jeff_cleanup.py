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
    with open("changes.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for file in files:
        if file == "other" or file == "to" or file == "from":
            continue
        x = file.split("--")
        #print(x[len(x)-1].replace("_", " "))
        
        if x[len(x)-1][0:2] == "TO":
            if file == "to gouverneur morris, .txt":
                print("wtf")
            new_file = x[len(x)-1].replace("_"," ").lower()
            for x in content:
                if new_file in x:
                    new_file = x.split(" -> ")[len(x.split(" -> "))-1]
            
            

            os.rename("jeff/"+file, "jeff/to/R. "+new_file)
            #os.rename("jeff/"+file, "jeff/")
        elif x[len(x)-1][0:4] == "FROM":
            new_file = x[len(x)-1].replace("_"," ").lower()

            for x in content:
                if new_file in x:
                    new_file = x.split(" -> ")[len(x.split(" -> "))-1]
            os.rename("jeff/"+file, "jeff/from/R. "+new_file)
        else:
            new_file = file.replace("_"," ").lower()
            for x in content:
                if new_file in x:
                    new_file = x.split(" -> ")[len(x.split(" -> "))-1]
            os.rename("jeff/"+file, "jeff/other/R. " + new_file)

if __name__ == '__main__':
    main()