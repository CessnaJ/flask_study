import selenium
import pandas
import numpy
import request
import requests
from bs4 import BeautifulSoup as bs

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

broswer = webdriver.Chrome("./chromedriver 2") # 어떤 브라우저 쓸지
url = "http://bfzido.org/home/#/list"          # 접속 URL
# driver = webdriver.Chrome('chromedriver_path')
broswer.maximize_window()                      # 새창 열어서 키우고
broswer.get(url)                               # url로 접속

elem = driver.find_element_by_tag_name("body")
last_height = driver.execute_script("return document.body.scrollHeight")

time_interval = 2

while True:
    scroll_down = 0
    while scroll_down < 500:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(time_interval)
        scroll_down += 1
    
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("********" + lecture['category'] + ' / ' + lecture['subCategory']  + " break********")
        break

    last_height = new_height


broswer.getPageSource()

http://bfzido.org/rest/web/v1/spot/spots?restApiKey=gcf703504d5556d38602b1e89db1257d&queryType=list&orderBy=rate&offset=0&limit=1100&searchInfo=spot_name like 대전 or spot_address like 대전