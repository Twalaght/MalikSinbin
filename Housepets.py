#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get
import urllib.request

# Source URL for the archive page
baseurl = "http://www.housepetscomic.com/archive/?archive_year=20"

for page in range(8, 21):
    # Take in the URL and parse it
    if page < 10:
        url = baseurl + "0" + str(page)
    else:
        url = baseurl + str(page)
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    # Find all the comic links on each year archive
    pagelinks = html_soup.find("table", class_ = "month-table").find_all("a")

    # For each extracted page, parse it too
    for i in range(len(pagelinks)):
        response2 = get(pagelinks[i]["href"])
        html_soup2 = BeautifulSoup(response2.text, "html.parser")
        type(html_soup2)

        # Save the link and local name
        comic_page = html_soup2.find("div", class_ = "comic-table").find("img")["src"]
        localname = comic_page[57:]

        # Status message
        print("Parsing page " + str(localname) + "...")

        # Write the image to disk
        urllib.request.urlretrieve(comic_page, localname)