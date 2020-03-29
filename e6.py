import requests
from bs4 import BeautifulSoup
from io import open as iopen

#User settings
downloadLocation = r"C:\Users\Jono\Downloads"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}


def poolLinkRip(pool, headers):
    postLinks = []
    page = 1
    morePages = False
    url = "https://e621.net/pool/show/" + str(pool) + "?page=1"
    soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")

    print(soup)

    if soup.find("div", class_="pagination"):
        morePages = True

    for data in soup.find_all("span", class_="thumb"):
        for a in data.find_all("a"):
            postLinks.append("https://e621.net" + (a.get("href")))

    while morePages:
        page += 1
        url = url[:-1] + str(page)
        soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
        for data in soup.find_all("span", class_="thumb"):
            for a in data.find_all("a"):
                postLinks.append("https://e621.net" + (a.get("href")))
        if soup.find("span", class_="disabled next_page"):
            morePages = False
    return postLinks

def imgDL(links):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                         (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

    print(len(links))

    url = links[0]
    soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")

    lists = []
    for li in soup.findAll('li'):
        lists.append(li)


    topkek = soup.find("div", id="stats")

    kekulet = []
    for a in topkek.find_all("a"):
        kekulet.append(a.get("href"))

    print(kekulet)

    i = requests.get(kekulet[3])
    with iopen(r"C:\Users\Jono\Downloads\MASSIVE JEW.png", 'wb') as file:
        file.write(i.content)

'''
    testArry = []
    for data in soup.find_all("div", class_="stats"):
        testArry.append(data.get("ul"))
'''




#postLinks.append((a.get("href")))



pool1 = poolLinkRip(12908, headers)
#pool2 = poolLinkRip(14043)

print(pool1)

#imgDL(pool1)




