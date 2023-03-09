# 코드의 의도 -> 검색돌릴 재료가 되는 bf data를 pandas df로 불러오고 그걸 iterate하면서 selenium으로 검색돌림. 결과 나오면 새로운 df에 append 안나오면 제낌.
# 안나오는거 걸러주는건 마지막에 일괄로 한다.

import requests
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd
import time

from webdriver_manager.chorme import ChromeDriverManager


# chromedriver = '/Users/datakim/workspace/selenium_learning/chromedriver' # 크롬드라이버의 경로를 써줘야 그걸 불러와서 씀. 절대경로 쓰는게 편하다. 컴퓨터마다 다르니까 경로 찾아보고 적용
# driver = webdriver.Chrome(chromedriver) 
driver = webdriver.Chrome(ChromeDriverManager.install()) # 크롬 경로 받아오는걸 자동으로 해주는 라이브러리 설치 후 적용.
# 포스팅 작성 당시 크롬 버젼 : 92
# 20230309 크롬버전 - 110.0.5481.178


# CSV 파일 경로와 파일 이름 지정. 이제 csv파일 불러올것임. ( 행렬 순회하면서 검색돌리고 그 결과를 csv에 저장할것임. )
csv_file = 'bf_data_109.csv'
# CSV 파일을 DataFrame 객체로 불러오기
bf_df = pd.read_csv(csv_file)
result_df = pd.DataFrame(columns=['search_index', 'search_keyword', 'naver_map_url'])
# 일단 spotName으로 검색해본다. 😀
search_keyword = 'spotName'

# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.
# df['naver_keyword'] = df['dong'] + "%20" + df['name']  # "%20"는 띄어쓰기를 의미합니다.

# df['naver_map_url'] = ''


# 본격적으로 가게 상세페이지의 URL을 가져옵시다

for i, keyword in enumerate(bf_df[search_keyword].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {bf_df.shape[0] -1} 행", keyword)
    try:
        naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={keyword}&sm=hty&style=v5"
        
        driver.get(naver_map_search_url)
        time.sleep(3.5)
        df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
        # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
        # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
        
        #만약 검색 결과가 없다면?
    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                df.iloc[i,-1] = driver.find_element_by_css_selector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
                time.sleep(1)
            except Exception as e2:
                print(e2)
                df.iloc[i,-1] = np.nan
                time.sleep(1)
        else:
            pass


driver.quit()


# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url']


# URL이 수집되지 않은 데이터는 제거합니다.
df = df.loc[~df['naver_map_url'].isnull()]