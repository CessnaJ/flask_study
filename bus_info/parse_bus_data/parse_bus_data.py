import requests
import xmltodict
import pandas as pd

df = pd.DataFrame(columns=['BUS_TYPE', 'CAR_REG_NO', 'ROUTE_CD'])

excel_idx = 0
for page in range(1, 373):
    service_key = "yfzRro1BbzFgxTncMEUf3K1z%2FDBImnHc0De3Xze7N1H%2FnLRvFZgqSQRfLodifiRmeVc3Git8rZehejUpkB%2BSkw%3D%3D" # 영록님꺼
    service_key = "C9z58j3DHtsZw5I9cnrhloQo11QBrDQ05LYrSPVUc12zxYjlWK6jr6ALUqoNbQwMEyb3CToq5tMgaaa4rqlFcg%3D%3D" # 내꺼
    url = f'http://openapitraffic.daejeon.go.kr/api/rest/busreginfo/getBusRegInfoAll?serviceKey={service_key}&reqPage={page}'
    
    res = requests.get(url)
    print(type(res.content))
    print(res)
    print(res.content)
    bus_dict_list = xmltodict.parse(res.content).get('ServiceResult').get('msgBody').get('itemList')

    for idx, dict_item in enumerate(bus_dict_list):
        print(dict_item)
        
        bus_type = dict_item.get('BUS_TYPE')
        # car_reg_no = dict_item.get('CAR_REG_NO').encode('utf-8').decode('unicode-escape')
        car_reg_no = dict_item.get('CAR_REG_NO')
        route_cd = dict_item.get('ROUTE_CD')
        
        print(bus_type)
        print(car_reg_no)
        print(route_cd)
        # car_reg_no = dict_item.get('CAR_REG_NO').decode('unicode-escape')
        # print(car_reg_no)
        # print(type(car_reg_no))
        
        if bus_type =='2':
            df.loc[excel_idx] = [bus_type, car_reg_no, route_cd]
            excel_idx += 1
        # car_reg_no.decode('utf-8')
    print(bus_dict_list[:10])
    
    if page >1:
        break
        
# 엑셀 파일로 저장
df.to_excel('output.xlsx', index=True)