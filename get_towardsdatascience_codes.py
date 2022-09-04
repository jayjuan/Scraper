from bs4 import BeautifulSoup
import requests

link = requests.get("https://towardsdatascience.com/image-processing-with-python-color-isolation-for-beginners-3b472293335b")

soup = BeautifulSoup(link.text, "html.parser")

tmp = []
for i in soup.findAll(('span', {'id':'2b63'})):
    if i == '':
        tmp.append('\n')
    else:
        tmp.append(i.text)
    
# tmp = [x for x in tmp if not x == '']


for i in tmp:
    f = open("towardsdatascience_codes.txt", "w")
    f.write(i)
    f.write('\n')
    f.close()