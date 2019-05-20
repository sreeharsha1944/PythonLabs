#!/usr/bin/env python3
from tkinter import *

def notyet():
    print("This event handler does nothing yet")

def main():
    root = Tk()		
    menubar = Menu(root)       # will act as menubar
    root.config(menu=menubar)  # assign as menu of root
    filemenu = Menu(menubar)
    filemenu.add_command(label="New", command=notyet)
    filemenu.add_separator()
    filemenu.add_command(label="Save", command=notyet)
    filemenu.add_command(label="SaveAs",command=notyet)
    
    menubar.add_cascade(label="File",menu=filemenu)
    
    editmenu = Menu(menubar)
    editmenu.add_command(label="Cut", command=notyet)
    editmenu.add_command(label="Copy", command=notyet)
    editmenu.add_command(label="PaSte",command=notyet)
    
    menubar.add_cascade(label="Edit",menu=editmenu)
    
    root.mainloop()

if __name__ == "__main__": main()
