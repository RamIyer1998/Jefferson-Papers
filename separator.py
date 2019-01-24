import sys
import os


def main():
    try:
        os.mkdir("From_Jefferson")
        print("Directory 'From_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    try:
        os.mkdir("To_Jefferson")
        print("Directory 'To_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    files = os.listdir("Jefferson_Papers/")
    #print(len("Thomas Jefferson to"))
    #sys.exit()

    count = 0

    for file in files:
        if file[0:16] == "Thomas Jefferson":
            print(file)
            os.rename("Jefferson_Papers/"+file, "From_Jefferson/"+file)
            count += 1
        else:
            os.rename("Jefferson_Papers/"+file, "To_Jefferson/"+file)

    print(count)


if __name__ == '__main__':
    main()