#!/usr/bin/env python3

from tkinter import *

from tkinter import messagebox

window = Tk()
window.geometry("200x200+20+50")
window.title("My First GUI")

def hello_call_back():
    msg = messagebox.showinfo("Hello Python", "Hellp World")

B = Button(window, text="Hello", command=hello_call_back)
B.place(x=50, y=50)

window.mainloop()
