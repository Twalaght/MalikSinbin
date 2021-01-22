#!/usr/bin/python3

from bs4 import BeautifulSoup
from requests import get
import urllib.request
from pathlib import Path
import re

page = get(f"https://feliniacomic.com/2017/08/16/comic-cover/")

Path("Felinia").mkdir(parents=True, exist_ok=True)

counter = 1

while True:
    html_soup = BeautifulSoup(page.text, "html.parser")
    nextlink = html_soup.find(class_ = "nav-next").find("a")["href"]
    image = html_soup.find_all("img")[2]["data-src"]

    print(f"Downloading {image}...")

    title = re.sub(".*/uploads/", "", image)
    title = re.sub("/", "_", title)

    img_path = Path.cwd() / "Felinia" / (str(counter) + Path(title).suffix)


    # Write the image to disk
    urllib.request.urlretrieve(image, img_path)
    counter = counter + 1
    page = get(nextlink)

quit()
