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
csv_file = './fetching_cid_sid_title.csv'

# CSV 파일을 DataFrame 객체로 불러오기
bf_df = pd.read_csv(csv_file)

# 검색어 재료가 될 keyword
cid = 'cid'
sid = 'sid'

# 행 추가 - 새로운 필드를 추가함.
bf_df['naver_serach_id'] = ""#!
bf_df['cid_sid_equals'] = "" #!
bf_df['naver_rating_score'] = ""#!
bf_df['naver_rating_count'] = ""#
bf_df['naver_place_title'] = ""#!
bf_df['card_review_json'] = ""#


def getting_rating_count(html_soup):
    if html_soup is None:
        return "no_html"
    
    # 😀 여기 에러
    soup = BeautifulSoup(html_soup, 'html.parser')
    rating_spans = soup.find_all('span', {'class': 'm7jAR'})
    # print(type(rating_spans))
    # print(*rating_spans, sep='\n\n')
    
    ratings = []
    for idx, span in enumerate(rating_spans):
        # print(f'{idx}번 순회합니다.')
        # print(span)
        # rating_text = span.contents[-1].strip()  # "(424명 참여)"
        rating_text = span.get_text()
        if len(rating_text) <= 4:
            continue
        else:
            rating = rating_text.split()[-2][1:-1]  # "424"
            # print(f'rating: {rating}')
            ratings.append(rating)
    return ratings


def to_search_iframe(driver):
    driver.switch_to.default_content() # 기본 프레임으로 일단 커서 옮기기. - 추후 iframe전환
    # driver.switch_to.frame('searchIframe')
    # 경로 맞는지 확인 필요.
    # frame_in = driver.find_element(By.XPATH, '/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')
    print('이제 프레임으로 들어가!')
    # frame_in = driver.find_element(By.XPATH, '//*[@id="_title"]/span[1]')
    print(1)
    # driver.switch_to.frame(frame_in)
    driver.switch_to.frame('entryIframe')
    print(2)


def element_content_as_dict(li_elements):
    reviews = []  # 리뷰를 저장할 리스트 초기화
    for li_element in li_elements:
        review_text = li_element.find_element(By.CSS_SELECTOR, "span.nWiXa").text  # 리뷰 텍스트 추출
        decoded_review = bytes(review_text, 'utf-8').decode('unicode_escape')
        korean_str = decoded_review.encode('utf-8').decode('unicode_escape')
        review_count = ''.join(filter(str.isdigit, li_element.find_element(By.CSS_SELECTOR, "span.TwM9q").text))  # 리뷰 카운트 추출
        
        review_dict = {decoded_review: review_count}  # 리뷰와 카운트를 딕셔너리로 저장
        reviews.append(review_dict)  # 딕셔너리를 리스트에 추가

    json_reviews = json.dumps(reviews)  # 리스트를 json 형태로 변환
    return json_reviews  # json 형태로 return


def regex_rating_count(text_val):
    '''
    txt 받아서 두번째 숫자 내뱉음.
    '''
    regex = r"\((\d+)명 참여\)"
    matches = re.search(regex, text_val)
    num = matches.group(1)
    return num


# 본격적 실행 시작.
with open('fetching_rating_data.csv', 'a', encoding='utf-8', newline='') as new_csv:
    for idx, row in bf_df[['sid', 'cid']].iterrows():
        print(f'{idx}번째 {row}으로 시행')
        # if idx == 10:
            # break
        if idx < 1322: # 1322번째부터 이어서 하기.
            continue

        if np.isnan(row['sid']): # 비어있으면
            continue  # 해당 행을 건너뜀

        sid = int(row['sid'])
        cid = int(row['cid'])
        # print(f'sid:{type(sid)}, cid:{type(cid)}')
        # print(sid, cid)
        # 일단 cid로 돌리고, 12개에 대해서는 직접 검증한다.
        
        # 'sid cid 같은지 조건 보고 field 채움.'
        if sid == cid:
            bf_df.loc[idx, 'cid_sid_equals'] = True
        else:
            bf_df.loc[idx, 'cid_sid_equals'] = False

        bf_df.loc[idx, 'naver_serach_id'] = cid
    # for idx, keyword in enumerate(bf_df[search_keyword].tolist()):
        # if idx <= 2160:
            # continue

        print("이번에 찾을 키워드 :", idx, f"/ {bf_df.shape[0] -1} 행", cid)
        writer = csv.writer(new_csv)
        try:
            naver_map_search_url = f"https://map.naver.com/v5/entry/place/{cid}?c=15,0,0,0,dh"
            driver.get(naver_map_search_url)
            time.sleep(random.choice([3]))
            to_search_iframe(driver)
            print('0')
            
            # 네이버 검색결과 title 따로 저장
            # place_title = driver.find_element(By.CSS_SELECTOR, '#_title > span.Fc1rA').text # 네이버 지도에 등록되어있는 이름 추출
            
            # wait = WebDriverWait(driver, 10)

            # place_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="_title"]/span[1]'))).text
            # place_title = driver.find_element(By.XPATH, '//*[@id="_title"]/span[1]').text # 네이버 지도에 등록되어있는 이름 추출
            # place_title = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]').text # 네이버 지도에 등록되어있는 이름 추출
            # place_title = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]'))).text
            place_title = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]').text
            print(place_title)
            print('1')
            bf_df.loc[idx, 'naver_place_title'] = place_title

            # 아래 에러 발생 가능. rating이 있는 장소인지? NoSuchElementException
            try:
                rating = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/em').text # 여기서 rating 추출
                # rating = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_section.OP4V8 > div.zD5Nm.f7aZ0 > div.dAsGb > span.PXMot.LXIwF > em').text # 여기서 rating 추출
                bf_df.loc[idx, 'naver_rating_score'] = rating
                print('별점 존재')
            except Exception:
                print(Exception)
                print('rating점수 받아오는데에서 문제- 네이버 장소 이름만 write하고 넘어갑니다.')
                bf_df.loc[idx, 'naver_rating_score'] = 'no_rating'
                
                if idx == 0:
                    bf_df.iloc[[idx]].to_csv(new_csv, header=True, index=False)
                else:
                    bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.
                
                continue
            
            
            # review_tab_click = driver.find_element(By.CSS_SELECTOR, '#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div > a:nth-child(1)').click() # 클릭
            # review_tab_click = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_fixed_maintab.place_stuck > div > div > div > div > a span:contains("리뷰")').click() # a태그의 자식인 span이 "리뷰"를 포함한 a태그를 선택.
            review_tab_click = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[contains(span/text(), "리뷰")]').click() # a태그의 자식인 span이 "리뷰"를 포함한 a태그를 클릭.
            print('클릭까지 완료')
            time.sleep(1) # 클릭을 해야 나옴.
            
            # 😀bs 이용해서 다시 시도.
            print('bs가져올거임.')
            html_source = driver.page_source
            # print(html_source)
            bf_df.loc[idx, 'naver_rating_count'] = getting_rating_count(html_source)

            # counting_element = driver.find_element(By.CSS_SELECTOR, "#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.no_margin.mdJ86 > div > div > div.Xj_yJ > span:nth-child(2)")
            # counting_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[7]/div[3]/div[1]/div/div/div[3]/span[2]')
            # val = counting_element.find_element(By.CSS_SELECTOR, "span").text
            # bf_df.loc[idx, 'naver_rating_count'] = regex_rating_count(val) # 몇명이 평가했는지 저장
            print('몇명인지 저장.')
            time.sleep(0.1)
            
            while True:
                time.sleep(1)
                try:
                    open_reviews_button = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[1]/div/div/div[2]/a')
                    if open_reviews_button.text == '접기':
                        break
                    else:
                        open_reviews_button.click()
                        print('창 넓히기 클릭 이벤트')
                except Exception:
                    break
            print(3)
            # li_elements = driver.find_elements(By.CSS_SELECTOR, "#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.no_margin.mdJ86 > div > div > div.k2tmh > ul > li")  # 모든 li 요소를 찾음
            li_elements = driver.find_elements(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[1]/div/div/div[2]/ul/li')  # 모든 li 요소를 찾음
            
            bf_df.loc[idx, 'card_review_json'] = element_content_as_dict(li_elements) # 카드정보 json으로 바꿔서 저장


            
            
            # 첫줄이면 헤드 넣고, 아니면 내용만 채우기
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