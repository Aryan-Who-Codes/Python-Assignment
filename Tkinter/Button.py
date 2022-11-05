from tkinter import *
from turtle import left

root= Tk()
root.geometry("655x333")

f1= Frame(root, bg = "black", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

def hello():
    print("Hello Tkinter")
    
def name():
    print("Name is Aryan.")

b1= Button(f1, bg="red",fg="white",text="Print now",command=hello)
b1.pack(side=LEFT,padx=10)  

b2= Button(f1, bg="red",fg="white",text="Tell me name now",command=name)
b2.pack(side=LEFT,padx=10)

b3= Button(f1, bg="red",fg="white",text="Print now")
b3.pack(side=LEFT,padx=10)

b4= Button(f1, bg="red",fg="white",text="Print now")
b4.pack(side=LEFT,padx=10)
 
root.mainloop()