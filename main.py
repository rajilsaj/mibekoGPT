import os
import requests 
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger

main = "https://www.sgg.cg/JO/"
merger = PdfMerger()

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
            lnew = new_url + '/' + link
            #print(lnew)
            if link.endswith('.pdf') :
                pdf.add(lnew)
    return pdf

def Save():
    for item in Parse_links():
        r = requests.get(item, stream=True)
        pdf_file_name = os.path.basename(item)
        if r.status_code == 200:
                filepath = os.path.join(os.getcwd(), pdf_file_name)
                with open(filepath, 'wb') as pdf_object:
                    pdf_object.write(r.content)
                    print(f'Printed successfully {pdf_file_name}')
                    return True
                    merger.append(filepath)
                merger.write("result.pdf")
                merger.close()
        else:
            print(f'Uh oh! Could not download {pdf_file_name},')
            print(f'HTTP response status code: {response.status_code}')
            return False

    print("done")





Get_links()
Parse_links()
Save()
