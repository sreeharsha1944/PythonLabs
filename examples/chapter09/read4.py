#!/usr/bin/env python3
import string
def main():
    try:
        with open("alphabet", "w") as theFile:
            theFile.write(string.ascii_letters)
        print("The following was written to the file:")
        print(string.ascii_letters, "\n")
        
        with open("alphabet", "r") as theFile:
            while True:
                theText = theFile.read(10)
                if not theText:
                    break
                print(theText)
    except OSError as err:
        print("IO Error:", err)

if __name__ == "__main__": main()