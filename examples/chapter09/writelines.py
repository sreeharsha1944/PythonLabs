#!/usr/bin/env python3
def getData():
    theList = []
    while True:
        data = input("Enter data ('q' to exit): ")
        if data == "q":
            break
        theList.append(data)
    return theList    

def main():
    data = getData()
    f = open("output", "a")
    f.writelines(data)
    f.close()
if __name__ == "__main__": main()