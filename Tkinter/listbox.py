from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("list")

lbl = Label(root,text="CourseList",font="comicsansms 15 bold")
lbl.pack()

CourseList = ["Software","Animation","It-ims"]
var = Variable(value=CourseList)

lbox = Listbox(root,selectmode="Multiple",font="Arial 20",listvariable=var)
lbox.pack()

root.mainloop()