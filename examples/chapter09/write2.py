#!/usr/bin/env python3
import sys
def getFileName():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter file name: ")
    return filename

def main():
    f = open(getFileName(), 'w')
    f.write('This is a test.\n') 
    f.close()
if __name__ == "__main__": main()