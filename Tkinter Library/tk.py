from tkinter import *

window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,miles)

b1 = Button(window, text = "Start", command = km_to_miles)
b1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, heigh = 1, width = 20)
t1.grid(row = 0, column = 2 )
window.mainloop()


b3 = Button(window, text = "Add entry", width = 15)
b3.place (relx = 0.2, rely = 0.3, anchor = CENTER)
b4 = Button(window, text = "Update", width = 15)
b4.place (relx = 0.3, rely = 0.3, anchor = CENTER)
b5 = Button(window, text = "Delete", width = 15)
b5.place (relx = 0.4, rely = 0.3, anchor = CENTER)
b6 = Button(window, text = "Close", width = 15)
b6.place (relx = 0.5, rely = 0.3, anchor = CENTER)
