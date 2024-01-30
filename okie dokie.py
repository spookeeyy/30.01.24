from tkinter import *


raam = Tk()
raam.title("Tühi tahvel")
# raam.attributes('-fullscreen', True)
tahvel = Canvas(raam, width=600, height =400, background="darkcyan")

# jooned

tahvel.create_line(50,50,100,50) # horisontaaljoon

tahvel.create_line(50,150,100,150,100,200) # horisontaal koos vertikaaljoonega

tahvel.create_line(50,100,100,250, width=4) # kaldjoon mis on PHAT

tahvel.create_line(350,50,350,100, width=4, fill="white", arrow=LAST) # valge nool

# ristkülik

tahvel.create_rectangle(150,50,200,100) # tühi must ruut

tahvel.create_rectangle(150,150,200,200, width=2, outline="yellow") # kollane tühi ruut

tahvel.create_rectangle(150,250,200,300, fill="white") # seest valge ruut

# hulknurk

tahvel.create_polygon(150,350,150,400,200,375, fill="red", outline="black")

# ovaal

tahvel.create_oval(10,10,100,100, fill="red", outline="green")

# tekst

tahvel.create_text(50,50, text="Tere!")

tahvel.create_text(50,50, text="Tere!", anchor = CENTER, fill="cyan")



tahvel.pack()



raam.mainloop()