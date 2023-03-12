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
import numpy as np
import time
import random
import re

from webdriver_manager.chrome import ChromeDriverManager





# Chrome 드라이버 서비스 객체 생성
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
# Chrome 웹 드라이버 생성
driver = webdriver.Chrome()

# driver = webdriver.Chrome(service=chrome_service)
# chromedriver = '/Users/datakim/workspace/selenium_learning/chromedriver' # 크롬드라이버의 경로를 써줘야 그걸 불러와서 씀. 절대경로 쓰는게 편하다. 컴퓨터마다 다르니까 경로 찾아보고 적용
# driver = webdriver.Chrome(chromedriver) 

# driver_path = ChromeDriverManager().install()
# driver = webdriver.Chrome(driver_path) # 크롬 경로 받아오는걸 자동으로 해주는 라이브러리 설치 후 적용.
# 20230309 크롬버전 - 110.0.5481.178


# CSV 파일 경로와 파일 이름 지정. 이제 csv파일 불러올것임. ( 행렬 순회하면서 검색돌리고 그 결과를 csv에 저장할것임. )
csv_file = './address_zipcode_added2.csv'

# CSV 파일을 DataFrame 객체로 불러오기
bf_df = pd.read_csv(csv_file)
result_df = pd.DataFrame(columns=['search_index', 'search_keyword', 'naver_map_url'])
# 일단 spotName으로 검색해본다. 😀
search_keyword = 'spotName'

# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.
# df['naver_keyword'] = df['dong'] + "%20" + df['name']  # "%20"는 띄어쓰기를 의미합니다.
# df['naver_map_url'] = ''

# 행 추가 - 검색한 키워드, 검색한 결과의 도로명주소, 이후 재료가 될 cid를 추가.
bf_df['new_keyword'] = ""
bf_df['road_address'] = ""
bf_df['result_dong'] = ""
bf_df['cid'] = ""
bf_df['sid'] = ""
bf_df['status'] = ""




def keyword_removing_parenthesis(idx, spotname):
    '''
    키워드만 받아서 spotname(동네)안에 있는 장소 정보를 받아서 "spotname 동네"로 바꿔주는 함수.(이후 띄어쓰기를 %20으로 싹 바꿈)
    '''
    if bf_df.loc[idx, 'streetAddr'] and not pd.isna(bf_df.loc[idx, 'streetAddr']):
        spotname = bf_df.loc[idx, 'streetAddr']+'%20'+spotname
    else:
        spotname = '대전'+'%20'+spotname

    
    if '(' in spotname:
        pattern = r'\((.*?)\)'
        output_str = re.sub(pattern, r' \g<1>', spotname) # 정규표현식 사용해서 재포맷
        output_str = output_str.replace(' ', '%20') # 띄어쓰기를 %20으로 변경
        return output_str
    else:
        return spotname.replace(' ', '%20')



# 본격적으로 가게 상세페이지의 URL을 가져오자.
# 결과값이 있다
with open('fetching_cid_sid_title.csv', 'a', encoding='utf-8', newline='') as new_csv:

    for idx, keyword in enumerate(bf_df[search_keyword].tolist()):
        if idx <= 2160:
            continue

        print("이번에 찾을 키워드 :", idx, f"/ {bf_df.shape[0] -1} 행", keyword)
        writer = csv.writer(new_csv)
        try:
            # 정규표현식 돌려서 브라우저로 돌린다. 그리고 2.5초 후에 긁을것임.
            new_keyword = keyword_removing_parenthesis(idx, keyword)
            naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query={new_keyword}&sm=hty&style=v5"
            driver.get(naver_map_search_url)
            time.sleep(random.choice([0.4, 0.6, 0.56]))

            # 정확한 매칭결과가 있을시, 그걸 넣어준다.
            #ct > div.search_listview._content._ctList > ul > li:nth-child(1) # 안에 있는 data-sid, data-title을 가져오고 싶음.
            #ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview 안에 있는 cid를 가져오고 싶음.
            # 아래 2줄 에러 발생 가능. NoSuchElementException
            outter_element = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li:nth-child(1)') # 여기서 data-sid, data-title 추출
            innter_element = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div > a:nth-child(1)') # 여기서 data-cid 추출
            lotaddress_click = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > div.item_info_inn > div > a').click()
            time.sleep(0.3) # 클릭을 해야 나옴.
            lotaddress = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > div.wrap_bx_address._addressBox > div > p:nth-child(2)') # 여기서 지번주소추출
            
            # 아래 코드들도 에러 발생가능 NoSuchElementException. 하지만 없을시 None을 발생하는게 일반적임.
            sid = outter_element.get_attribute('data-sid')
            title = outter_element.get_attribute('data-title')
            cid = innter_element.get_attribute('data-cid')
            lotaddress_text = lotaddress.text
            print(f'{sid}:{title}:{cid}:{lotaddress_text}')
            
            bf_df.loc[idx, 'sid'] = sid
            bf_df.loc[idx, 'title'] = title
            bf_df.loc[idx, 'cid'] = cid
            

            if str(bf_df.loc[idx, 'streetAddr']) in lotaddress_text:
                bf_df.loc[idx, 'status'] = True
                print(f'{idx}번 잘 됨.')
            else:
                bf_df.loc[idx, 'status'] = 'different'
            
            # print('00')
            if idx == 0:
                bf_df.iloc[[idx]].to_csv(new_csv, header=True, index=False)
            else:
                bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.
            # print('1')

            # ------------------------여기까지 일단.
            # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었음.
            # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됨.
        
        except KeyError as keyerror:
            print(keyerror)

        except Exception as e1: # 검색결과가 없다.
            print(e1)
            if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데?"
                try: # cid만 다시 가져오는걸로 시도.
                    print('2')
                    bf_df.loc[idx, 'status'] = 'no_result'
                    bf_df.loc[idx,'cid'] = driver.find_element(By.CSS_SELECTOR, "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute('data-cid')
                    bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.
                    time.sleep(1)
                except Exception as e2:
                    print(f'e2:{e2}')
                    bf_df.loc[idx,'cid'] = np.nan
                    bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.
                    time.sleep(1)
            else:
                print(f'e1: {e1}')
        # if idx == 30:
            # break


driver.quit()

# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다

# df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url']


# URL이 수집되지 않은 데이터는 제거합니다.
# df = df.loc[~df['naver_map_url'].isnull()]