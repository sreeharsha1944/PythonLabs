#!/usr/bin/env python3
import sys

def main():
    sys.stdout.write("Please enter some text:\n")
    x = sys.stdin.readline()
    sys.stdout.write("Standard Output\n" + x)
    sys.stderr.write("Error Output\n" + x)

if __name__ == "__main__": main()