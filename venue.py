import tkinter
from tkinter import Place, Toplevel, ttk
from tkinter import CENTER, font
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def venuecall():

    venue=customtkinter.CTk()
    venue.title("VENUE")
    venue.iconbitmap("cricket2icon.ico")
    venue.geometry("850x675")

    test=tkinter.PhotoImage(file='1.png',master=venue)
    label1=tkinter.Label(venue,image=test)
    label1.place(x=25,y=0)

    test2=tkinter.PhotoImage(file='2.png',master=venue)
    label2=tkinter.Label(venue,image=test2)
    label2.place(x=25,y=335)

    test5=tkinter.PhotoImage(file='5.png',master=venue)
    label5=tkinter.Button(venue,image=test5)
    label5.place(x=830,y=334)

    test4=tkinter.PhotoImage(file='4.png',master=venue)
    label4=tkinter.Button(venue,image=test4)
    label4.place(x=830,y=0)

    test3=tkinter.PhotoImage(file='3.png',master=venue)
    label3=tkinter.Label(venue,image=test3)
    label3.place(x=25,y=666)



    venue.mainloop()
