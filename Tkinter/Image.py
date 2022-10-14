from tkinter import *
from PIL import Image,ImageTk # pillow Module imported

root = Tk()

root.title("Image")
root.geometry("1020x700")
root.minsize(400,200)
root.maxsize(1920,920)

#Image 

# note : Tkinter doesn't support jpg images, 
#        but using pillow module
#        [Write (pip install pillow) on console]
#        we can import jpg images.

# Normal Png Image

png_img = PhotoImage(file="D:\\Sem-2\\HTML\\Task\\16.png")
img_lbl = Label(image=png_img)
img_lbl.pack()

# Jpg Image using pillow module

jpg_img = Image.open("D:\\Sem-2\\HTML\\Task\\10.jpg")
bg_img = ImageTk.PhotoImage(jpg_img)
img_lbl2 = Label(image=bg_img)
img_lbl2.pack()

root.mainloop()