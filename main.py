import requests 
from bs4 import BeautifulSoup

URL = "https://www.sgg.cg/JO/"

def extract_data(url):
    result = requests.get(URL).text
    doc = BeautifulSoup(result, 'html.parser')

    links = doc.find_all('a')
    linked = []
    for a in links:
        linkis = a.string
        if not (linkis.isalpha()):
            linkin = linkis[:len(linkis) - 1]
            linked.append(linkin)
            #print(linkin)
            #print()

    return linked


print(extract_data(URL))
