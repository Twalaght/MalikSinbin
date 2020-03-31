#!/usr/bin/python3

import argparse
from bs4 import BeautifulSoup
from requests import get
import urllib.request

# parser = argparse.ArgumentParser(description="Download all the images from a pool on e621")
# parser.add_argument("pool", metavar="pool", type=str, help="Pool ID to download")
# args = parser.parse_args()


import requests


#requests.get("https://e621.net", auth=("Twalaght", ""))

poollinks = get("https://e621.net/pools/11139.json", auth=("Twalaght", ""))
print(poollinks)

# # Source URL for the archive page
# baseurl = "https://e621.net/pools/" + "11139" + "?page=1"

# # Take in the URL and parse it
# response = get(baseurl)
# html_soup = BeautifulSoup(response.text, "html.parser")
# type(html_soup)

# # Find all the image links on the index page
# pagelinks = html_soup.find(id="a-show")

# print(html_soup)


# for page in range(8, 21):
#     
#     if page < 10:
#         url = baseurl + "0" + str(page)
#     else:
#         url = baseurl + str(page)
#     

#     # Find all the comic links on each year archive
#     

#     # For each extracted page, parse it too
#     for i in range(len(pagelinks)):
#         response2 = get(pagelinks[i]["href"])
#         html_soup2 = BeautifulSoup(response2.text, "html.parser")
#         type(html_soup2)

#         # Save the link and local name
#         comic_page = html_soup2.find("div", class_ = "comic-table").find("img")["src"]
#         localname = comic_page[57:]

#         # Status message
#         print("Parsing page " + str(localname) + "...")

#         # Write the image to disk
#         urllib.request.urlretrieve(comic_page, localname)





# def main():


#     if not os.path.isfile(args.filename):
#         print('The file  does not exist')
#         sys.exit()

#     random.seed(args.seed)
#     mycrypto(args.filename)

# if __name__== "__main__":
#     main()