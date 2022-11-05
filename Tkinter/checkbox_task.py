from tkinter import *
from unittest import result

root = Tk()

root.geometry("655x333")
root.title("Check_task")

menu_items = {"icecream - 20 Rs.": 20,"juice - 50 Rs.":50,"breakfast - 300 Rs.":300,"lunch - 300 Rs.":300,"dinner - 500 Rs.":500}
selected = {}

def Calculate():
    bill =0
    for item in menu_items:
        if selected[item].get():
            bill += menu_items[item]
        
    results.delete(1.0,END)
    results.insert(END,"Total Cost : "+str(bill))
    
for item in menu_items:
    var_select = BooleanVar()
    button = Checkbutton(root, text=item, variable=var_select)
    button.grid(sticky="w")
    selected[item] = var_select
    
Calc_but = Button(root,text="Calculate",command=Calculate)
Calc_but.grid()
    
results = Text(root,width=20,height=4,wrap=WORD)
results.grid(columnspan=2)
    
    
# F1 = Frame(root, bg="Cornflower blue",borderwidth = 8, relief = SUNKEN)
# F1.pack()

# Lb1 = Label(F1,text="Menu List",font="Courier 15 bold",fg="white",bg="Cornflower blue",padx=5,pady=5)
# Lb1.pack()

# opt1value= IntVar()
# opt2value= IntVar()
# opt3value= IntVar()
# opt4value= IntVar()


# opt1 = Checkbutton(F1,text="Menu",font="Courier 10 bold",fg="black",bg="Cornflower blue",variable=opt1value)
# opt1.pack()
# opt2 = Checkbutton(F1,text="Menu",font="Courier 10 bold",fg="black",bg="Cornflower blue",variable=opt2value)
# opt2.pack()
# opt3 = Checkbutton(F1,text="Menu",font="Courier 10 bold",fg="black",bg="Cornflower blue",variable=opt3value)
# opt3.pack()
# opt4 = Checkbutton(F1,text="Menu",font="Courier 10 bold",fg="black",bg="Cornflower blue",variable=opt4value)
# opt4.pack()




root.mainloop()