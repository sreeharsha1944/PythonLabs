#!/usr/bin/env python3
from tkinter import *
def grabtxt():
    global line, pos
    try:
        line, pos = ent01.get(), ent02.get()
        data = txt.get(line + "." + pos, END)
    except:
        data = "Invalid line or position #"
    print("Data:", data)

def deltxt():
    try:
        line, pos = ent01.get(), ent02.get()
        txt.delete(line + "." + pos, 'end')
    except:
        print("Unable to Delete: line=", line, "pos=", pos)

def main():
    global ent01, ent02, txt, line, pos
    line = pos = "0"
    root = Tk()
    root.title("Text Widgets")
    Label(root, text="Starting Line Number:").pack()
    ent01 = Entry(root)
    ent01.pack()
    Label(root, text="Start Position Within Line").pack()
    ent02 = Entry(root)
    ent02.pack()
    Button(root, text="Grab Text", command=grabtxt).pack()
    Button(root, text="Delete Text", command=deltxt).pack()
    Button(root, text="Quit", command=root.destroy).pack()
    txt = Text(root, height=8, width=50)
    txt.insert("end", "This is line 1\nThis is line 2")
    txt.pack()
    
    root.mainloop()
if __name__ == "__main__": main()