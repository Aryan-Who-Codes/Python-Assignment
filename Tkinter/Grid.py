from tkinter import *

root = Tk()

root.geometry("655x333")

def getvals():
    print (f"The value of username is {userValue.get()}")
    print (f"The value of password is {passValue.get()}")
    f=open("Form.txt", "a")
    f.truncate(0)
    f.write(f"{userValue.get()}")
    f.write(f"\n")
    f.write(f"{passValue.get()}")
    f.write(f"\n")
    
user = Label(root, text="Username")
Password = Label(root, text="Password")

user.grid()
Password.grid(row=1)

# Variable classes in Tkinter.

# BooleanVar,StringVar,IntVar,DoubleVar

userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable= userValue)
passEntry = Entry(root, textvariable= passValue)

userEntry.grid(row=0,column=1)
passEntry.grid(row=1,column=1)

Button(root, text="Submit",command=getvals).grid()

root.mainloop()