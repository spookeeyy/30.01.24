from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = "Tere, " + nimi.get()
    messagebox.showinfo(message=tervitus)
    
    
raam = Tk()
raam.title("Tervitaja")
raam.geometry("300x300")

silt = ttk.Label(raam, text="Nimi")
silt.place(x=5, y=5,)

nimi = ttk.Entry(raam)
nimi.place(x=70, y=5, width=150)

nupp = ttk.Button(raam, text="Tervita!", command=tervita)
nupp.place(x=70, y=40, width=150)

raam.mainloop()

