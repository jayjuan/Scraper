# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:26:57 2021

@author: jjuan
"""

from bs4 import BeautifulSoup
import requests

link = requests.get('https://www.mudah.my/Sabah/Electronics-for-sale-3000')
source = link.text
soup = BeautifulSoup(source, 'html.parser')

txt = open("Mudah_list.txt", 'w')

for parent in soup.findAll('div', {'class': 'sc-gzOgki iiNhZ'}):
    # parent = parent.text.split()
    print(parent)
    if parent is not None: 
        txt.write(parent.text) 
        txt.write('\n')
    
txt.close()