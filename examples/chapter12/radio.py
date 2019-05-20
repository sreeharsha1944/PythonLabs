#!/usr/bin/env python3
from tkinter import *
def results():
    if not var1.get():
        print("Nothing Selected")
        return
    print(txt[var1.get() - 1])
    
def main():
    global var1, txt
    root = Tk()
    root.title("Radio Buttons")
    var1 = IntVar()
    Label(root, text="Select A Favorite Sport").pack()
    Button(root, text="Get Selection",
           command=results).pack(side=TOP)
    txt = ["Basketball", "Football", "Baseball"]
    for idx, sport in enumerate(txt):
        Radiobutton(root, text=sport, variable=var1,
                    value=idx + 1).pack(side=LEFT)
    root.mainloop()
    
if __name__ == "__main__": main()