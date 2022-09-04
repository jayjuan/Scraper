# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:59:03 2021

@author: jjuan
"""

import requests
from bs4 import BeautifulSoup

link = requests.get("https://my.shein.com/category/Men-Shoes-Accessories-sc-00811755.html?ici=my_tab04navbar07&scici=navbar_MenHomePage~~tab04navbar07~~7~~itemPicking_00811755~~~~0&srctype=category&userpath=category%3ESHOES-ACCESSORIES")
txt = link.text
soup = BeautifulSoup(txt, "html.parser")

for i in soup.findAll("a",{"class":"S-product-item__link S-product-item__link_jump"}):
    print(i.get('href'))
    print()