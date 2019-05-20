#!/usr/bin/env python3
def main():
    with open("output", "w") as aFile:
        while True:
            data = input("Enter data ('q' to exit): ")
            if data == "q":
                break
            print(data, file=aFile)

    print("File Is Now Closed? ", aFile.closed)
if __name__ == "__main__": main()