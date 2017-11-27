"""
Database Application (Book Store)

Author: William
Date: 21/11/2017

https://github.com/williamsoftwarecode/python-projects

A program that stores book information in the following format:
Title, Author
Year, ISBN

Features include: 
    1. 
    
Additional Notes:

User can:
    1. View all records
    2. Search an entry
    3. Add entry
    4. Update entry
    5. Delete
    6. Close

"""


from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
        
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    backend.update(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

window=Tk()

l1=Label(window,text='Title')
l1.grid(row=0,column=0)
l2=Label(window,text='Author')
l2.grid(row=0,column=2)
l3=Label(window,text='Year')
l3.grid(row=1,column=0)
l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
isbn_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# Need to link listbox with vertical scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Add binding to Listbox (event type and function)
list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)
b1=Button(window,text="Search entry",width=12,command=search_command)
b1.grid(row=3,column=3)
b1=Button(window,text="Add entry",width=12,command=add_command)
b1.grid(row=4,column=3)
b1=Button(window,text="Update selected",width=12)
b1.grid(row=5,column=3)
b1=Button(window,text="Delete selected",width=12,command=delete_command)
b1.grid(row=6,column=3)
b1=Button(window,text="Close",width=12)
b1.grid(row=7,column=3)

window.mainloop()