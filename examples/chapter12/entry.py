#!/usr/bin/env python3
from tkinter import *
import os

def listfiles():
    print("Listing Files from " + ent01.get())
    files = os.listdir(ent01.get())
    for file in files:
        print(file)
    print("++++++++++++")
def dele():
    ent01.delete(0, 'end')
def stop():
    master.destroy()
def main():
    global ent01, master
    master = Tk()
    master.title("Directories")
    Label(master, text="Directory Name:").pack(side=TOP)
    ent01 = Entry(master, width=30)
    ent01.pack()
    #ent01.focus_set()
    Button(master, text="List Files", width=10,
           command=listfiles).pack()
    Button(master, text="Quit", width=10,
           command=stop).pack()
    Button(master, text="Delete Text", width=10,
           command=dele).pack()
    master.mainloop()
if __name__ == "__main__": main()