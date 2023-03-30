import requests
import xmltodict
import pandas as pd

df = pd.DataFrame(columns=['BUS_TYPE', 'CAR_REG_NO'])

excel_idx = 0
for page in range(1, 373):
    service_key = "yfzRro1BbzFgxTncMEUf3K1z%2FDBImnHc0De3Xze7N1H%2FnLRvFZgqSQRfLodifiRmeVc3Git8rZehejUpkB%2BSkw%3D%3D"
    url = f'http://openapitraffic.daejeon.go.kr/api/rest/busreginfo/getBusRegInfoAll?serviceKey={service_key}&reqPage={page}'
    res = requests.get(url)
    print(type(res.content))
    bus_dict_list = xmltodict.parse(res.content).get('ServiceResult').get('msgBody').get('itemList')

    for idx, dict_item in enumerate(bus_dict_list):
        bus_type = dict_item.get('BUS_TYPE')
        # car_reg_no = dict_item.get('CAR_REG_NO').encode('utf-8').decode('unicode-escape')
        car_reg_no = dict_item.get('CAR_REG_NO')
        # car_reg_no = dict_item.get('CAR_REG_NO').decode('unicode-escape')
        # print(car_reg_no)
        # print(type(car_reg_no))
        
        if bus_type =='2':
            df.loc[excel_idx] = [bus_type, car_reg_no]
            excel_idx += 1
        # car_reg_no.decode('utf-8')
    
    # if page >5:
        # break
        
# 엑셀 파일로 저장
df.to_excel('output.xlsx', index=True)