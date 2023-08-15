import tkinter
from tkinter import Place, Toplevel, ttk
from tkinter import CENTER, font
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import pymysql
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    
#function for click here binding
def jump(self):
    root.destroy()
    import signup


def login_user():
    if email.get()==''or password.get()=='':
        messagebox.showerror('Error','All Fields are required')
    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue Please Try Again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where email=%s and password=%s'
        mycursor.execute(query,(email.get(),password.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid Email or Password')
        else:
            root.destroy()
            import mainwindow


root = customtkinter.CTk()            #main window
root.geometry("390x440")
root.title("Login")
root.iconbitmap("cricket2icon.ico")


loginlabel=customtkinter.CTkLabel(root,text="LOGIN",text_font=("San serif",25))
loginlabel.place(x=130,y=75)


email=customtkinter.CTkEntry(height=35,width=300,placeholder_text="Email")
email.place(x=50,y=200)

password=customtkinter.CTkEntry(height=35,width=300,show='*',placeholder_text="Password")
password.place(x=50,y=250)

loginbutton = customtkinter.CTkButton(root, text="Login",fg_color=("#ff0000"),hover_color=("#bf0000"), width=300,command=login_user)      #login button
loginbutton.place(x=50,y=325)

sign_up2=customtkinter.CTkLabel(text="Don't have an account?,")
sign_up2.place(x=50,y=375)
sign_up3=tkinter.Label(text="Click here",cursor="hand2",fg="lightblue",bg="#212325") 
sign_up3.bind("<Button-1>",jump)      #for opening the second window(signup).
sign_up3.place(x=280,y=568)


root.mainloop()



