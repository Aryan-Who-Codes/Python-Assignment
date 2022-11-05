# 1. Reverse a String.

# from tkinter import *

# root = Tk()

# root.geometry("400x200")
# root.title("Q1")

# heading =Label(text="Reverse a String",font="Comicsansms 15 bold")
# heading.grid(row=0,column=1,padx=10)

# gap=Label()
# gap.grid(row=1,column=1)

# Lbl = Label(text="Enter a word : ",font="comicsansms 10 bold")
# Lbl.grid(row=2,column=1)

# txtvalue=StringVar()

# txt=Entry(textvariable=txtvalue,font="comicsansms 10 bold")
# txt.grid(row=2,column=2)

# def reverse():
#     answer = Label(text=f"{txtvalue.get()}"[::-1],font="comicsansms 10 bold")
#     answer.grid(row=3,column=2,pady=5)

# btn = Button(text="Validate",width="15",command=reverse)
# btn.grid(row=4,column=2,pady=10)
# root.mainloop()

# ------------------------------------------------------------------------------


# 2. Sum of integers.

# from tkinter import *

# root = Tk()

# root.geometry("400x200")
# root.title("Q2")

# heading =Label(text="Sum of integers",font="Comicsansms 15 bold")
# heading.grid(row=0,column=1,padx=10)

# gap=Label()
# gap.grid(row=1,column=1)

# Lbl = Label(text="Enter value of integer N : ",font="comicsansms 10 bold")
# Lbl.grid(row=2,column=1,padx=10)

# entryvalue=IntVar()

# txt=Entry(textvariable=entryvalue,font="comicsansms 10 bold")
# txt.grid(row=2,column=2)

# def reverse():
#     sum=0
#     num = entryvalue.get()
    
#     # while(num):
#     #     sum+=num
#     #     num-=1
    
#     sum=int((num*(num+1))/2)
    
#     answer = Label(text=f"The sum is 1+2+3+..+{entryvalue.get()}={sum}",font="comicsansms 10 bold")
#     answer.grid(row=3,column=2,pady=5)

# btn = Button(text="Validate",width="15",command=reverse)
# btn.grid(row=4,column=2,pady=10)

# root.mainloop()

# -----------------------------------------------------------------------------

# 3. GUI

# from tkinter import *

# root = Tk()

# root.geometry("250x200")
# root.title("GUI practice")

# radiovalue=IntVar()

# R1 = Radiobutton(text="male",variable=radiovalue,value=1,state=NORMAL)
# R1.grid(row=0,column=0,padx=20,pady=10)
# R2 = Radiobutton(text="female",variable=radiovalue,value=2,state=NORMAL)
# R2.grid(row=0,column=1)

# checkvalue1=IntVar()
# checkvalue2=IntVar()

# C1 = Checkbutton(text="Cricket",variable=checkvalue1)
# C1.grid(row=2,column =0,padx=20,pady=10)
# C2 = Checkbutton(text="Tennis",onvalue=0,offvalue=1,variable=checkvalue2)
# C2.grid(row=2,column =1)

# options=["one","two","three","four"]

# Optionvalue = StringVar()
# Optionvalue.set("select")

# dropdown = OptionMenu(root,Optionvalue,*options)
# dropdown.grid(row=3,column =0)

# l_list = ["one","two","three","four"]
# var = Variable(value=l_list)

# list = Listbox(root,listvariable=var,selectmode=ALL,height=5)
# list.grid(row=3,column =1)

# root.mainloop()

# -------------------------------------------------------------------------------

# 4 temperature Converter.

from functools import partial
from tkinter import *
from tkinter import messagebox

temp_val = "Celsius"

def store_temp(set_temp):
    global temp_val
    temp_val = set_temp
    
def call_convert(rlabel1, inputn):
    temp = inputn.get()
    
    if temp_val == "Celsius":
        
        f = float((float(temp)*9/5)+32)
        rlabel1.config(text="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Fahrenheit")
        
    if temp_val=="Fahrenheit":
        
        c= float((float(temp)-32)*5/9)
        rlabel1.config(text="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Celsius")
        
    return

root = Tk()

root.geometry("300x150+600+200")
root.title("Temperature Converter")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

inputNumber = StringVar()
var = StringVar()

input_label = Label(root,text = "Enter Temperature")
input_entry = Entry(root,textvariable = inputNumber)

input_label.grid(row=1)
input_entry.grid(row=1,column=1)

result_label = Label(root)
result_label.grid(row=3,columnspan=4)

dropdownlist = ["Celsius","Fahrenheit"]

drop_down = OptionMenu(root,var, *dropdownlist,command=store_temp)
var.set(dropdownlist[0])
drop_down.grid(row=1,column=2)

call_convert = partial(call_convert,result_label,inputNumber)

result_button = Button(root,text ="Convert",command=call_convert)
result_button.grid(row=2,columnspan=2)

root.mainloop()