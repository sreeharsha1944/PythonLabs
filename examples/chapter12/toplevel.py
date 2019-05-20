#!/usr/bin/env python3
from tkinter import *
def create():
    global top
    if top:
        top.deiconify()
        top.focus_set()
        return
    top = Toplevel(root)
    top.geometry("400x100")
    top.title("TOP LEVEL WINDOW")
    top.protocol('WM_DELETE_WINDOW', close)
    Button(top, text="CLOSE ME", command=close).pack()

def close():
    global top
    top.destroy()
    top = None
    
def main():
    global top, root
    top = None
    root = Tk()
    root.geometry("200x50-500-500")
    Button(root, text='CREATE TOP LEVEL',
           command=create).pack()
    root.mainloop()

if __name__ == "__main__": main()