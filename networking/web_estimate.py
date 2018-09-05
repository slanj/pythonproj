import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def crawler(base, url, deep, x = ctx):
    if deep == 0:
        return
    print("Retrieving: ", base + url)
    req = urllib.request.Request(base[:-1] + url, headers={'User-Agent' : "Super Browser"})
    html = urllib.request.urlopen(req, context=x).read()
    soup = BeautifulSoup(html, 'html.parser')
    inno_count = find_innovation(soup)
    istudios[base]['Innovation'] += inno_count
    print(inno_count)
    tags = soup('a')
    for tag in tags:
        link = tag.get('href', '')
        if re.search('^/', link) and not re.search('clickfrog', link):
            try:
                crawler(base, link, deep-1)
            except:
                continue

def find_innovation(soup):
    entries = soup.find_all('p')
    text = [e.get_text() for e in entries]
    text = " ".join(text)
    inno_list = re.findall("ннова", text)
    return len(inno_list)

studios = {'https://wezom.com.ua/': 8372, 'https://mahaon.ua/': 7343, 'https://artjoker.ua/': 4841, 'https://www.media5.com/': 4676, 'https://promodex.net/': 3885, 'https://artlanding.net/': 3740, 'https://www.whiteweb.ua/': 2911, 'https://dmi3yy.com/': 2623, 'https://fnx.dp.ua/': 2414, 'https://www.mega-site.com.ua/': 2382, 'https://seosolution.ua/': 2370, 'https://simplamarket.com/': 2358, 'https://webpc.com.ua/': 2273, 'https://www.linecore.com/': 2263, 'https://web-stolica.com.ua/': 2242, 'https://aweb.ua/': 2130, 'https://stearling.net/': 2019, 'https://art-lemon.com/': 2019, 'https://vintage.com.ua/': 1915}

istudios = {}

for url, rating in studios.items():
    istudios[url] = {'Rating': rating, 'Innovation': 0}


for base in istudios.keys():
    crawler(base, '/', 2)

print(istudios)


