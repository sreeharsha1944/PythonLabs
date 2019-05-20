#!/usr/bin/env python3
from tkinter import *
from tkinter.messagebox import askyesno, showinfo
def go():
    print("go")
def callback():
    if askyesno('Verify', 'Really Quit'):
        showinfo("Quiting", "Quit has been selected")
        root.destroy()
def main():
    global root
    root = Tk()
    root.geometry("150x50")
    b1 = Button(root, text="quit", command=callback)
    b1.pack(side=LEFT)
    b2 = Button(root, text="keep going", command=go)
    b2.pack(side=LEFT)
    root.mainloop()
if __name__ == "__main__": main()