from tkinter import *

master = Tk() 
master.geometry("500x300")
 

Label(master, text='First Name').grid(row=0) 
e1 = Entry(master)
grid(row=0, column=1) 

Label(master, text='Last Name').grid(row=1) 
e2 = Entry(master)
e2.grid(row=1, column=1) 

def fetch_value():
    print(e1.get())
    print(e2.get())

Button(master, text='Submit', width=25, command=fetch_value).grid(row=2, column=2)


mainloop()