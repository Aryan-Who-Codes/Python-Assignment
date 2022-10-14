from email import message
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("300x150")
root.title("practice")

def fun():
    messagebox.showinfo("Hello","Red Button Clicked")

def fun2():
    messagebox.showinfo("Hello","Blue Button Clicked")

def fun3():
    messagebox.showinfo("Hello","Green Button Clicked")

def fun4():
    messagebox.showinfo("Hello","Yellow Button Clicked")


b1= Button(root,text="red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=Button(root,text="blue",command=fun2,activeforeground="blue",activebackground="lightblue",pady=10)
b3= Button(root,text="green",command=fun3,activeforeground="green",activebackground="lightgreen",pady=10)
b4=Button(root,text="yellow",command=fun4,activeforeground="orange",activebackground="lightyellow",pady=10)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
root.mainloop()