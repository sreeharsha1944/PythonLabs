#!/usr/bin/env python3
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename

def setBgColor():
	triple, hexstr = askcolor()
	if hexstr:
		print(hexstr, triple)
		btn1.config(bg=hexstr)

def find():
	ans = askopenfilename()
	f = open(ans, "r")
	lines = f.readlines()
	for line in lines: t.insert(END, line)

def cls(): t.delete(1.0,END)

def main():
	global t, btn1
	root = Tk()
	btn1 = Button(root, text="Choose a Color",
	              command = setBgColor)
	btn1.config(height=2, font=("Courier", 20, 'bold'))
	btn1.pack()
	Button(text="Open File", command=find).pack()
	Button(text="Clear", command=cls).pack()
	t = Text(height=10, width=70)
	t.pack(expand=YES, fill=BOTH)
	root.mainloop()
	
if __name__ == "__main__": main()