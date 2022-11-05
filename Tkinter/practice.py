# from email import message
# from tkinter import *
# from tkinter import messagebox

# root=Tk()
# root.geometry("300x150")
# root.title("practice")

# def fun():
#     messagebox.showinfo("Hello","Red Button Clicked")

# def fun2():
#     messagebox.showinfo("Hello","Blue Button Clicked")

# def fun3():
#     messagebox.showinfo("Hello","Green Button Clicked")

# def fun4():
#     messagebox.showinfo("Hello","Yellow Button Clicked")


# b1= Button(root,text="red",command=fun,activeforeground="red",activebackground="pink",pady=10)
# b2=Button(root,text="blue",command=fun2,activeforeground="blue",activebackground="lightblue",pady=10)
# b3= Button(root,text="green",command=fun3,activeforeground="green",activebackground="lightgreen",pady=10)
# b4=Button(root,text="yellow",command=fun4,activeforeground="orange",activebackground="lightyellow",pady=10)

# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)
# root.mainloop()

#---------------------------------------------------------------------------------------------------

# # Python Code for Dance Academy Form
# from tkinter import*

# root = Tk()
# root.geometry("655x333")

# form = Label(root,text= "Dance Academy Form ",font="comicssanms 16 bold")
# form.grid(column=2)

# n= Label(root,text= "\n")
# n.grid(column=2)

# name = Label(root,text = "Name :  ")                            # Lable of NAME
# name.grid()

# namevalue = StringVar()                                         # defining entry var 
# name_entry = Entry(root, textvariable = namevalue)              # Entry Var
# name_entry.grid(column = 1  , row = 2 )                         # Adding it in Grid

# age = Label(root,text = "Age : ")                               # Label of Age 
# age.grid()

# age_value = StringVar()
# age_Entry = Entry(root, textvariable = age_value  )
# age_Entry.grid(column = 1 , row = 3  )

# contact = Label(root,text = "Contact No. : ")                              
# contact.grid()

# contact_value = StringVar()
# contact_Entry = Entry(root, textvariable = contact_value  )
# contact_Entry.grid(column = 1 , row = 4  )

# mail = Label(root,text = "E-Mail Adress  : ")                              
# mail.grid()

# mail_value = StringVar()
# mail_Entry = Entry(root, textvariable = mail_value  )
# mail_Entry.grid(column = 1 , row = 5  )

# xp = Label(root,text = "Any Prior Experience  : ")                              
# xp.grid()

# xp_value = StringVar()
# xp_Entry = Entry(root, textvariable = xp_value  )
# xp_Entry.grid(column = 1 , row = 6  )

# def Submit():
#     print(f"{namevalue.get()}")
#     print(f"{age_value.get()}")
#     print(f"{contact_value.get()}")
#     print(f"{mail_value.get()}")
#     print(f"{xp_value.get()}")
#     f = open("form_1.txt","a")  
#     f.truncate(0)
#     f.write(f"{namevalue.get()}")
#     f.write('\n')
#     f.write(f"{age_value.get()}")
#     f.write('\n')
#     f.write(f"{contact_value.get()}")
#     f.write('\n')
#     f.write(f"{mail_value.get()}")
#     f.write('\n')
#     f.write(f"{xp_value.get()}")
#     f.write('\n')

# submit_l1 = Label(root,text="\n")
# submit_l1.grid( row = 8 )

# submit_button = Button(root,text="SUBMIT", command = Submit)
# submit_button.grid( row = 8 )

# root.mainloop()

#---------------------------------------------------------------------------------------------------

from tkinter import *

root= Tk()

root.geometry("655x333")
root.title("Form")

def submit():
    print(f"Name : {namevalue.get()}")
    print(f"Password : {passvalue.get()}")
    print(f"Email : {emailvalue.get()}")
    print(f"Gender : {gendervalue.get()}")
    print(f"Contact : {contactvalue.get()}")
    with open("form.txt", "a") as f:
        f.truncate(0)
        f.write(f"Name : {namevalue.get()}\n")
        f.write(f"Password : {passvalue.get()}\n")
        f.write(f"Email : {emailvalue.get()}\n")
        f.write(f"Gender : {gendervalue.get()}\n")
        f.write(f"Contact : {contactvalue.get()}\n")
                  
f1= Frame(root,bg="black")
f1.grid()

l1 = Label(f1,text="Register Form",font="comicsansms 15 bold",pady=15,bg="black",fg="red",padx=20)
l1.grid(row=0,column =3,columnspan=2)

#1
name = Label(f1,text="Name",bg="black",fg="red",pady=10)
name.grid(row=1,column =2)

namevalue= StringVar()
nameentry = Entry(f1,textvariable=namevalue)
nameentry.grid(row=1,column =3)

#2
password = Label(f1,text="Password",bg="black",fg="red",pady=10)
password.grid(row=2,column =2)

passvalue= StringVar()
passentry = Entry(f1,textvariable=passvalue)
passentry.grid(row=2,column =3)

#3
email = Label(f1,text="Email",bg="black",fg="red",pady=10)
email.grid(row=3,column =2)

emailvalue= StringVar()
emailentry = Entry(f1,textvariable=emailvalue)
emailentry.grid(row=3,column =3)

#4
gender = Label(f1,text="Gender",bg="black",fg="red",pady=10)
gender.grid(row=4,column =2)

gendervalue= StringVar()
genderentry = Entry(f1,textvariable=gendervalue)
genderentry.grid(row=4,column =3)

#4
contact = Label(f1,text="Contact",bg="black",fg="red",pady=10)
contact.grid(row=5,column =2)

contactvalue= StringVar()
contactentry = Entry(f1,textvariable=contactvalue)
contactentry.grid(row=5,column =3)

#5

Button(f1,text="Submit",command=submit,bg="black",fg="red",borderwidth=4,relief=SUNKEN).grid(row=6,column =3)

root.mainloop()