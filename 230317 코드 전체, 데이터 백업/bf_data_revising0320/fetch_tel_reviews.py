# 안나오는거 걸러주는건 마지막에 일괄로 한다.
import requests
import csv
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup 

import pandas as pd
import numpy as np
import time
import random
import re

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# Chrome 드라이버 서비스 객체 생성
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=options)

# CSV 파일 경로와 파일 이름 지정. 이제 csv파일 불러올것임. ( 행렬 순회하면서 검색돌리고 그 결과를 csv에 저장할것임. )
csv_file = './merged.csv'

# CSV 파일을 DataFrame 객체로 불러오기
bf_df = pd.read_csv(csv_file)

# 검색어 재료가 될 keyword
cid = 'cid'
sid = 'sid'

# 행 추가 - 새로운 필드를 추가함.
bf_df['naver_open_hours'] = ""
bf_df['naver_tel'] = ""
bf_df['user_reviews'] = ""
bf_df['theme_keyword'] = ""
bf_df['menu'] = ""


def write_csv_by_line(idx, new_csv):#
    if idx == 0:
        bf_df.iloc[[idx]].to_csv(new_csv, header=True, index=False)
    else:
        bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.


def regex_find_tel(text_list):
    for item in text_list:
        phone_pattern = re.compile(r'(\d{2,4}-)?(\d{2,4})?-\d{4}') # 전화번호 패턴 찾기
        match = phone_pattern.search(str(item))
        if match:
            phone_number = match.group(0)
            # print(phone_number)
            return phone_number
        

    else: # 다 돌때까지 못찾았다.
        print("Phone number not found.")
        return []


def fetch_naver_tel(driver):#
    try:
        soup = fetching_html_source(driver)
        
        div_list = soup.select('#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div')
        # print(2)
        # print(div_list[0])
        tel_num = regex_find_tel(div_list)
        print(f'전화번호 추출된것.:{tel_num}')
        # tel_el = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[6]/div/div[1]/div/div/div[3]/div/span[1]')
        # /html/body/div[3]/div/div/div/div[6]/div/div[1]/div/div/div[3]/div/span[1]
        # tel_num = tel_el.text
        return tel_num
    except Exception as err:
        print(err)
        return 'null'
        


def page_down(driver):#
    # actions = ActionChains(driver)
    # actions.send_keys(Keys.PAGE_DOWN).perform()
    js_code = "window.scrollBy(0, 1000)"

    # 자바스크립트 코드 실행
    driver.execute_script(js_code)
    time.sleep(2)


def click_naver_open_hours(driver):#
    try:
        # element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[6]/div/div[1]/div/div/div[2]/div/a')
        print('클릭시도')
        time.sleep(1)
        element = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.pSavy > div > a > div')
        # element = driver.find_element(By.CLASS_NAME, 'gKP9i.RMgN0')

        # /html/body/div[3]/div/div/div/div[6]/div/div[1]/div/div/div[2]/div/a
        element.click()
        print('clicked')
        time.sleep(1)
    except Exception as e1:
        print('e1')
        print(e1)
        return 'null'




def fetching_html_source(driver):#
    # HTML 코드 가져오기
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    return soup


def fetch_naver_open_hours(soup):
    try:
        # CSS 선택자로 자식 div 태그 선택하여 리스트로 저장
        div_list = soup.select('#app-root > div > div > div > div:nth-child(7) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.pSavy > div > a > div')
        #app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.pSavy > div > a
        
        # print(div_list)
        arr = []
        for item in div_list:
            arr.append(str(item))
            # print(item)
            # print(str(item))
        print('got open hours')
        # print(arr)
        return str(arr)
    except Exception as e2:
        print('open hours 가져오는거에서 에러')
        print('e2')
        print(e2)
        return 'null'


def fetch_user_reviews(soup):
    try:
        div_list = soup.select('#app-root > div > div > div > div:nth-child(7) > div > div:nth-child(6) > div > div.TraH1 > ul > li')
        return str(div_list)
    except Exception as e3:
        print('e3')
        print(e3)
        return 'null'


def fetch_menu(soup):
    try:
        div_list = soup.select('#app-root > div > div > div > div:nth-child(7) > div > div:nth-child(3) > div > ul > li')
        return str(div_list)
    except Exception as e4:
        print('e4')
        print(e4)
        return 'null'



def fetch_theme_keyword(soup):
    try:
        div_list = soup.select('#app-root > div > div > div > div:nth-child(7) > div > div.place_section.I_y6k > div.place_section_content > div > div > ul > li')
        return str(div_list)
    except Exception as e5:
        print('e5')
        print(e5)
        return 'null'




def to_search_iframe(driver):
    driver.switch_to.default_content() # 기본 프레임으로 일단 커서 옮기기. - 추후 iframe전환
    driver.switch_to.frame('entryIframe')




# 본격적 실행 시작.
with open('tel_review_added.csv', 'a', encoding='utf-8', newline='') as new_csv:
    for idx, row in bf_df[['sid', 'cid']].iterrows():
        if idx < 2390: # xlsx에서 257부터 채워나가야하는데, idx < 254로 조건 걸면 딱 맞다. -> 2248부터= idx < 2245 // 2393부터 idx<2390
            continue
        print(f'{idx}번째 {row}으로 시행')

        if np.isnan(row['sid']): # 비어있으면
            write_csv_by_line(idx, new_csv)
            continue  # 해당 행을 건너뜀

        sid = int(row['sid'])
        cid = int(row['cid'])
    
        print("이번에 찾을 키워드 :", idx, f"/ {bf_df.shape[0] -1} 행", cid)
        try:
            # naver_open_hours
            # naver_tel
            # user_reviews
            # theme_keyword
            # menu
            
            naver_map_search_url = f"https://map.naver.com/v5/entry/place/{cid}?c=15,0,0,0,dh"
            driver.get(naver_map_search_url)
            time.sleep(random.choice([3]))
            to_search_iframe(driver)
            print('0')
            
            bf_df.loc[idx, 'naver_tel'] = fetch_naver_tel(driver)
            click_naver_open_hours(driver)
            page_down(driver)
            soup = fetching_html_source(driver)
            bf_df.loc[idx, 'naver_open_hours'] = fetch_naver_open_hours(soup)
            bf_df.loc[idx, 'user_reviews'] = fetch_user_reviews(soup)
            bf_df.loc[idx, 'menu'] = fetch_menu(soup)
            bf_df.loc[idx, 'theme_keyword'] = fetch_theme_keyword(soup)
            write_csv_by_line(idx, new_csv)
        except Exception as error:
            write_csv_by_line(idx, new_csv)
            print(error)

        
        # if idx == 30:
            # break


driver.quit()