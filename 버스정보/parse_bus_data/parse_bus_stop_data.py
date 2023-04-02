import requests
import xmltodict
import pandas as pd

df = pd.DataFrame(columns=['ARO_BUSSTOP_ID', 'BUSSTOP_ENG_NM', 'BUSSTOP_NM', 'BUS_NODE_ID', 'GPS_LATI', 'GPS_LONG', 'ROAD_NM', 'ROAD_NM_ADDR', 'ROUTE_NO'])

excel_idx = 0
# for page in range(1, 373):
# service_key = "yfzRro1BbzFgxTncMEUf3K1z%2FDBImnHc0De3Xze7N1H%2FnLRvFZgqSQRfLodifiRmeVc3Git8rZehejUpkB%2BSkw%3D%3D" # 영록님꺼
service_key = "C9z58j3DHtsZw5I9cnrhloQo11QBrDQ05LYrSPVUc12zxYjlWK6jr6ALUqoNbQwMEyb3CToq5tMgaaa4rqlFcg%3D%3D" # 내꺼
    # url = f'http://openapitraffic.daejeon.go.kr/api/rest/busreginfo/getBusRegInfoAll?serviceKey={service_key}&reqPage={page}'


#트러블슛 테스트
# test_url = 'http://openapitraffic.daejeon.go.kr/api/rest/stationinfo/getStationByUid?arsId=32350&serviceKey=C9z58j3DHtsZw5I9cnrhloQo11QBrDQ05LYrSPVUc12zxYjlWK6jr6ALUqoNbQwMEyb3CToq5tMgaaa4rqlFcg%3D%3D'
# test_res = requests.get(test_url)
# test_dict = xmltodict.parse(test_res.content).get('ServiceResult').get('msgBody').get('itemList')
# print(test_dict)


    
excel_idx = 1
for idx in range(10000, 100000, 10):
        try:    
            print(f'try : {idx}')

            url2 = f'http://openapitraffic.daejeon.go.kr/api/rest/stationinfo/getStationByUid?arsId={idx}&serviceKey={service_key}'
            # http://openapitraffic.daejeon.go.kr/api/rest/stationinfo/getStationByUid?arsId=32350&serviceKey=서비스키
            
            res = requests.get(url2)
            # print(type(res.content))
            # print(res.content)
            bus_stop_dict = xmltodict.parse(res.content).get('ServiceResult').get('msgBody').get('itemList')
            print(bus_stop_dict)


            ARO_BUSSTOP_ID = bus_stop_dict.get('ARO_BUSSTOP_ID')
            BUSSTOP_ENG_NM = bus_stop_dict.get('BUSSTOP_ENG_NM')
            BUSSTOP_NM = bus_stop_dict.get('BUSSTOP_NM')
            BUS_NODE_ID = bus_stop_dict.get('BUS_NODE_ID')
            GPS_LATI = bus_stop_dict.get('GPS_LATI')
            GPS_LONG = bus_stop_dict.get('GPS_LONG')
            ROAD_NM = bus_stop_dict.get('ROAD_NM')
            ROAD_NM_ADDR = bus_stop_dict.get('ROAD_NM_ADDR')
            ROUTE_NO = bus_stop_dict.get('ROUTE_NO')
            
            if ARO_BUSSTOP_ID:
                df.loc[excel_idx] = [ARO_BUSSTOP_ID, BUSSTOP_ENG_NM, BUSSTOP_NM, BUS_NODE_ID, GPS_LATI, GPS_LONG, ROAD_NM, ROAD_NM_ADDR, ROUTE_NO]
                print(excel_idx)
                excel_idx += 1

            # if excel_idx > 100:
                #  break
        # for idx, dict_item in enumerate(bus_dict_list):
        #     bus_type = dict_item.get('BUS_TYPE')
            
        #     car_reg_no = dict_item.get('CAR_REG_NO')
            
        #     if bus_type =='2':
        #         df.loc[excel_idx] = [bus_type, car_reg_no]
        #         excel_idx += 1
        
        
        # if page >5:
            # break
        except Exception as e:
            print(e)

# 엑셀 파일로 저장
df.to_excel('bus_stop.xlsx', index=True)