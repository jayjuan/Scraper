# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 17:23:53 2021

@author: jjuan
"""

from bs4 import BeautifulSoup
import requests
import re

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }  

source = requests.get('https://iprice.my/computing/hardware/graphic-cards/', headers = header)
link = source.text
soup = BeautifulSoup(link, 'html.parser')
title = soup.find('a', {'class':'cN ey kR qt lQ eZ c em ra hA kF uc ud kL oT'})

temp = []
for i in soup.findAll(('a', {'class':'cN ey kR qt lQ eZ c em ra hA kF uc ud kL oT'})):
    
    # Prints GPU name from div tag
    div = i.find('span', attrs={'class': 'truncate-2 db webkit-box-ns oz kH oV gE g ht b uD'})
    if div is None: # Error checking to make sure div is non empty
        pass        # .text cant be used if div is empty
    else:
        print(div.text)

    price = i.find('div', {'class':'gM G pb0-ns cN lQ nW qz fl c_ kG kp b er uC'})
    if price is None: 
        pass        
    else:
        price = price.text.split()
        print(price[0], price[1])
        print('')

    

    

    # print(div.get('span'))
    
    # print(i.get('div'), {'class':'cN lQ hw eK ei h n0 bt-ns hR h- t_ hy ua er b--orange'})

# for name in soup.findAll('a', {'class':'cN ey kR qt lQ eZ c em ra hA kF uc ud kL oT'}):
#     print(name.get('div'))

# for price in soup.findAll('div', {'class':'a- db ue iR'}):
#     print("Price(MYR): " + price.text)

