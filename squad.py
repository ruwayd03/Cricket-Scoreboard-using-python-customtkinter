import tkinter
from tkinter import Place, Toplevel, ttk
from tkinter import CENTER, font
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
def squadcall():
    
    def jumpIndia(self):
        india=customtkinter.CTkToplevel(squad)
        india.geometry("300x500")
        india.title("INDIA")
        india.iconbitmap("cricket2icon.ico")
        team1=customtkinter.CTkLabel(india,text='Rohit Sharma (c)\n\n KL Rahul\n\n Virat Kohli\n\n Suryakumar Yadav\n\n Deepak Hooda\n\n Rishabh Pant\n\n Dinesh Karthik\n\n Hardik Pandya\n\n R Ashwin\n\n Yuzvendra Chahal\n\n Axar Patel\n\n Bhuvneshwar Kumar\n\n Harshal Patel\n\n Arshdeep Singh\n\n Mohammad Shami')
        team1.place(x=80,y=10)
        india.mainloop()
    def jumpSouthAfrica(self):
        southafrica=customtkinter.CTkToplevel(squad)
        southafrica.geometry("300x500")
        southafrica.title("SOUTH AFRICA")
        southafrica.iconbitmap("cricket2icon.ico")
        team2=customtkinter.CTkLabel(southafrica,text='Temba Bavuma (c)\n\n Quinton de Kock\n\n Heinrich Klaasen\n\n Reeza Hendricks\n\n Keshav Maharaj\n\n Aiden Markram\n\n David Miller\n\n Lungi Ngidi\n\n Anrich Nortje\n\n Wayne Parnell\n\n Kagiso Rabada\n\n Rillee Rossouw\n\n Tabraiz Shamsi\n\n Tristan Stubbs\n\n Marco Jansen.')
        team2.place(x=80,y=10)
        southafrica.mainloop()
    def jumpBangladesh(self):
        bangladesh=customtkinter.CTkToplevel(squad)
        bangladesh.geometry("300x500")
        bangladesh.title("BANGLADESH")
        bangladesh.iconbitmap("cricket2icon.ico")
        team3=customtkinter.CTkLabel(bangladesh,text='Shakib Al  Hasan (c)\n\n Nurul Hasan\n\n Afif Hossain\n\n Ebadot Hossain\n\n Hasan Mahmud\n\n Litton Das\n\n Mehidy Hassan Miraz\n\n Mustafizur Rahman\n\n Najmul Hossain Shanto\n\n Shoriful Islam\n\n Soumya Sarkar\n\n Musaddek Hossain\n\n Nasum Ahmed\n\n Taskin Ahmed\n\n Yasir Ali Chowdhury')
        team3.place(x=80,y=10)
        bangladesh.mainloop()
    def jumpPakistan(self):
        pakistan=customtkinter.CTkToplevel(squad)
        pakistan.geometry("300x500")
        pakistan.title("PAKISTAN")
        pakistan.iconbitmap("cricket2icon.ico")
        team4=customtkinter.CTkLabel(pakistan,text='Babar Azam (c)\n\n Shadab Khan\n\n Asif Ali\n\n Fakhar Zaman\n\n Haider Ali\n\n Haris Rauf\n\n Iftikhar Ahmed\n\n Khushdil Shah\n\n Mohammad Hasnain\n\n Mohammad Nawaz\n\n Mohammad Rizwan\n\n Mohammad Wasim\n\n Naseem Shah\n\n Shaheen Shah Afridi\n\n Shan Masood')
        team4.place(x=80,y=10)
        pakistan.mainloop()
    def jumpZimbabwe(self):
        zimbabawe=customtkinter.CTkToplevel(squad)
        zimbabawe.geometry("300x500")
        zimbabawe.title("ZIMBABWE")
        zimbabawe.iconbitmap("cricket2icon.ico")
        team5=customtkinter.CTkLabel(zimbabawe,text='Craig Ervine (c)\n\n Ryan Burl\n\n Regis Chakabva\n\n Tendai Chatara\n\n Bradley Evans\n\n Luke Jongwe\n\n Clive Madande\n\n Wessly Madhevere\n\n Wellington Masakadza\n\n Tony Munyonga\n\n Blessing Muzarabani\n\n Richard Ngarava\n\n Sikandar Raza\n\n Milton Shumba\n\n Sean Williams')
        team5.place(x=80,y=10)
        zimbabawe.mainloop()
    def jumpNetherlands(self):
        netherlands=customtkinter.CTkToplevel(squad)
        netherlands.geometry("300x500")
        netherlands.title("NETHERLANDS")
        netherlands.iconbitmap("cricket2icon.ico")
        team6=customtkinter.CTkLabel(netherlands,text='Scott Edwards (c)\n\n Colin Ackermann\n\n Shariz Ahmad\n\n Logan van Beek\n\n Tom Cooper\n\n Brandon Glover\n\n Timm van der Gugten\n\n Fred Klaassen\n\n Bas de Leede\n\n Paul van Meekeren\n\n Roelof van der Merwe\n\n Stephan Myburgh\n\n Teja Nidamanuru\n\n Max O’Dowd\n\n Tim Pringle\n\n Vikram Singh')
        team6.place(x=80,y=10)
        netherlands.mainloop()
    #GROUP1

    def jumpNewzealand(self):
        newzealand=customtkinter.CTkToplevel(squad)
        newzealand.geometry("300x500")
        newzealand.title("NEW ZEALAND")
        newzealand.iconbitmap("cricket2icon.ico")
        team7=customtkinter.CTkLabel(newzealand,text='Kane Williamson (c)\n\n Tim Southee\n\n Ish Sodhi\n\n Mitchell Santner\n\n Glenn Phillips\n\n Jimmy Neesham\n\n Daryl Mitchell\n\n Adam Milne\n\n Martin Guptill\n\n Lachlan Ferguson\n\n Devon Conway\n\n Mark Chapman\n\n Michael Bracewell\n\n Trent Boult\n\n Finn Allen')
        team7.place(x=80,y=10)
        newzealand.mainloop()
    def jumpAustralia(self):
        australia=customtkinter.CTkToplevel(squad)
        australia.geometry("300x500")
        australia.title("AUSTRALIA")
        australia.iconbitmap("cricket2icon.ico")
        team8=customtkinter.CTkLabel(australia,text='Aaron Finch (c)\n\n Ashton Agar\n\n Pat Cummins\n\n Tim David\n\n Cameron Green\n\n Josh Hazlewood\n\n Mitchell Marsh\n\n Glenn Maxwell\n\n Kane Richardson\n\n Steven Smith\n\n Mitchell Starc\n\n Marcus Stoinis\n\n Matthew Wade\n\n David Warner\n\n Adam Zampa')
        team8.place(x=80,y=10)
        australia.mainloop()
    def jumpEngland(self):
        england=customtkinter.CTkToplevel(squad)
        england.geometry("300x500")
        england.title("ENGLAND")
        england.iconbitmap("cricket2icon.ico")
        team9=customtkinter.CTkLabel(england,text='Jos Buttler (c)\n\n Moeen Ali\n\n Harry Brook\n\n Sam Curran\n\n Chris Jordan\n\n Liam Livingstone\n\n Dawid Malan\n\n Adil Rashid\n\n Phil Salt\n\n Ben Stokes\n\n Tymal Mills\n\n David Willey\n\n Chris Woakes\n\n Mark Wood\n\n Alex Hales')
        team9.place(x=80,y=10)
        england.mainloop()
    def jumpIreland(self):
        ireland=customtkinter.CTkToplevel(squad)
        ireland.geometry("300x500")
        ireland.title("IRELAND")
        ireland.iconbitmap("cricket2icon.ico")
        team10=customtkinter.CTkLabel(ireland,text='Andrew Balbirnie (c)\n\n Mark Adair\n\n Curtis Campher\n\n Gareth Delany\n\n George Dockrell\n\n Stephen Doheny\n\n Fionn Hand\n\n Josh Little\n\n Barry McCarthy\n\n Conor Olphert\n\n Simi Singh\n\n Paul Stirling\n\n Harry Tector\n\n Lorcan Tucker\n\n Graham Hume')
        team10.place(x=80,y=10)
        ireland.mainloop()
    def jumpAfghanistan(self):
        afghanistan=customtkinter.CTkToplevel(squad)
        afghanistan.geometry("300x500")
        afghanistan.title("AFGHANISTAN")
        afghanistan.iconbitmap("cricket2icon.ico")
        team11=customtkinter.CTkLabel(afghanistan,text='Mohammad Nabi (c)\n\n Najibullah Zadran\n\n Rahmanullah Gurbaz\n\n Azmatullah Omarzai\n\n Darwish Rasooli\n\n Fareed Ahmad Malik\n\n Fazal Haq Farooqi\n\n Hazratullah Zazai\n\n Ibrahim Zadran\n\n Mujeeb ur Rahman\n\n Naveen ul Haq\n\n Qais Ahmad\n\n Rashid Khan\n\n Salim Safi\n\n Usman Ghani')
        team11.place(x=80,y=10)
        afghanistan.mainloop()
    def jumpSrilanka(self):
        srilanka=customtkinter.CTkToplevel(squad)
        srilanka.geometry("300x500")
        srilanka.title("SRILANKA")
        srilanka.iconbitmap("cricket2icon.ico")
        team12=customtkinter.CTkLabel(srilanka,text='Dasun Shanaka (c)\n\n Pathum Nissanka\n\n Kusal Mendis\n\n Charith Asalanka\n\n Bhanuka Rajapaksa\n\n Dhananjaya de Silva\n\n Wanindu Hasaranga\n\n Maheesh Theekshana\n\n Jeffrey Vandersay\n\n Chamika Karunaratne\n\n Kasun Rajitha\n\n Ashen Bandara\n\n Lahiru Kumara\n\n Binura Fernando\n\n Pramod Madushan')
        team12.place(x=80,y=10)
        srilanka.mainloop()




    squad=customtkinter.CTk()
    squad.title("TEAMS")
    squad.geometry("600x500")
    squad.iconbitmap("cricket2icon.ico")

    headinglabel=tkinter.Label(squad,text="T20 WORLD CUP TEAMS",fg="WHITE",bg="#212325",font=("Arial",32,"bold"))
    headinglabel.place(x=80,y=20)

    indialabel=tkinter.Label(squad,text="INDIA", cursor='hand2',fg="blue",bg="#212325",font=("Sans Serif",20))
    indialabel.place(x=100,y=150)
    indialabel.bind("<Button-1>",jumpIndia)

    southafricalabel=tkinter.Label(squad,text="SOUTH AFIRCA", cursor='hand2',fg="#00957b",bg="#212325",font=("Sans Serif",20))
    southafricalabel.place(x=100,y=250)
    southafricalabel.bind("<Button-1>",jumpSouthAfrica)

    pakistanlabel=tkinter.Label(squad,text="PAKISTAN", cursor='hand2',fg="#7bba3b",bg="#212325",font=("Sans Serif",20))
    pakistanlabel.place(x=100,y=350)
    pakistanlabel.bind("<Button-1>",jumpPakistan)

    bangladeshlabel=tkinter.Label(squad,text="BANGLADESH", cursor='hand2',fg="#029d52",bg="#212325",font=("Sans Serif",20))
    bangladeshlabel.place(x=100,y=450)
    bangladeshlabel.bind("<Button-1>",jumpBangladesh)

    zimbabwelabel=tkinter.Label(squad,text="ZIMBABWE", cursor='hand2',fg="#eb4f59",bg="#212325",font=("Sans Serif",20))
    zimbabwelabel.place(x=100,y=550)
    zimbabwelabel.bind("<Button-1>",jumpZimbabwe)

    netherlandslabel=tkinter.Label(squad,text="NETHERLANDS", cursor='hand2',fg="#fe733a",bg="#212325",font=("Sans Serif",20))
    netherlandslabel.place(x=100,y=650)
    netherlandslabel.bind("<Button-1>",jumpNetherlands)

    #GROUP1




    newzealandlabel=tkinter.Label(squad,text="NEW ZEALAND", cursor='hand2',fg="#8c8a85",bg="#212325",font=("Sans Serif",20))
    newzealandlabel.place(x=550,y=150)
    newzealandlabel.bind("<Button-1>",jumpNewzealand)

    englandlabel=tkinter.Label(squad,text="ENGLAND", cursor='hand2',fg="#d41c36",bg="#212325",font=("Sans Serif",20))
    englandlabel.place(x=550,y=250)
    englandlabel.bind("<Button-1>",jumpEngland)

    irelandlabel=tkinter.Label(squad,text="IRELAND", cursor='hand2',fg="#a1d668",bg="#212325",font=("Sans Serif",20))
    irelandlabel.place(x=550,y=350)
    irelandlabel.bind("<Button-1>",jumpIreland)

    australialabel=tkinter.Label(squad,text="AUSTRALIA", cursor='hand2',fg="#e0e74d",bg="#212325",font=("Sans Serif",20))
    australialabel.place(x=550,y=450)
    australialabel.bind("<Button-1>",jumpAustralia)

    srilankalabel=tkinter.Label(squad,text="SRILANKA", cursor='hand2',fg="#0b82c5",bg="#212325",font=("Sans Serif",20))
    srilankalabel.place(x=550,y=550)
    srilankalabel.bind("<Button-1>",jumpSrilanka)

    afghanistanlabel=tkinter.Label(squad,text="AFGHANISTAN", cursor='hand2',fg="#1636bc",bg="#212325",font=("Sans Serif",20))
    afghanistanlabel.place(x=550,y=650)
    afghanistanlabel.bind("<Button-1>",jumpAfghanistan)



    squad.mainloop()
