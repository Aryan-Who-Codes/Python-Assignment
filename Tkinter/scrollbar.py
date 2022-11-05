from tkinter import *

root = Tk()

root.geometry("150x200")

w= Label(root,text="Scrollbar",font="50").pack()

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT,fill=Y)

mylist = Listbox(root,yscrollcommand=scroll_bar.set)
for i in range(1,26):
    mylist.insert(END,"number "+str(i))
mylist.pack(side=LEFT,fil=BOTH)

scroll_bar.config(command=mylist.yview)
root.mainloop()