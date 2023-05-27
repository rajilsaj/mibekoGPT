import requests
from bs4 import BeautifulSoup
import pdfkit

# Set the URL for the Python documentation
url = 'https://docs.python.org/3.10/'

# Send a GET request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the documentation page
links = soup.find_all('a')

# Create a list to store the URLs for each documentation page
doc_urls = []

# Loop through the links and extract the URLs for each documentation page
for link in links:
    if link.get('href') and link.get('href').startswith('https://docs.python.org/3.10/'):
        doc_urls.append(link.get('href'))

# Use pdfkit to convert the documentation to a PDF file
pdfkit.from_url(doc_urls, 'python-documentation.pdf')

