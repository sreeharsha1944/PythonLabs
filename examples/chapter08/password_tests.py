#!/usr/bin/env python3
from password_utilities import *


def checkPassword(password):
    checkTrivial(password)
    checkLength(password)
    checkDuplicates(password)


def main():
    while True:
        try:
            line = input("Please enter a password")
            checkPassword(line)
            print("That would be a valid password")
        except PasswordError as pe:
            print("Password Error: ", pe)


if __name__ == "__main__":
    main()
