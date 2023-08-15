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
def jump2(self):
    signup.destroy()
    import login1

#function for clearing the enteries
def clear():
    name1.delete(0,customtkinter.END)
    email_2.delete(0,customtkinter.END)
    password_2.delete(0,customtkinter.END)

#database connectivity
def connect_database():
    if name1.get()==''or email_2.get()==''or password_2.get()=='':
        messagebox.showerror('Error','All Fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue Please Try Again')
            return
        
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, name varchar(100), email varchar(50),  password varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query='select * from data where email =%s'
        mycursor.execute(query,(email_2.get()))
        row=mycursor.fetchone()
        
        if row != None:
            messagebox.showerror('Error','Email Already Exists')
        
        else:
            query='insert into data(name,email,password) values(%s,%s,%s)'
            mycursor.execute(query,(name1.get(),email_2.get(),password_2.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful')
            clear()
            signup.destroy() 
            import login1
           
        



#signupwindow
signup = customtkinter.CTk()            

#title
signup.title("SignUp")

# Geometry
signup.geometry("390x440")

signup.iconbitmap("cricket2icon.ico")

login2=customtkinter.CTkLabel(signup,text="SIGN UP",text_font=("San serif",25))
login2.place(x=135,y=75)
    
name1=customtkinter.CTkEntry(signup,height=35,width=300,placeholder_text="Name")
name1.place(x=50,y=175)
    
    
email_2=customtkinter.CTkEntry(signup,height=35,width=300,placeholder_text="Email")
email_2.place(x=50,y=225)
    
   
password_2=customtkinter.CTkEntry(signup,height=35,width=300,show="*",placeholder_text="Password")
password_2.place(x=50,y=275)
    
button2 = customtkinter.CTkButton(signup, text="SignUp", width=300,fg_color=("#214ae1"),hover_color=("#1c3ebb"),command=connect_database)   # signup button
button2.place(x=50,y=325)  

login2=customtkinter.CTkLabel(text="Already have an account?,")
login2.place(x=50,y=375)
login3=tkinter.Label(text="Click here",cursor="hand2",fg="lightblue",bg="#212325") 
login3.bind("<Button-1>",jump2)      #for opening the login window.
login3.place(x=292,y=568)

signup.mainloop()