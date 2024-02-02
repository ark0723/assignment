import requests
from bs4 import BeautifulSoup
from random import randint
import time
import pandas as pd
import csv


data = []

# 2023년 역주행차트 리스트
for month in range(1,13): 

    str_month = str(month).zfill(2)

    url = "https://www.melon.com/chart/month/index.htm?classCd=GN0000&moved=Y&rankMonth=2023{}".format(str_month)
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=header)

    soup = BeautifulSoup(res.text, "lxml")
    top100_monthly = soup.select(".lst50") + soup.select(".lst100")
    print(len(top100_monthly))

    date = '2023' + str_month

    for rank, song in enumerate(top100_monthly, 1):
        if song.select_one(".rank_up"):
            up = int(song.select_one(".rank_wrap")['title'].split(" ")[0][:-2])
            title = song.select_one(".rank01 a")
            singer = song.select_one(".rank02 a")
            album = song.select_one(".rank03 a")
            # print(up, title.text, singer.text, album.text)
            row_data = [date, rank, up, title.text, singer.text, album.text]
            data.append(row_data)
    # time.sleep(randint(1,3))


df = pd.DataFrame(data, columns = ["date", "rank", "up", "title", "singer", "album"])

# save df to csv 
df.to_csv("data/melon_up_2023.csv")

# load kospi_df
# data = pd.read_csv("data/kospi_df.csv", index_col=0)