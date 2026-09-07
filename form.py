from tkinter import *
from tkinter import font


window = Tk()
window.geometry("500x300")
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Segoe Script", size=90, weight=font.BOLD)


lab = Label(window, text="I'm Label")
lab.pack()

window.mainloop()