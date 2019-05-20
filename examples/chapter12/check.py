#!/usr/bin/env python3
from tkinter import *

def listSports():
    result = "Selected Sports: "
    for chkbtn, state in zip(chkbtns, chkbtnStates):
        if state.get():
            result += chkbtn["text"] + " "
            chkbtn.deselect()
    print(result)

def listStates():
    print("Checkbutton States:")
    for chkbtn, state in zip(chkbtns, chkbtnStates):
        print("\t", chkbtn["text"], ":", state.get(),
              sep="")
def main():
    global chkbtns, chkbtnStates
    root = Tk()
    root.title("Checkboxes Example")
    chkbtnStates = [IntVar(), IntVar(), IntVar()]
    Label(root, text="Select Favorite Sports").pack()
    Button(root, text="List Selected Sports", 
           command=listSports).pack(side=TOP)
    Button(root, text="List All Checkbutton States",
                command=listStates).pack(side=TOP)
    c1 = Checkbutton(root, text="Basketball",
                     variable=chkbtnStates[0])
    c2 = Checkbutton(root, text="Football",
                     variable=chkbtnStates[1])
    c3 = Checkbutton(root)
    c3["text"] = "Baseball"          # setting properties
    c3["variable"] = chkbtnStates[2] # as key/value pairs
    chkbtns = [c1,c2,c3]
    for chkbtn in chkbtns:
        chkbtn.pack(side=LEFT)
    root.mainloop()
if __name__ == "__main__": main()