import requests
from bs4 import BeautifulSoup


def get_links(sites, keyword):
    links = {}
    for site in sites:
        url = "http://google.ru/search?q=" + keyword + "&as_sitesearch=" + site + "&as_qdr=d3"


        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        for item in soup.select(".r a"):
            if ("http" in str(item)):
                links[item.text] = str(item)[str(item).index('http'):str(item).index('&')]

    return links