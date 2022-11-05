from tkinter import *

root = Tk()

root.geometry("300x200")
root.title("Spinbox")

w= Label(root,text="Spinbox")
w.pack()

sp = Spinbox(root,from_ = 0, to = 20)
sp.pack()
root.mainloop()