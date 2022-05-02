# Seguindo tutorial do site:
# https://pythongeeks.org/gui-programming-in-python/

from tkinter import *

win = Tk()
win.title('Bem-vindo!')
win.geometry('500x100')

Label(win, text='Nome').grid(row=0)
Label(win, text='Email').grid(row=1)

ent1 = Entry(win)
ent2 = Entry(win)

ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)

win.mainloop()
