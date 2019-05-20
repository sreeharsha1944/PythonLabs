#!/usr/bin/env python3
from tkinter import *
def main():
    root = Tk()
    root.geometry("300x300")
    root.title("Three Frames")
    
    frame1 = Frame(root)
    Label(frame1, text="frame 1").pack()
    frame1.pack(expand=YES, fill=BOTH)

    frameA = Frame(frame1, bg="cyan")
    Label(frameA, text="frameA").pack()
    frameA.pack(side=LEFT, expand=YES, fill=X)
    
    frameB = Frame(frame1)
    Label(frameB, text="frameB").pack()
    frameB.pack(side=RIGHT)
    
    frame2 = Frame(root, bg="#00ffff")
    Label(frame2, text="frame 2").pack()
    frame2.pack(expand=YES, fill=BOTH)
    
    frame3 = Frame(root, bg="#ffff00")
    Label(frame3, text="frame 3", bg="magenta",
          font=('Helvetica', '18') ).pack()
    frame3.pack(expand=YES, fill=Y)
    
    root.mainloop()

if __name__ == "__main__": main()