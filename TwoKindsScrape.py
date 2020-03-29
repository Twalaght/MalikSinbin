#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get
import urllib.request

for page in range(1, 1102):
    # Take in the URL and parse it
    url = "http://twokinds.keenspot.com/comic/" + str(page) + "/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    # Find the comic part of the HTML, set the url and local file name
    comic_page = html_soup.find("article", class_ = "comic").find("img")["src"]
    localname = comic_page[40:]

    # Status message
    print("Parsing page " + str(page) + "...")

    # Write the image to disk
    urllib.request.urlretrieve(comic_page, localname)