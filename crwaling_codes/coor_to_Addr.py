'''
https://developers.kakao.com/docs/latest/ko/local/dev-guide 링크 참조.
'''

import pandas as pd
import requests

# 재료가 되는 행렬 사용. csv_df는 불러온 임시데이터. 따로 저장을 해야 반영됨.
csv_df = pd.read_csv('bf_data_60pg.csv')
coors = csv_df[['spotLng', 'spotLat']]
print(coors, sep='\n')


# 행 추가
csv_df['streetAddr'] = ""
csv_df['addr_dong'] = ""


# 가져와서 1줄씩 돌리기
locations = []

for idx, row in coors.iterrows():
    lng, lat = row['spotLng'], row['spotLat']
    print(f'{idx}번 시도의 재료, lng:{lng}/lat:{lat}')
    # x = 127.1086228
    # url = f'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={lng}&y={lat}'
    url = f'https://dapi.kakao.com/v2/local/geo/coord2address.json?x={lng}&y={lat}&input_coord=WGS84'
    print(f'url: {url}')
    
    headers = {
    ## 여러분의 카카오 API의 REST API키를 아래 예시와 같이 입력해주세요
    ## "Authorization": "KakaoAK REST API키 입력 gogo"}
    # "Authorization": "KakaoAK f64acb1ae8c66asdfasefasfasdfadsf"}
    "Authorization": "KakaoAK 1da7b3747e086ab039713b8c280ee6d5"}

    # place = requests.get(url, headers = headers).json()['documents']
    place = requests.get(url, headers = headers).json()

    if place['documents'][0]['road_address']: # 도로명 주소 존재시?
        csv_df.at[idx, 'streetAddr'] = place['documents'][0]['address']['region_3depth_name']
        csv_df.at[idx, 'addr_dong'] = place['documents'][0]['road_address']['address_name']
        
    else:
        pass

csv_df.to_csv('modified_data.csv', index=False)

