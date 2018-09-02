import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Roxabella.html"

def crawler(url, deep):
    print("Retrieving: ", url)
    if deep == 0:
        return url
    req = urllib.request.Request(url, headers={'User-Agent' : "Super Browser"})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count += 1
        if count == 18:
            return crawler(tag.get('href', None), deep-1)

final_url = crawler(url, 7)
print(final_url)