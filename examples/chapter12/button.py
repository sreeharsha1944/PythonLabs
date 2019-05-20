#!/usr/bin/env python3
from tkinter import *
def click():
    print("Something was clicked")
    
def main():
    root = Tk()
    root.geometry("300x75")
    root.title("Button Example")
    Label(root, text="Hello").pack(side=LEFT)
    b = Button(root, text="Press Me",command=click)
    b.pack()
    root.mainloop()
    
if __name__ == "__main__": main()