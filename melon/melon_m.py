# 모바일 환경으로 접속해서 크로링한다.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import json



'''
user = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
#initiation
options = Options()

#유저 정보넣기
options.add_argument("user-agent = Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.1")
#화면 자동종료 해제 
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

# user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#driver = webdriver.Chrome(options=chrome_options)

header ={
    "Host":"m2.melon.com",
    "Referer": "https://m2.melon.com/index.htm",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
'''

mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)

#크롤링할 코드 
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(3)

if driver.current_url != url:
    driver.get(url)
    time.sleep(1)
    # 팝업창 닫기


driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.2)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()

html = driver.page_source

#beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# record updated time
today = datetime.today().strftime("%Y%m%d")
updated_time = soup.select_one(".txt-time").text.strip()[4:]
updated_time = today + " " +updated_time
print(updated_time)

# get top100 song list
top100 = soup.select("li.list_item")
print(len(top100))

# https://programmingbeginner.tistory.com/entry/8-JSON-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80-%ED%85%8C%EC%9D%B4%EB%B8%94%EB%A1%9C-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0
# https://kerpect.tistory.com/71
# https://with-ahn-ssu.tistory.com/51

# date : key - updated time, value - list of row-data(dict)
data_list = []

for song in top100:
    rank = song.select_one(".ranking_num")
    if rank:
        img_link = song.select_one(".img")["style"]
        print(img_link)
        img_link = "https:" + re.search(r'\//([^)]+)', img_link).group().strip()[:-1] # ()안의 문자열 받아오기
        # updown = song.select_one(".rankimg_updown .ranking_hide")
        title = song.select_one(".title")
        singer = song.select_one(".name")
        print(img_link)
        # print(updown.text)
        print(title.text.strip())
        print(singer.text.strip())
        print(rank.text)
        print("="*20)

        data_list.append({"ranking": rank.text.strip(), "singer": singer.text.strip(),"title": title.text.strip(),"image": img_link})


# save to a json file
save_dir = "./melon/melon_"+ updated_time +".json" 
with open(save_dir, 'w', encoding = 'utf-8') as file:
    json.dump(data_list, file, indent = "\t")
