#!/usr/bin/env python3
from tkinter import *
from tkinter.messagebox import showerror
def cls():
    txt.delete('1.0','end')
def show():
    filename = entry.get()
    try:
        with open(filename, "r") as file:
            for line in file:
                txt.insert('end', line)
    except OSError:
        showerror('ERROR', 'No file ' + filename)
def main():
    global txt, entry
    Label(text="Enter File Name").pack()
    entry = Entry(width=20)
    entry.pack()
    txt = Text(height=8,width=70)
    txt.pack()
    Button(text="Show File", command=show).pack()
    Button(text="Clear Text", command=cls).pack()
    mainloop()
if __name__ == "__main__": main()