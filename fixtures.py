import tkinter
from tkinter import Place, Toplevel, ttk
from tkinter import CENTER, font
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def fixturecall ():

    fixture=customtkinter.CTk()
    fixture.title("FIXTURES")
    fixture.geometry("850x600")
    fixture.iconbitmap("cricket2icon.ico")

    fixturesheading=tkinter.Label(master=fixture,text="FIXTURES",fg="white",bg="#212325",font=("Arial",32,"bold"))
    fixturesheading.place(x=500,y=30)

    fix1=Image.open('group1.jpg')
    fix2=fix1.resize((600,650))
    fix3=ImageTk.PhotoImage(fix2,master=fixture)

    fixlabel1=tkinter.Label(master=fixture,image=fix3)
    fixlabel1.place(x=635,y=150)

    fix4=Image.open('group2.jpg')
    fix5=fix4.resize((600,650))
    fix6=ImageTk.PhotoImage(fix5,master=fixture)

    fixlabel2=tkinter.Label(master=fixture,image=fix6)
    fixlabel2.place(x=35,y=150)




    fixture.mainloop()