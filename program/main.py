import bs4

import requests

r = requests.get("https://quotes.toscrape.com")
print(r)
soup = bs4.BeautifulSoup(r.text)
print(soup)
names = soup.select(".author")
for name in names:
    print(name.text)
    author = set()
    author.add(name.text)
    print(author)


