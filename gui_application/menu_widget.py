from tkinter import *

master = Tk() 
master.geometry("500x500")

menu = Menu(master)
master.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=master.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


mainloop()