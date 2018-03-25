import requests
from bs4 import BeautifulSoup


def get_links(sites, keyword):
    links = {}
    site_name = ""
    for site in sites:
        site_name += "+site%3A" + site + "+%7C"
    url = "http://google.ru/search?q=" + keyword + site_name + "&as_qdr=d3"


    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    for item in soup.select(".r a"):
        if ("http" in str(item)):
            links[item.text] = str(item)[str(item).index('http'):str(item).index('&')]

    return links