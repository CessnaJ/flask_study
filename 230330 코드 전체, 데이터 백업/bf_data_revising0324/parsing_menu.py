# 메뉴, 가격 dict로 묶어서 저장하자. 아래 코드 수정하면 됨.
from bs4 import BeautifulSoup
import pandas as pd
import json
import numpy as np

excel_file = 'user_review_parsed0324.xlsx'

df = pd.read_excel(excel_file)


# 메뉴 아이템 가져옴.
# 두번 다 돌려봄
# 둘중에 긴거 선택해서 저장.
# 태그가 있는거, 아예 데이터가 없는거, 빈 리스트 있는거 나눠서 관리. 빈 리스트는 빈 리스트 그대로 넣어주고, 아예 아무것도 없는거는 아무것도 없는거 그대로..

def parse_menu(row):
    item = row["menu"]

    if pd.isnull(item): # 아예 빈값은 float type으로
        return item
    elif item == '{}':
        return item
    else:
        menu_dict1 = parsing_menu_type1(item)
        menu_dict2 = parsing_menu_type2(item)

        return menu_dict1 if len(menu_dict1) > len(menu_dict2) else menu_dict2
        


def parsing_menu_type1(html_item):
    try:
        soup = BeautifulSoup(html_item, 'html.parser')
        menu_arr = [a.text for a in soup.find_all('a', {'class': 'place_bluelink ihmWt'})]
        price_arr = [em.text for em in soup.find_all('em', {'class': 'awlpp'})]
        
        menu_dict = dict(zip(menu_arr, price_arr))
        return menu_dict


    except Exception as e1:
        return ""


def parsing_menu_type2(html_item):
    try:
        soup = BeautifulSoup(html_item, 'html.parser')
        menu_arr = [div1.text for div1 in soup.find_all('div', {'class': 'MENyI'})]
        price_arr = [div2.text for div2 in soup.find_all('div', {'class': 'gl2cc'})]
        
        menu_dict = dict(zip(menu_arr, price_arr))
        return menu_dict

    except Exception as e2:
        return ""



try:
    # 각 행 순회하기
    for i, row in df.iterrows():
        # sfiInfo 필드값 덮어쓰기
        row["menu"] = parse_menu(row)
        # 수정된 행 다시 저장. menu dict가 최종본이 됨.
        df.loc[i] = row

    # 결과 데이터프레임을 csv 파일로 저장하기
    df.to_csv("result.csv", index=True)
    df.to_excel("result.xlsx", index=True)

except Exception as e1:
    print(e1)
    print(i)



# 배민 연동된 카드형 메뉴
# <div class="MENyI">아보카도 쉬림프 샐러드</div>
# <div class="gl2cc">18,500원</div>


# 일반 메뉴로 추측
# <a class="place_bluelink ihmWt" href="https://m.booking.naver.com/order/bizes/310889/items/3339905/menus/2432100?theme=place&amp;refererCode=menutab&amp;service-target=map-pc&amp;area=bmp" role="button" target="_blank">에스프레소</a>
# <em class="awlpp">3,000원</em>

# 네이버 예약?
# <div class="MENyI">(R)콜드브루 아메리카노</div>
# <div class="gl2cc">4,800원</div>

# 47행부터 다시 체크
# a태그 class="place_bluelink ihmWt"
# <em class="awlpp">4,500원</em>