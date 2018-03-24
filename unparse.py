# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:45:24 2018

@author: Александр"""

import requests
from bs4 import BeautifulSoup

def get_links(site,keyword):
    
    url = "https://google.ru/search?q="+keyword+"&as_sitesearch="+site+"&as_qdr=d3"
    #url = "http://google.ru/search?q=site: habrahabr.ru android"
    print(url)
    links = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    
    for item in soup.select(".r a"):
        if("http" in str(item)):
            #links.append(item)
            links.append(str(item)[str(item).index('http'):str(item).index('&')])
            
    return links

print(get_links('habrahabr.ru','android'))
