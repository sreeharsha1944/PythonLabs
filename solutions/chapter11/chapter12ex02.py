#!/usr/bin/env python3
#
# A Solution For Chapter 12 Exercise 2
#
from tkinter import *
def display():
	fn = e1.get()
	print("file name is ", fn)
	f = open(fn, "r")
	for line in f:
		tex.insert('end', line)

def dele():
	tex.delete('1.0', 'end')

def ins():
        tex.insert('2.5', "Hello\n")

root = Tk()
lab = Label(root, text = "Enter File Name")
lab.pack()
e1 = Entry()
e1.pack()
b1 = Button(root, text="Display File", command=display)
b1.pack()
b2 = Button(root, text="DeleteText", command=dele)
b2.pack()
b3 = Button(root, text="Exit App", command=root.destroy)
b3.pack()
tex = Text(root, height=20, width=50)
tex.pack()
root.mainloop()
