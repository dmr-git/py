#!/usr/bin/env python3

# Filename:     tkinter_demo.py
# Author:       DMR

import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text="Hello from TKinter")
label.pack()
text = tkinter.Entry(root)


def buttonclick():
    text.get()


button = tkinter.Button(root, text="Enter something: ", command=buttonclick)
button.pack(side="left")
text.pack(side="left")

root.mainloop()
