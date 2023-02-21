import csv
from bs4 import BeautifulSoup
import os
import time


def get_most_recent_files(dir_path, file_extension, n=3):
    files = [f for f in os.listdir(dir_path) if f.endswith(file_extension)]
    files_with_time = [(f, os.path.getmtime(os.path.join(dir_path, f))) for f in files]
    files_with_time.sort(key=lambda x: x[1], reverse=True)
    return [f[0] for f in files_with_time[:n]]

# Get the current working directory
dir_path = os.getcwd()

# Get the 3 most recent .html files
recent_files = get_most_recent_files(dir_path, ".html", 3)

# Print the names of the 3 most recent files
for file in recent_files:
    print(file)

file_name = input("Enter the name of the HTML file (including the .html extension): ")

# Open the HTML file
with open(file_name, 'r', encoding='ISO-8859-1') as file:
    html_content = file.read()

# Parse the HTML content of the file
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <p> tags
paragraphs = soup.find_all('p')

# Find all the <h1> tags
headers = soup.find_all('h1')

# Merge all the text content of the <p> tags into one sentence
company_description = " ".join([p.text for p in paragraphs])

# Replacing 'â' with '’'
company_description = company_description.replace('â',"'")

# Replacing 'Â' with ' '
company_description = company_description.replace('Â'," ")

company_description = company_description.replace("â",'')

# Merge all the text content of the <h1> tags into one sentence
header_description = " ".join([h.text for h in headers])

# Combine the company and header description
result = company_description + " " + header_description

# Specify the file name for the CSV file
csv_file = "paragraphs.csv"

# Write the data to the CSV file
with open(csv_file, 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Company Description'])
    writer.writerow([result])

print(f"Data has been written to {csv_file}")
