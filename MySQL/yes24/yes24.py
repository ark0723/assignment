from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager().install()

# chromedriver 실행이 되지 않을경우 경로지정
'''
1. 상대경로
path = "/.chromedriver

browser = webdriver.Chrome(path)
'''

path = "/.chromedriver"

browser = webdriver.Chrome(path)
# browser = webdriver.Chrome()
browser.get("http://naver.com")

