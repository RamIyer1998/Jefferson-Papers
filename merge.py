import sys
import os


def main():
    files = os.listdir("Jefferson_Papers/From")
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
            os.rename("jeff/to/"+file, "Jefferson_Papers/From/"+file)


if __name__ == '__main__':
    main()
