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


def view_command():
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

title=StringVar()
author=StringVar()
year=StringVar()
isbn=StringVar()
e1=Entry(window,textvariable=title)
e1.grid(row=0,column=1)
e2=Entry(window,textvariable=author)
e2.grid(row=0,column=3)
e3=Entry(window,textvariable=year)
e3.grid(row=1,column=1)
e4=Entry(window,textvariable=isbn)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)
b1=Button(window,text="Search entry",width=12)
b1.grid(row=3,column=3)
b1=Button(window,text="Add entry",width=12)
b1.grid(row=4,column=3)
b1=Button(window,text="Update",width=12)
b1.grid(row=5,column=3)
b1=Button(window,text="Delete",width=12)
b1.grid(row=6,column=3)
b1=Button(window,text="Close",width=12)
b1.grid(row=7,column=3)

window.mainloop()