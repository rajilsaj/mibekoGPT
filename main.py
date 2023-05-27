import os
import PyPDF2
import requests
from bs4 import BeautifulSoup


main = "https://www.sgg.cg/JO/"

foldername = main.rstrip('/').split('/')[-1]
if not os.path.exists(foldername):
    os.mkdir(foldername)


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
    del linked[len(linked) - 1]
    return linked


def Parse_links():
    pdf = set()

    for url in Get_links():
        new_url = main + url
        # print(new_url.split('/')[-1])
        r = requests.get(new_url).text
        doc = BeautifulSoup(r, 'html.parser')
        for item in doc.findAll('a'):
            link = item["href"]
            lnew = new_url + '/' + link
            if link.endswith('.pdf'):
                pdf.add(lnew)
    return pdf


def Save():
    for item in Parse_links():
        r = requests.get(item, stream=True)
        filename = item.split("/")[-1]
        # print(item.split('/')[-2])
        with open(f"{foldername}/{filename}", 'wb') as f:
            f.write(requests.get(item).content)
            print(f"{filename}.pdf téléchargé")


Get_links()
Parse_links()
Save()
