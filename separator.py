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

    


if __name__ == '__main__':
    main()