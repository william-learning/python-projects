"""
Website Backend

Author: William
Date: 16/11/2017

https://github.com/williamsoftwarecode/python-projects

This application is builds a website with Python via Flask. 
Features include: 
    1. Backend to serve HTML files (static websites)
    2. Deployed website on a live server
    
Additional Notes:
    1. Flask contains all the prototypes to set up websites

"""


from flask import Flask
import os

# Instantiating an object of the Flask class 
app=Flask(__name__)

@app.route('/')
def home():
    return "Website homepage"
    
@app.route('/about/')
def about():
    return "About page: Website content"
    
if __name__=="__main__":
    app.run(debug=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)))