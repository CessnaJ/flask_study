# 일부 누락되고 있는데 이유 찾아야함.


# 메뉴, 가격 dict로 묶어서 저장하자. 아래 코드 수정하면 됨.
from bs4 import BeautifulSoup
import pandas as pd
import json
import numpy as np

excel_file = 'menu_parsed0324.xlsx'

df = pd.read_excel(excel_file)


# 메뉴 아이템 가져옴.
# 두번 다 돌려봄
# 둘중에 긴거 선택해서 저장.
# 태그가 있는거, 아예 데이터가 없는거, 빈 리스트 있는거 나눠서 관리. 빈 리스트는 빈 리스트 그대로 넣어주고, 아예 아무것도 없는거는 아무것도 없는거 그대로..
from bs4 import BeautifulSoup


def mapping_working_hour(soup):
    try:
        res_dict = {}
        for div in soup.find_all('div', class_='w9QyJ')[1:]:
            day = div.find('span', class_='i8cJw').text
            hours = [x.strip() for x in div.find('div', class_='H3ua4').stripped_strings]
            res_dict[day] = hours

        return res_dict

    except Exception as e1:
        # error_handler_mapping(soup)

        # print(e1)
        # print(f'soup: {soup}')
        # print(*soup)
        # print('idx:',i)
        return soup


def error_handler_mapping(soup):
    try:
        res_dict = {}
        for div in soup.find_all('div', class_='w9QyJ')[1:]:
            
            date_str = div.find('span', class_='i8cJw').text
            if date_str:
                print(date_str)
            # span
            # H3ua4
            print(div)
            hours = [x.strip() for x in div.find('span', class_='H3ua4')]
            # if hours:
            print('asd', hours)

            res_dict[date_str] = time_list

    except Exception as e2:
        print('e2')
        print(e2)



def parse_open_hour(i, row):
    item = row["naver_open_hours"]
    
    if pd.isnull(item): # 아예 빈값은 float type으로
        return item
    elif item == '[]':
        return item
    else:
        soup = BeautifulSoup(item, 'html.parser')       
        working_hour_dict = mapping_working_hour(soup)
        
        return working_hour_dict
        # return menu_dict1 if len(menu_dict1) > len(menu_dict2) else menu_dict2
        





try:
    # 각 행 순회하기
    for i, row in df.iterrows():
        # sfiInfo 필드값 덮어쓰기
        row["naver_open_hours"] = parse_open_hour(i, row)
        # 수정된 행 다시 저장. menu dict가 최종본이 됨.
        print(1)
        df.loc[i] = row

    # 결과 데이터프레임을 csv 파일로 저장하기
    df.to_csv("result.csv", index=True)
    df.to_excel("result.xlsx", index=True)

except Exception as e1:
    print(e1)
    print(i)