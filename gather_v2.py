import os
import csv
from bs4 import BeautifulSoup

directory = r'#'

with open('company_description.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['domain', 'header', 'company_description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                domain = soup.title.string if soup.title else ''
                company_description = ''
                
                for p in soup.find_all('p'):
                    company_description += p.text
                for h1 in soup.find_all('h1'):
                    company_description += h1.text
                if domain:
                    writer.writerow({'domain': filename, 'header': domain, 'company_description': company_description})

#I changed the directory and API to number sign for privacy.