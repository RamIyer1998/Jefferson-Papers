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

        if file == "Thomas Jefferson, July 27, 1821, Autobiography Draft Fragment, January 6 through July 27.xml":
            os.rename(sys.argv[1]+"/"+file, sys.argv[1]+"/xmlFiles/"+file)
            continue

        counts = 0
        #print(file)
        if file == ".DS_Store":
            continue
        if file == "xmlFiles":
            continue
        if file[-4:] == ".txt":
            continue
        txtfile = open(sys.argv[1]+"/"+file[0:len(file)-4].lower()+".txt", "w")
        contents = ""
        tree = ET.parse(sys.argv[1]+"/"+file, ET.XMLParser(encoding='utf-8'))
        root = tree.getroot()

        for element in root.iter():
            for child in list(element):
                if child.tag == 'note':
                    if child.tail:
                        tail = child.tail.strip()
                        if element.text:
                            element.text = element.text.strip() +" "+tail
                        else:
                            element.text = tail
                    element.remove(child)
                if child.tag == 'pageinfo':
                    if child.tail:
                        tail = child.tail.strip()
                        if element.text:
                            element.text = element.text.strip() +" "+tail
                        else:
                            element.text = tail
                    element.remove(child)
                if child.tag == 'anchor':
                    if child.tail:
                        tail = child.tail.strip()
                        if element.text:
                            element.text = element.text.strip() +" "+tail
                        else:
                            element.text = tail
                    element.remove(child)

        body = root.find("text").find("body").find("div")


        counts = 0
        for child in body.iter():

            if child.text:
                if child.tail:
                    child.text += " " + child.tail.strip()
                contents += " " + child.text + "\n"

            elif child.tail:
                contents += " " + child.tail.strip()

            if child.tag == "p":
                contents += "\n"
                counts += 1

        #print(contents)
        #print()
        #print(contents[-1])
        count += 1
        txtfile.write(contents)
        os.rename(sys.argv[1]+"/"+file, sys.argv[1]+"/xmlFiles/"+file)



        #print(file[0:len(file)-4] + ".txt successfully created!")


#def dir():



if __name__ == "__main__":
    main()
