from tkinter import * # to import all libraries of tkinter.
# Tkinter Window
root = Tk()

# To change them title of GUI.
root.title("Label")

#GUI Logic here

# To change Height and Width { Format : Width x Height }
root.geometry("733x434")

# Max and Min Width and Height { Format : Width, Height}
root.minsize(300,150)
root.maxsize(1920,800)

#label {Syntax : Variable_name = Label(Attribute)}

# Here Label Attribute are 

# text - adds the text
# bg - background
# fg - foreground

# font - sets the font 
# syntax1 :- font=("Times New Roman",15,"bold")
# Syntax2 :- font="TimesNewRoman 15 italic"
# padx - x padding 
# pady - y padding
# relief - border Styling :- (SUNKEN, RAISED, GROOVE, RIDGE)

lbl = Label(text="PyCharm Community Edition",bg="Green",fg="white",padx=20,pady=20,font="TimesNewRoman 15 italic",borderwidth=2,relief=SUNKEN)
lbl1 = Label(text="Version 2017.2",fg="grey")
lbl2 = Label(text="Create new Project")
lbl3 = Label(text="Open")
lbl4 = Label(text="Check out from Version Control")

# Pack Attribute Options

# anchor = "nw,ne,sw,se" (nw-northwest,ne-northeast,sw-southwest,se-southest)
# side = TOP,BOTTOM,LEFT,RIGHT
# fill = X or Y (its like responsive)
# padx = x padding
# pady = y padding

lbl.pack(side=LEFT,fill=Y,padx=20,pady=20)
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()

root.mainloop()