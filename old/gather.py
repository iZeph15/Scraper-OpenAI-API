import csv
import os
import requests
import time
from bs4 import BeautifulSoup
from slugify import slugify

# prompt the user for the name of the CSV file and column header
file_name = input("Enter the name of the CSV file: ")
col_name = input("Enter the column name of the URLs: ")

# create a folder to save the results
folder_name = "html"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# open the CSV file and read the website domains
with open(file_name, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # retrieve the website domain from the CSV file
        url = row[col_name]
        
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
            
        print("Processing: ", url)
        # send a request to the website and retrieve the HTML
        try:
            response = requests.get(url)
            about_response = requests.get(url+"/about")
        except:
            print("Error: Failed to establish a new connection for ", url)
            continue
            
        html = response.text
        about_html = about_response.text
        
        # use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(html, 'html.parser')
        about_soup = BeautifulSoup(about_html, 'html.parser')

        # save the parsed HTML to a .html file
        with open(os.path.join(folder_name, slugify(url) + ".html"), "w", encoding='utf-8') as file:
            file.write(str(soup))
            
        with open(os.path.join(folder_name, slugify(url+"_about") + ".html"), "w", encoding='utf-8') as about_file:
            about_file.write(str(about_soup))
            
        time.sleep(1) # Add a delay of 1 sec before sending the next request
