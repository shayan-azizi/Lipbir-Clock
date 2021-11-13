from tkinter import *
from tkinter.ttk import *
from time import strftime

def time ():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)


root = Tk()
root.title("Lipbir - Clock")

label = Label(root, font = ("DS-Digital", 80), background = "black", foreground = "green" )
label.pack(anchor = "center",)
time()


mainloop()