'''
https://developers.kakao.com/docs/latest/ko/local/dev-guide 링크 참조.
'''

import pandas as pd
import requests

# 재료가 되는 행렬 사용.
csv_df = pd.read_csv('bf_data_60pg.csv')
coors = csv_df[['spotLng', 'spotLat']]
print(coors, sep='\n')

# 가져와서 1줄씩 돌리기
locations = []
i = 0
for lng, lat in coors.iterrows():
    print(f'{i}시도의 재료, {lng}/{lat}')
    # x = 127.1086228
    url = f'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={lng}&y={lat}'
    
    headers = {
    ## 여러분의 카카오 API의 REST API키를 아래 예시와 같이 입력해주세요
    ## "Authorization": "KakaoAK REST API키 입력 gogo"}
    # "Authorization": "KakaoAK f64acb1ae8c66asdfasefasfasdfadsf"}
    "Authorization": "KakaoAK 1da7b3747e086ab039713b8c280ee6d5"}

    # place = requests.get(url, headers = headers).json()['documents']
    place = requests.get(url, headers = headers).json()
    print(f'{i}번째 라인/ {place}')
    locations.append(place)
    i += 1
    
    # 10줄만 돌려보자.
    if i == 10:
        break