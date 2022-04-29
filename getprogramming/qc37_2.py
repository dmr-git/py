#!/usr/bin/env python3

import tkinter

w1 = tkinter.Tk()
w2 = tkinter.Tk()
w3 = tkinter.Tk()
w4 = tkinter.Tk()

w1.geometry("500x200")
w1.title("go go go")
w1.configure(background="green")

w2.geometry("100x900")
w2.title("Tall One")
w2.configure(background="red")

w3.geometry("100x100")
w3.title("")
w3.configure(background="white")

w4.geometry("100x100")
w4.title("")
w4.configure(background="black")

w1.mainloop()
w2.mainloop()
w3.mainloop()
w4.mainloop()
