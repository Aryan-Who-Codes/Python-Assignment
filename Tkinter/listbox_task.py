from tkinter import * 
                                       
root = Tk()

root.geometry("500x500")

root.title("ListBox")

def right():
    for i in lb1.curselection():
        lb2.insert(END,f"{lb1.get(i)}")
        lb1.delete(i,i)
        
def left():
    for i in lb2.curselection():
        lb1.insert(END,f"{lb2.get(i)}")
        lb2.delete(i,i)

def all_right():
    # for i in range((lb1.get(END))):
    #     print(f"{lb1.get(i)}")
    #     # lb2.insert(END,f"{lb1.get(0)}")
    #     # lb2.insert(END,f"{lb1.get(1)}")
    #     # lb2.insert(END,f"{lb1.get(2)}")
    #     for i in range(len(lb1.get(i))):
    #         lb2.insert(i,f"{lb1.get(END)}")
    #     lb1.delete(0,END)
    pass

def all_left():
    pass


lbl1 = Label(root,text="List 1",font="comicsansms 15 bold")
lbl1.grid(row=0,column=2)

lbl2 = Label(root,text="List 2",font="comicsansms 15 bold")
lbl2.grid(row=0,column=4)

list1=["Ajp","Javascript","jsp"]
var1 = Variable(value=list1)

list2=[]
var2 = Variable(value=list2)

lb1 = Listbox(root,selectmode="all",listvariable=var1,font="Arial 10",fg="white",bg="black")
lb1.grid(row=1,rowspan=5,column=2)

lb2 = Listbox(root,selectmode="all",listvariable=var2,font="Arial 10",fg="white",bg="black")
lb2.grid(row=1,rowspan=5,column=4)

btn1 = Button(root,text=">",padx=5,bg="black",fg="red",command=right)
btn1.grid(row=1,column=3)

btn2 = Button(root,text="<",padx=5,bg="black",fg="red",command=left)
btn2.grid(row=2,column=3)

btn3 = Button(root,text=">>",padx=1,bg="black",fg="red",command=all_right)
btn3.grid(row=3,column=3)

btn4 = Button(root,text="<<",padx=1,bg="black",fg="red",command=all_left)
btn4.grid(row=4,column=3)

root.mainloop()