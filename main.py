import requests 
from bs4 import BeautifulSoup

URL = "https://www.sgg.cg/JO/"

result = requests.get(URL).text
doc = BeautifulSoup(result, 'html.parser')
#print(doc.prettify())

links = doc.find_all('a')
for a in links:
    print(a.string)
    print()
