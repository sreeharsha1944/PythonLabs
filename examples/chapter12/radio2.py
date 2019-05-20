#!/usr/bin/env python3
from tkinter import *
import calendar

def results():
    print(var.get())

def main():
    global var
    root = Tk()
    root.title("Days of the Week")
    Label(root, text="Select A Day").pack()
    daysLong = list(calendar.day_name)
    daysAbbr = list(calendar.day_abbr)
    var = StringVar()
    for dayLong, dayAbbr in zip(daysLong, daysAbbr):
        Radiobutton(root, value=dayLong, text = dayAbbr,
                    variable = var,
                    command=results).pack(side=LEFT)
    root.mainloop()

if __name__ == "__main__": main()