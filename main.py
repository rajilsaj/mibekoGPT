import requests 
from bs4 import BeautifulSoup

main = "https://www.sgg.cg/JO/"

def Get_links():
    result = requests.get(main).text
    doc = BeautifulSoup(result, 'html.parser')
    links = doc.find_all('a')
    linked = []
    for a in links:
        linkis = a.string
        if not (linkis.isalpha()):
            linkin = linkis[:len(linkis) - 1]
            linked.append(linkin)
    del linked[0:2]
    del linked[len(linked) - 1 ]
    return linked

def Parse_links():
    pdf = set()
    
    for url in Get_links():
        new_url = main + url
        r = requests.get(new_url).text
        doc = BeautifulSoup(r, 'html.parser')
        for item in doc.findAll('a'):
            link = item["href"]
            if link.endswith('.pdf') :
                pdf.add(link)
    print(pdf)
    return pdf

def Save():
    for item in Parse_links():
        print(f"Downloading File: {item[55:]}")
        r = requests.get(item)
        with open(f"{item[55:]}", "wb") as f:
              f.write(r.content)
    print("done")





Get_links()
Parse_links()
#Save()
