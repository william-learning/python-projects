"""
Website Blocker

Author: William
Date: 15/11/2017

https://github.com/williamsoftwarecode/python-projects

This application is a website blocker that runs in the background. 
Features include: 
    1. Prevents access to certain websites such as Facebook during fixed hours
    2. Website links/URL can be passed into the application as strings 
    
Additional Notes:
    1. Focus on file manipulation, dates and times
    2. Process in the background
    3. curl -Is www.facebook.com | head -1
       Command is used to check if URL can be reached
       
Program Architecture: 
Windows: C:\Windows\System32\drivers\etc\hosts
Linux/Mac: etc/hosts

"""



import time

# r prefix necessary to avoid escape characters
# hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path="/etc/hosts/"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

num = 0

while True:
    num=num+1
    print(num)
    time.sleep(5)
    
