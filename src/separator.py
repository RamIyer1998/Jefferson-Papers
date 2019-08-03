import sys
import os


def main():
    try:
        os.mkdir("../Jefferson Papers/From_Jefferson")
        print("Directory 'From_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    try:
        os.mkdir("../Jefferson Papers/To_Jefferson")
        print("Directory 'To_Jefferson' Created")
    except FileExistsError:
        print("Directory already made")

    files = os.listdir("../Jefferson Papers/")
    #print(len("Thomas Jefferson to"))
    #sys.exit()

    with open("../changes.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    count = 0

    for file in files:
        if file == "From_Jefferson" or file == "To_Jefferson" or file == "xmlFiles":
            continue

        if file[0:16] == "thomas jefferson":
            #print(file)
            os.rename("../Jefferson Papers/"+file, "../Jefferson Papers/From_Jefferson/"+file)
            count += 1
        else:
            if file == "william h. cabell from thomas jefferson, june 29, 1807.txt":
                os.rename("../Jefferson Papers/"+file, "../Jefferson Papers/From_Jefferson/to william h. cabell, june 29, 1807.txt")
            elif file == "george washington from thomas jefferson, january 15, 1792, with copy.txt":
                os.rename("../Jefferson Papers/"+file, "../Jefferson Papers/From_Jefferson/to george washington, january 15, 1792.txt")
            elif file == "john mason from thomas jefferson, august 18, 1814.txt":
                os.rename("../Jefferson Papers/"+file, "../Jefferson Papers/From_Jefferson/to john mason, august 18, 1814.txt")
            else:
                new_file = file
                for x in content:
                    if file in x:
                        new_file = x.split(" -> ")[len(x.split(" -> "))-1]
                os.rename("../Jefferson Papers/"+file, "../Jefferson Papers/To_Jefferson/"+new_file)

    #print(count)


if __name__ == '__main__':
    main()
