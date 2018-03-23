# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:45:24 2018

@author: Александр"""

import requests
from bs4 import BeautifulSoup

def get_links(url):
    
    links = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    
    for item in soup.select(".r a"):
        if("http" in str(item)):
            links.append(str(item)[str(item).index('http'):str(item).index('&')])
            
    return links

#print(get_links('https://www.google.ru/search?q=android'))
