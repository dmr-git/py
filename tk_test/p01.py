#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title("p01.py")

lbl0 = Label(text="Enter Name:")
lbl0.grid(row=0, column=0)

e = Entry(root)
e.grid(row=0, column=1)


def f1():
    msg = "Hello " + e.get()
    lbl1 = Label(text=msg)
    lbl1.grid()


btn1 = Button(root, text="Click Me", padx=10, command=f1)
btn1.grid(row=1, column=0)

root.mainloop()
