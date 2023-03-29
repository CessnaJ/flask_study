import pandas as pd
import json

excel_file = 'bf_data_0321.xlsx'

df = pd.read_excel(excel_file)

for i, row in df.iterrows():
    # naver_place_title에 값이 있는 경우
    # if row["sfiInfo"] == '[]':
        # arr = [1]

    # if pd.notnull(row["sfiInfo"]):
    if len(row["sfiInfo"]) > 3:
        item = row['sfiInfo']
        json_items = json.loads(item)

        arr = []
        for dict_item in json_items:
            converted_sfInfo = sfInfo_dict.get(dict_item.get('sfsSeq'))
            if converted_sfInfo:
                arr.append(converted_sfInfo)
        
        arr.sort()

    else:
        arr = [1]
    

    # sfiInfo 필드값 덮어쓰기
    row["sfiInfo"] = arr

    # 수정된 행 다시 저장. title값이 최종본이 됨.
    df.loc[i] = row

# 결과 데이터프레임을 csv 파일로 저장하기
df.to_csv("result.csv", index=True)
df.to_excel("result.xlsx", index=True)

