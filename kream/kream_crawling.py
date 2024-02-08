# import library
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium options
from selenium.webdriver.chrome.options import Options
#크롬 드라이버 매니저 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
# 자동으로 크롬 드라이브를 최신으로 유지해주는 패키지
from webdriver_manager.chrome import ChromeDriverManager
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
# 키보드 입력
from selenium.webdriver.common.keys import Keys
# consider js rendering time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from random import random
import json

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent = {user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

# chromeDriverManger  would be automatically installed 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = options_)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

# 알아서 클릭하도록 동작 설정(돋보기 클릭)
driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(random() + 0.3)

# 검색창에 검색어 보내기
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(random() + 0.3)

# driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림\n")
# enter key를 누르게 한다.
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(random() + 0.1)

# get current url
current_url = str(driver.current_url)
print("The current url is: ", current_url)

# redirect by category
categories = {"outer":63,"top": 64, "bottom":65, "shoes": 34, 
              "bag": 9, "wallet": 66, "watch":54, "accessory": 7}

def change_unit(amount: str):
    if '만' in amount:
        num = float(amount[:-1])*10000
        return str(num)
    else:
        return amount

# create empty list for json object
data = []

for key, val in categories.items():
    redirect_url = current_url + '&shop_category_id={}'.format(categories[key])
    # how long would you wait for rendering a page
    wait = WebDriverWait(driver, 10)
    driver.get(redirect_url)
    wait.until(EC.url_to_be(redirect_url))

    # 자동으로 스크롤 내리기
    for i in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(random()+0.2)

    # getting html text
    html = driver.page_source
    # crawling with bs4
    soup = BeautifulSoup(html, "html.parser")
    # each item
    items = soup.select(".search_result_item.product")

    for i in items:
        # row_data : empty dict
        row_data = {}

        #crawling part
        name = i.select_one(".translated_name").get_text()
        product_num = i["data-product-id"]
        product_url = "https://kream.co.kr" + i.select_one(".item_inner")["href"]
        img_url = i.select_one(".product_img > img")["src"]
        brand = i.select_one(".product_info_brand").get_text().strip()
        price = i.select_one(".amount").get_text().strip().replace(",","")[:-1]
        if not price: # if price not present on webpage
            price = 0
        
        transaction = i.select_one(".status_value")
        if transaction:
            transaction = i.select_one(".status_value").get_text().strip().replace(",","").split(" ")[1]
            transaction = change_unit(transaction)
        else: 
            transaction = 0

        review_link = "https://kream.co.kr/social/products/" + product_num
        wish = i.select_one(".action_wish_review .text")
        if wish:
            wish = wish.get_text().strip().replace(",","")
            wish = change_unit(wish)
        else:
            wish = 0
        
        reviews = i.select_one(".review_figure .text")
        if reviews:
            review_num = reviews.get_text().strip().replace(",","")
            review_num = change_unit(review_num)
        else:
            review_num = 0
        # row_data: dict(key, val)
        row_data['product_id'] = product_num
        row_data['category'] = key
        row_data['brand'] = brand
        row_data['title'] = name
        row_data['price'] = price
        row_data['sales'] = transaction
        row_data['wish'] = wish
        row_data['review'] = review_num
        row_data['img'] = img_url
        row_data['product_link'] = product_url
        row_data['review_detail'] = review_link
        data.append(row_data)
driver.quit()

print(len(data))

# save data into json file
save_ = 'kream/data/item.json'
with open(save_, 'w') as f:
    json.dump(data, f)