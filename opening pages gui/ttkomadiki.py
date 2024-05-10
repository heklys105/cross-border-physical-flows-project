import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox

def appopen():
    #window setup
    window=ttk.Window(title="Cross-Border Physical Flow (GR)",themename="sandstone",)
    window.geometry("900x600")
    window.resizable(False,False)
    window.iconbitmap("12443898.ico")
    #title and choose period labels
    title = ttk.Label(window, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window, text="Choose time period:",font=("Helvetica",14), bootstyle="dark")
    labelperiod.pack(side="top",pady=(30,40))

    #buttons placement
    b1 = ttk.Button(window,text= "Choose Date",bootstyle="outline-dark",width=20,command=opendate)
    b1.pack(side="top")

    b1 = ttk.Button(window,text= "Choose Month",bootstyle="outline-dark",width=20,command=openmonth)
    b1.pack(side="top",pady=25)

    b1 = ttk.Button(window,text= "Choose Year",bootstyle="outline-dark",width=20,command=openyear)
    b1.pack(side="top")
    window.mainloop()

def opendate():
    #window setup
    window3=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window3.geometry("900x600")
    window3.resizable(False,False)
    window3.iconbitmap("12443898.ico")
    #title and choose period labels
    title = ttk.Label(window3, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window3, text="Choose Date:",font=("Helvetica",14), bootstyle="dark")
    labelperiod.pack(side="top",pady=40)

    #buttons placement
    dateentry=ttk.DateEntry(window3,bootstyle="Dark")
    dateentry.pack()
    
    def confirmyear():#checking for year input
        datechose=dateentry.entry.get()
        chosenyear=int(datechose[len(datechose)-4:len(datechose)-1])
        if chosenyear<2022 or  chosenyear>2024:
            messagebox.showerror("Error","Please enter a valid year (2022-2024)")

    
    #opens window for statistics
    def openstatistics():
        #checking if the user has entered a right date
        confirmyear()
        

    labelperiod = ttk.Label(window3, text="*(2022-2024)",font=("Helvetica",11), bootstyle="dark")
    labelperiod.pack(side="top",pady=5)

    bconfirm = ttk.Button(window3,text= "Confirm Date",bootstyle="outline-dark",width=20,command=openstatistics)
    bconfirm.pack(side="top",pady=20)

    window3.mainloop()

def openmonth():
    #window setup
    window2=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window2.geometry("900x600")
    window2.resizable(False,False)
    window2.iconbitmap("12443898.ico")

    #title and choose period labels
    title = ttk.Label(window2, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window2, text="Choose Month:",font=("Helvetica",14), bootstyle="dark")
    labelperiod.pack(side="top",pady=40)

    listmonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    combobox=ttk.Combobox(window2,bootstyle="Dark",values=listmonths,state="readonly")
    combobox.set("Choose month")
    combobox.pack()

    listyears = [
        "2022",
        "2023",
        "2024"
    ]

    combobox=ttk.Combobox(window2,bootstyle="Dark",values=listyears,state="readonly")
    combobox.set("Choose year")
    combobox.pack(pady=10)

    bconfirm = ttk.Button(window2,text= "Confirm Month",bootstyle="outline-dark",width=20)
    bconfirm.pack(side="top",pady=20)

    window2.mainloop()


def openyear():
    #window setup
    window1=ttk.Toplevel(title="Cross-Border Physical Flow (GR)")
    window1.geometry("900x600")
    window1.resizable(False,False)
    window1.iconbitmap("12443898.ico")
    #title and choose period labels
    title = ttk.Label(window1, text="Cross-Border Physical Flow (Greece)",font=("Helvetica",15), bootstyle="inverse-light")
    title.pack(side="top",pady=40)
    labelperiod = ttk.Label(window1, text="Choose Year:",font=("Helvetica",14), bootstyle="dark")
    labelperiod.pack(side="top",pady=30)

    
    listyears = [
        "2022",
        "2023",
        "2024"
    ]

    combobox=ttk.Combobox(window1,bootstyle="Dark",values=listyears,state="readonly")
    combobox.set("Choose year")
    combobox.pack()

    bconfirm = ttk.Button(window1,text= "Confirm year",bootstyle="outline-dark",width=20)
    bconfirm.pack(side="top",pady=20)

    window1.mainloop()

appopen()