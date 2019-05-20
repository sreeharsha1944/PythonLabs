#!/usr/bin/env python3
def main():
    f = open('output', 'w')
    print("Type of stream:", type(f).__name__)
    print("Module it is found in:", type(f).__module__)
    f.write('This is a test.\n') 
    f.write('This is another test.\n') 
    f.close()

if __name__ == "__main__": main()