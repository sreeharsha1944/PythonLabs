#!/usr/bin/env python3
def main():
    charCount = lineCount = 0
    with open(input("Enter a file name: "), "r") as aFile:
        while True:
            txt = aFile.readline()
            if not txt:
                break
            charCount += len(txt)
            lineCount += 1

    print("Characters:", charCount, " Lines:", lineCount)

if __name__ == "__main__": main()