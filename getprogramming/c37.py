#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.geometry("800x200")
window.title("My First GUI")
window.configure(background="grey")

red = tkinter.Button(window, text="Red", bg="red")
red.pack()

yellow = tkinter.Button(window, text="Yellow", bg="yellow")
yellow.pack()

green = tkinter.Button(window, text="Green", bg="green")
green.pack()

textbox = tkinter.Entry(window)
textbox.pack()

colorlable = tkinter.Label(window, height="10", width="10")
colorlable.pack()

window.mainloop()
