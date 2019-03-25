from tkinter import *
main = Tk() 
main.title('Counting Seconds') 

var1 = IntVar() 
c1 = Checkbutton(main, text='male', variable=var1)
c1.grid(row=0, sticky=W) 
c1.var = var1

var2 = IntVar() 
c2 = Checkbutton(main, text='female', variable=var2)
c2.grid(row=1, sticky=W)
c2.var = var2
def fetch_value():
    print(c1.var)
    print(c2.var)

Button(main, text='Submit', width=25, command=fetch_value).grid(row=2, column=2) 


main.mainloop() 