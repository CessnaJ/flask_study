import requests
import csv
import pandas as pd
import json


'''
요청형식.
http://bfzido.org/rest/web/v1/spot/spots/
093992dd9d7af1b702334b15befb99e920180511095358
?restApiKey=gcf703504d5556d38602b1e89db1257d
'''


def fetching_data(idx, pk, cid, new_df):
    req_url = f'http://bfzido.org/rest/web/v1/spot/spots/{pk}?restApiKey=gcf703504d5556d38602b1e89db1257d'
    res_json = requests.get(req_url)
    imgs = res_json.spotMainImageDataInfo

    # 이미지 정보를 순회하면서 파일 다운로드 받는 로직
    for img_info in imgs:
        img_res = requests.get(img_info.spotAwsS3ImageFullUrl)
        img_idx = requests.get(img_info.spotAwsS3ImageSortNum)
        # 이미지를 파일로 만드는 함수.(베프지도 pk)
        with open(f'img_{pk}_{img_idx}.jpg', 'wb') as f:
            f.write(img_res.content)
        
        # 이미지를 파일로 만드는 로직.(네이버 cid )
        with open(f'img_{cid}_{img_idx}.jpg', 'wb') as f2:
            f2.write(img_res.content)

    # 시설정보를 순회하면서 csv에 추가하는 로직
    facility_infos = res_json.spotFacilitiesDataInfo

    # 그냥 순회하지말고 이거는 그냥 그대로 넣자. 가공 나중에 해도 됨.
    '''
    for facility_info in facility_infos:
        pass
    '''
    








# CSV 파일을 DataFrame 객체로 불러오기
csv_file = './fetching_cid_sid_title.csv'
bf_df = pd.read_csv(csv_file)

with open('bf_data_60pg.csv', 'a', encoding='utf-8', newline='') as csvfile:
    start = 0
    count = 50
    
    for idx, row in bf_df[['sid', 'cid']].iterrows():


    if idx == 0:
                    bf_df.iloc[[idx]].to_csv(new_csv, header=True, index=False)
                else:
                    bf_df.iloc[[idx]].to_csv(new_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.
                
                continue
    
    
    writer = csv.writer(csvfile)
    field_arr = ['spotSeq',
    'spotRate',
    'spotAveragePoint',
    'spotName',
    'spotCategory',
    'spotLat',
    'spotLng',
    'spotZipcode',
    'spotAddress',
    'spotBuildingName',
    'spotPlaceId',
    'spotOpenDays',
    'spotCloseDays',
    'spotRunTimesMemo',
    'spotTelNumber', 
    'spotRegLang', 
    'spotIsViewEnabled', 
    'spotViewCount', 
    'soptRegUserId',
    'spotRegLoginRouteType',
    'spotRegDatetime',
    'totalSpotPointCommentsCount', 
    'totalCurrentSpotFavoritesCount', 
    'sfiInfo']

    # CSV 파일에 헤더를 작성
    # writer.writerow(['name', 'address', 'lat', 'lng', 'rate', 'image_url'])
    # JSON 데이터를 파싱하여 CSV 파일에 작성
    writer.writerow(field_arr)
    rows = []
    for _ in range(60):
        url = f'http://bfzido.org/rest/web/v1/spot/spots?restApiKey=gcf703504d5556d38602b1e89db1257d&queryType=list&orderBy=rate&offset={start}&limit={count}&searchInfo=spot_name like 대전 or spot_address like 대전'
        res = requests.get(url) # 첫번째 요청
        json_data = res.json()

        for spot in json_data['dataList']:
            temp = []
            for field in field_arr:
                temp.append(spot[field])
            writer.writerow(temp)
        
        start += 50
            
# http://bfzido.org/rest/web/v1/spot/dftSpotSettingInfo?restApiKey=gcf703504d5556d38602b1e89db1257d
    
    