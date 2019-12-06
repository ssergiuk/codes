"""
FRONT END PART:
"""
import backend
from tkinter import *
def view_command(): #VIEW THE LIST
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():# SEARCH IN THE LIST
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():#INSERT SOMETHING IN THE LIST
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event): #get the list and input in entry box (works with list.bind function)
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def delete_command(): # DELETE FUNCTION WORKS WITH LIST.BIND FUNCTION WRITTEN DOWN HHERE
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


window = Tk()
window.wm_title("BookDB")

l1 = Label(window,text = "Title:")
l1.grid(row = 0,column = 0, pady = 6)

l2 = Label(window,text = "Author")
l2.grid(row = 0,column = 2)

l3 = Label(window,text = "Year")
l3.grid(row = 0,column = 4)

l4 = Label(window,text = "ISBN")
l4.grid(row = 0,column = 6)

l5 = Label(window,text = "")
l5.grid(row = 1, column = 0, pady = 7)

title_text = StringVar()
e1 = Entry(window,textvariable = title_text)
e1.grid(row = 0,column = 1)

author_text = StringVar()
e2 = Entry(window,textvariable = author_text)
e2.grid(row = 0,column = 3)

year_text = StringVar()
e3 = Entry(window,textvariable = year_text)
e3.grid(row = 0,column = 5)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)
e4.grid(row = 0,column = 7)



list1 = Listbox(window, heigh = 15, width = 150)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 8)
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 8, rowspan = 6)
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text = "View all", width = 15, command = view_command)
b1.place (relx = 0.04, rely = 0.12)

b2 = Button(window, text = "Search entry", width = 15, command = search_command)
b2.place (relx = 0.198, rely = 0.12)

b3 = Button(window, text = "Add entry", width = 15, command = insert_command)
b3.place (relx = 0.356, rely = 0.12)

b4 = Button(window, text = "Update", width = 15, command = update_command)
b4.place (relx = 0.514, rely = 0.12)

b5 = Button(window, text = "Delete", width = 15, command = delete_command)
b5.place (relx = 0.672, rely = 0.12)

b6 = Button(window, text = "Close", width = 15, command = window.destroy)
b6.place (relx = 0.83, rely = 0.12)

window.mainloop()
