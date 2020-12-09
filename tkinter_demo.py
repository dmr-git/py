#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# Filename:     template.py 
# Author:       DMR

# remember to use 'chmod u+x filename.py' to make the script executable

import tkinter

root = tkinter.Tk()
label = tkinter.Label(root,text='Hello from TKinter')
label.pack()
text = tkinter.Entry(root)

def buttonclick():
    text.get()

button = tkinter.Button(root,text='Enter something: ',command=buttonclick)
button.pack(side='left')
text.pack(side='left')

root.mainloop()


