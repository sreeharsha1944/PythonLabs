#!/usr/bin/env python3
from tkinter import *
def main():
    root = Tk()
    Label(root, text="Hello, world!", fg="red",
              font=("Helvetica", 30)).pack()
    root.mainloop()

if __name__ == "__main__": main()