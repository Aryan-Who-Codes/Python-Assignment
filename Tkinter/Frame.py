from tkinter import *
root=Tk()
root.geometry("655x333")

#frame_1 = top frame
f1 = Frame(root, bg='grey',borderwidth = 8, relief = SUNKEN)
f1.pack(side =TOP,fill = "x")

l1 = Label(f1, text="welcome to Aryan's Editor",font="bold 12",relief=SUNKEN)
l1.pack()

#frame_2  = right frame

f2 = Frame(root, bg = "grey", borderwidth = 7, relief = SUNKEN)
f2.pack(side = LEFT,fill=  "y")

l2 = Label(f2 , text="""
NEW_FILE
OPEN
SAVE
EDIT
FONT
BOLD
UNDERLINE
INSERT_TABLES
INSERT_PICTURE
EXIT
""")
l2.pack(pady=50)



root.mainloop()