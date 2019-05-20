#!/usr/bin/env python3
from tkinter import *
import os
def getselected():
    item = listbox.curselection()
    li = list(item)
    if not li:
        print("No selection!")
        return
    for i in li:
        print(listbox.get(i))
def main():
    global listbox
    root = Tk()
    root.title("List Boxes")
    Label(root, text="Select from List").pack()
    listbox = Listbox(root, selectmode=MULTIPLE)
    listbox.pack()
    Button(root, text="Get Selection",
           command=getselected).pack()
    for item in os.listdir("."):
        listbox.insert(END, item)
    root.mainloop()
if __name__ == "__main__": main()