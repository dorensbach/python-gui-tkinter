# Seguindo tutorial do site:
# https://pythongeeks.org/gui-programming-in-python/

import tkinter.messagebox
from tkinter import *

win = Tk()
win.title('Bem-vindo!')
win.geometry('500x200')

def func():
    tkinter.messagebox.showinfo("Saudações", "Olá! Seja bem vindo!")

# can = Canvas(win, width=500, height=300)
# oval = can.create_oval(100, 100, 200, 180, fill='red')
# can.pack()

btn = Button(win, text="Ok", width=10, height=3, activebackground='#ffffff', command=func)
btn.place(x=200, y=30)

cb_var1 = IntVar()
cb1 = Checkbutton(win, text='Python', variable=cb_var1, onvalue=1, offvalue=0, height=2, width=10).grid(row=0, sticky=W)

cb_var2 = IntVar()
cb2 = Checkbutton(win, text='C++', variable=cb_var2, onvalue=1, offvalue=0, height=2, width=10).grid(row=1, sticky=W)

cb_var3 = IntVar()
cb3 = Checkbutton(win, text='Java', variable=cb_var3, onvalue=1, offvalue=0, height=2, width=10).grid(row=2, sticky=W)

win.mainloop()
