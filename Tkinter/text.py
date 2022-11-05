from tkinter import *
import tkinter as tk 

root= Tk()

root.geometry("250x170")

T = Text(root,height=5,width=52)

l = Label(root,text="Fact of the day")
l.config(font=("Courier",14))

Fact ="""Sun rises in the East...."""

b1= Button(root,text="Next")
b2= Button(root,text="Exit",command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

T.insert(tk.END,Fact)
root.mainloop()