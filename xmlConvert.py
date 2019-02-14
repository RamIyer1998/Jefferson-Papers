import sys
import os
from xml.etree import cElementTree as ET

def main():
    count = 1
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
        counts = 0
        print(file)
        if file == ".DS_Store":
            continue
        if file == "xmlFiles":
            continue
        if file[-4:] == ".txt":
            continue
        txtfile = open(sys.argv[1]+"/"+file[0:len(file)-3]+".txt", "w")
        contents = ""
        tree = ET.parse(sys.argv[1]+"/"+file, ET.XMLParser(encoding='utf-8'))
        root = tree.getroot()

        body = root.find("text").find("body").find("div")
        
        counts = 0
        for child in body:
            if child.tag == "note":
                counts += 1
                continue
            if child.tag == "pageinfo":
                counts += 1
                continue
            for text in child.itertext():
                contents += text.strip()
                if counts < 6:
                    contents += "\n"
                counts += 1
                
        
            

        print(contents)
        print()
        print(contents[-1])
        #sys.exit()
        count += 1
        txtfile.write(contents)
        os.rename(sys.argv[1]+"/"+file, sys.argv[1]+"/xmlFiles/"+file)


        
        #print(file[0:len(file)-3] + ".txt successfully created!")

#def dir():



if __name__ == "__main__":
    main()