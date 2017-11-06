"""
Interactive Dictionary 

Author: William
Date: 06/11/2017

This application is a Python based interactive dictionary with a JSON database. 
Features include: 
    1. A search from a database for word definitions 
    2. Suggest similar words for inputs which do no exist in the database
    
Additional Notes:
    1. JSON is a data format with key-value pairs. 
"""



import json

# Loading the json database into a Python dictionary
data = json.load(open("data.json", 'r'))


# Looks up and returns word definition from the database
def search(word):
    # Accounting for inputs which do not match the database
    if word in data: 
        return data[word]
    else: 
        return "The word doesn't exist. Please double check it."
    
    
word = input("Enter a word: ")
# Making the search case insensitive, lowercase for all searches
print(search(word.lower()))
