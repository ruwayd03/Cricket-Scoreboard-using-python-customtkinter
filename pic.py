import tkinter

from PIL import Image, ImageTk
root=tkinter.Tk()
root.geometry("1130x640")

test=tkinter.PhotoImage(file='cricket2.png')
label1=tkinter.Button(image=test)
label1.place(x=5,y=5,height=100,width=100)
root.mainloop()