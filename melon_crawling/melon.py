import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'

res = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
soup = BeautifulSoup(res.text, "lxml")

# tr.lst50, tr.lst100
# rank: .wrap t_center span.rank
'''
top50 = soup.select(".lst50")
top100 = top50 + soup.select(".lst100") 
print(len(top100))
'''

top100 = soup.find_all(class_ = ["lst50", "lst100"])
print(len(top100))

for rank, song in enumerate(top100, 1):
    title = song.select_one(".rank01 a")
    singer = song.select_one(".rank02 >a")
    album = song.select_one(".rank03 a")

    print(f"{rank}위곡 - album: {album.text.strip()}, singer: {singer.text}, title: {title.text.strip()}")
    print("="*20)
