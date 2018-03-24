# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:43:02 2018

@author: Александр
"""
import requests
from bs4 import BeautifulSoup

def get_links(site,keyword):

    url = "https://search.google.com/search?q="+keyword+"&as_sitesearch="+site+"&as_qdr=d3"
    links = {}

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    for item in soup.select(".r a"):
        if("http" in str(item)):
            links[item.text] = str(item)[str(item).index('http'):str(item).index('&')]

    return links

#print(get_links('habrahabr.ru','android'))