import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        abc = input("Enter an element that is in the URL:")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if abc in url:
                print("\n" + web+ '/' + url)
xyz = input("Enter a site:")
web = xyz
Scraper(web).scrape()