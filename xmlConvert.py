import sys
import os
from xml.etree import cElementTree as ET

def main():
    if len(sys.argv) <= 1:
        print("You gotta include a directory bud!")
        sys.exit()
    files = os.listdir(sys.argv[1]+"/")
    try:
        os.mkdir(sys.argv[1]+"/xmlFiles")
        print(sys.argv[1]+"/xmlFiles successfully created!")
    except:
        print("This already exists!")
    for file in files:
        print(file)
        #txtfile = open(sys.argv[1]+"/"+file[0:len(file)-3]+".txt", "w")
        contents = ""
        tree = ET.parse(sys.argv[1]+"/"+file)
        root = tree.getroot()
        body = root.find("text").find("body").find("div").findall("p")
        for child in body:
            contents += child.text
        print(contents)
        sys.exit()
        #txtfile.write(contents)
        #os.rename(sys.argv[1]+"/"+file, sys.argv[1]+"/xmlFiles/"+file)


        
        #print(file[0:len(file)-3] + ".txt successfully created!")

#def dir():



if __name__ == "__main__":
    main()