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

import sqlite3
from tkinter import *

window=Tk()

b1=Button(window,text="View All")
b1.grid(row=,column=)