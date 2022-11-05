from tkinter import *

root = Tk()

root.title("Menu")

menubar = Menu(root)

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "file",menu=file)
file.add_command(label = "file",command=None)
file.add_command(label = "New file",command=None)
file.add_command(label = "Open...",command=None)
file.add_command(label = "Save",command=None)

file.add_separator()
file.add_command(label="Exit",command = root.destroy)


root.config(menu=menubar)
root.mainloop()