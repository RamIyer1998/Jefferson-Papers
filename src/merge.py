import sys
import os


def main():
    files = os.listdir("Jefferson Papers/From_Jefferson")
    merge_files = os.listdir("jeff/to")
    with open("merge.txt") as f:
        merge_ok = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    merge_ok = [x.strip() for x in merge_ok]
    
    for file in merge_files:
        document = file.split(" ")
        if document[len(document)-1][0] != "1":
            if "," in document[len(document)-1]:
                splitComma = document[len(document)-1].split(",")
                splitComma[0] = splitComma[0]+","
                newDoc = ""
                for y in range(len(document)-1):
                    newDoc += document[y] + " "
                newDoc += splitComma[0]+" "
                newDoc += splitComma[1]
                #print(newDoc)
                os.rename("jeff/to/"+file, "jeff/to/"+newDoc)
            else:
                if file in merge_ok:
                    os.rename("jeff/to/"+file, "Jefferson Papers/From_Jefferson/"+file)
    
    merge_files = os.listdir("jeff/to")

    for file in merge_files:
        document = file.split(" ")
        merge = True
        for comp in files:
            comp_doc = comp.split(" ")
            for x in range(1, 5):
                if document[len(document)-x] != comp_doc[len(comp_doc)-x]:
                    break
                if x == 4:
                    merge = False
        if merge:
            os.rename("jeff/to/"+file, "Jefferson Papers/From_Jefferson/"+file)

    merge_files = os.listdir("jeff/other")
    for file in merge_files:
        if file in merge_ok:
            os.rename("jeff/other/"+file, "Jefferson Papers/From_Jefferson/"+file)
    
    files = os.listdir("Jefferson Papers/To_Jefferson")
    merge_files = os.listdir("jeff/from")
    for file in merge_files:
        os.rename("jeff/from/"+file, "Jefferson Papers/To_Jefferson/"+file)

    




if __name__ == '__main__':
    main()
