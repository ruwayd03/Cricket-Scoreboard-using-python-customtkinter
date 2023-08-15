import tkinter
from tkinter import Place, Toplevel, ttk
from tkinter import CENTER, font
from PIL import ImageTk, Image
import customtkinter
import mysql.connector
from sqlalchemy import create_engine
import webview
from squad import *
from fixtures import *
from venue import *


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def livescore():
    webview.create_window('Live Score', 'https://www.espncricinfo.com/live-cricket-score')
    webview.start()



def show1():
    mysqldb=mysql.connector.connect(host='localhost',user='root',password='1234',database='cricket')
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT Teams,Played,Wins,Lost,NRR,Points FROM group3")
    records=mycursor.fetchall()
    
    
    for i,(Teams,Played,Wins,Lost,NRR,Points) in enumerate(records,start=1):
        listbox1.insert("","end",values=(Teams,Played,Wins,Lost,NRR,Points))
        mysqldb.close()

def show2():
    mysqldb=mysql.connector.connect(host='localhost',user='root',password='1234',database='cricket')
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT Teams,Played,Wins,Lost,NRR,Points FROM group4")
    records=mycursor.fetchall()
    
    
    for i,(Teams,Played,Wins,Lost,NRR,Points) in enumerate(records,start=1):
        listbox2.insert("","end",values=(Teams,Played,Wins,Lost,NRR,Points))
        mysqldb.close()


def jumpvenue():
    venuecall()

def jumpteam():
    squadcall()

def jumpfixture():
    fixturecall()

window = customtkinter.CTk()            #main window
window.geometry("860x640")
window.iconbitmap("cricket2icon.ico")
window.title("ICC T20 WORLD CUP")

logo1=Image.open('Logo.png')
logo2=logo1.resize((100,100))
logo3=ImageTk.PhotoImage(logo2,master=window)
 
logolabel=tkinter.Label(master=window,image=logo3)
logolabel.place(x=350,y=10)

# to change the color of treeview / table
style=ttk.Style()
style.theme_use('default')

style.configure("Treeview",background="#1e1e1e",foreground="white",rowheight=21,fieldbackground="#1e1e1e")
style.configure("Treeview.Heading",background="#212325",foreground="white")

#to change the color after selecting on a row
style.map('Treeview',background=[('selected',"#005e48")])
style.map('Treeview.Heading',background=[('selected',"#000000")])


heading1= customtkinter.CTkLabel(window,text="ICC T20 WORLD CUP",text_font=("<Sans Serif>",20))
heading1.place(x=310,y=10)

pointslabel1= customtkinter.CTkLabel(window,text="POINTS TABLE",text_font=("<Sans Serif>",16))
pointslabel1.place(x=350,y=110)

pointslabel2= customtkinter.CTkLabel(window,text="GROUP 1",text_font=("<Sans Serif>",12))
pointslabel2.place(x=20,y=145)

pointslabel3= customtkinter.CTkLabel(window,text="GROUP 2",text_font=("<Sans Serif>",12))
pointslabel3.place(x=20,y=340)

livebutton = customtkinter.CTkButton(window, text="LIVE SCORE", width=800,height=35,fg_color=("#009270"),hover_color=("#005e48"),command=livescore)  
livebutton.place(x=35,y=535) 

fixturebutton = customtkinter.CTkButton(window, text="FIXTURES", width=245,height=35,fg_color=("#009270"),hover_color=("#005e48"),command=jumpfixture)
fixturebutton.place(x=35,y=585)

venuebutton = customtkinter.CTkButton(window, text="VENUE", width=245,height=35,fg_color=("#009270"),hover_color=("#005e48"),command=jumpvenue)
venuebutton.place(x=315,y=585)

teambutton = customtkinter.CTkButton(window, text="TEAMS", width=245,height=35,fg_color=("#009270"),hover_color=("#005e48"),command=jumpteam)
teambutton.place(x=592,y=585)

cols=("Teams","Played","Wins","Lost","NRR","Points")
listbox1=ttk.Treeview(window,columns=cols,show='headings')
listbox2=ttk.Treeview(window,columns=cols,show='headings')





for col in cols:
    listbox1.heading(col,text=col)
    listbox1.place(x=50,y=260)
    listbox2.heading(col,text=col)
    listbox2.place(x=50,y=550)

show1()
show2()
window.mainloop()
