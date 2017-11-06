"""
Interactive Dictionary 

Author: William
Date: 06/11/2017

This application is a Python based interactive dictionary with a JSON database. 
Features include: 
    1. A search from a database for word definitions 
    2. Suggest similar words
    
Additional Notes:
    1. JSON is a data format with key-value pairs. 
"""

import json

# Import the json database into a Python dictionary
data = json.load(open("data.json", 'r'))

search_key = input("Enter a word: ")
print(data[search_key])