# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:45:24 2018

@author: Александр
"""

import requests
from bs4 import BeautifulSoup
page = requests.get("http://www.google.ru/search?q=android&as_qdr=h5") #Запрос приводить к форме search?q=*
soup = BeautifulSoup(page.content)
import re
links = soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(re.split(":(?=http)",link["href"].replace("/url?q=","")))