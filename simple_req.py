import requests
import csv



# print(json_data)

with open('bf_data_test.csv', 'w', encoding='utf-8', newline='') as csvfile:
    start = 250
    count = 50
    
    
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
    for _ in range(3):
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
    
    