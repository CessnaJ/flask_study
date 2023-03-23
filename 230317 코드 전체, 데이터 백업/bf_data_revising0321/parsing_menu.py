# 메뉴, 가격 dict로 묶어서 저장하자. 아래 코드 수정하면 됨.

from bs4 import BeautifulSoup
import pandas as pd
import json

excel_file = 'sfInfo_parsed0323.xlsx'

df = pd.read_excel(excel_file)


try:
    # 각 행 순회하기
    for i, row in df.iterrows():
        
        if type(row["user_reviews"]) == float:
            review_dict = ''

        elif len(row["user_reviews"]) > 3:
            item = row['user_reviews']
            # json_items = json.loads(item)
            

            soup = BeautifulSoup(item, 'html.parser')
            review_arr = [div.text for div in soup.find_all('div', {'class': 'rg88i'})]
            # print(review_arr)
            nickname_arr = [span.text for span in soup.find_all('span', {'class': 'zPfVt'})]
            # print(nickname_arr)
            
            review_dict = dict(zip(review_arr, nickname_arr))

        else:
            review_dict = {}


        # sfiInfo 필드값 덮어쓰기
        row["user_reviews"] = review_dict

        # 수정된 행 다시 저장. title값이 최종본이 됨.
        df.loc[i] = row


        # if i > 10:
            # break

    # 결과 데이터프레임을 csv 파일로 저장하기
    df.to_csv("result.csv", index=True)
    df.to_excel("result.xlsx", index=True)

except Exception as e1:
    print(e1)
    print(i)



배민 연동된 카드형 메뉴
<div class="MENyI">아보카도 쉬림프 샐러드</div>
<div class="gl2cc">18,500원</div>


일반 메뉴로 추측
<a class="place_bluelink ihmWt" href="https://m.booking.naver.com/order/bizes/310889/items/3339905/menus/2432100?theme=place&amp;refererCode=menutab&amp;service-target=map-pc&amp;area=bmp" role="button" target="_blank">에스프레소</a>
<em class="awlpp">3,000원</em>

네이버 예약?
<div class="MENyI">(R)콜드브루 아메리카노</div>
<div class="gl2cc">4,800원</div>

47행부터 다시 체크