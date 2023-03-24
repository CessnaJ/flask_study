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