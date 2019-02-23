import sys
import os

def main():
    files = os.listdir("Jefferson_Papers/from")

    for file in files:
        splits = file.split("thomas jefferson ")
        os.rename("Jefferson_Papers/from/"+file, "Jefferson_Papers/from/"+splits[len(splits)-1])

if __name__ == '__main__':
    main()