import sys
import os


def main():
    try:
        os.mkdir("Jefferson Papers/From_Jefferson")
        print("Directory 'From_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    try:
        os.mkdir("Jefferson Papers/To_Jefferson")
        print("Directory 'To_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    files = os.listdir("Jefferson Papers/")
    #print(len("Thomas Jefferson to"))
    #sys.exit()

    count = 0

    for file in files:
        if file == "From_Jefferson" or file == "To_Jefferson" or file == "xmlFiles":
            continue
        
        if file[0:16] == "thomas jefferson":
            #print(file)
            os.rename("Jefferson Papers/"+file, "Jefferson Papers/From_Jefferson/"+file)
            count += 1
        else:
            if file == "william h. cabell from thomas jefferson, june 29, 1807.txt":
                os.rename("Jefferson Papers/"+file, "Jefferson Papers/From_Jefferson/"+file)
            else:
                os.rename("Jefferson Papers/"+file, "Jefferson Papers/To_Jefferson/"+file)

    #print(count)


if __name__ == '__main__':
    main()