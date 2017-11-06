"""
Interactive Dictionary 

Author: William
Date: 06/11/2017

https://github.com/williamsoftwarecode/python-projects

This application is a Python based interactive dictionary with a JSON database. 
Features include: 
    1. A search from a database for word definitions 
    2. Suggest similar words for inputs which do no exist in the database
    
Additional Notes:
    1. JSON is a data format with key-value pairs. 
    2. Use difflib get_close_matches to compare input and word similarities
    3. Libraries can be found on https://docs.python.org/3/library/index.html
    4. "dictionary".keys() and "dictionary".values()
"""



import json
import difflib                          # Library to compare text
from difflib import SequenceMatcher     # Used to calculate similarity ratio
from difflib import get_close_matches


# Loading the json database into a Python dictionary
data = json.load(open("data.json", 'r'))
keys = data.keys()

# Looks up and returns word definition from the database
def search(word):
    # Accounting for inputs which do not match the database
    if word in data: 
        return data[word]
    elif len(get_close_matches(word, keys, cutoff=0.8)) > 0 :
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, keys, cutoff=0.8)[0]).upper()
        # Prompt user for similarity check confirmation
        if yn == "Y":
            return data[get_close_matches(word, keys, cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your entry."
    else: 
        return "The word doesn't exist. Please double check it." 
    
    
word = input("Enter a word: ")
# Making the search case insensitive, lowercase for all searches
output = search(word.lower())

# Optimise output for list
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)