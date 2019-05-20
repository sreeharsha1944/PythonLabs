#!/usr/bin/env python3
import datetime
def main():
    f = open('output', 'w')
    aList = [1,2,3]
    today = datetime.datetime.today()
    # f.write(today)  ~ Will not work since not a string
    f.write(str(aList) + "\n")
    f.write(str(today) + "\n")
    f.close()

if __name__ == "__main__": main()