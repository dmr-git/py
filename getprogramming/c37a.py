#!/usr/bin/env python3

import tkinter

# button colors do not work on macosx, so below is a workaround
# to use, I went to virtual environment and ran
# python3 -m pip install tkmacosx

from tkmacosx import Button as button

def change_bg():
    cl = "red"
    window.configure(background=cl)

def change_bg_white():
    window.configure(background="white")

def change_bg_red():
    window.configure(background="red")

def change_bg_green():
    window.configure(background="green")

window = tkinter.Tk()
window.geometry("800x200")
window.title("My First GUI")
window.configure(background="grey")

red = button(window, text="Red", bg="red", command=change_bg)
red.pack()

white = button(window, text="White", bg="white", command=change_bg_white)
white.pack()

green = button(window, text="Green", bg="green", command=change_bg_green)
green.pack()

textbox = tkinter.Entry(window)
textbox.pack()

colorlable = tkinter.Label(window, height="10", width="10", bg="red")
colorlable.pack()

window.mainloop()
