
import requests
import json
import os
import pandas as pd
import math

excel_file = 'pre_processing_complete_data.xlsx'
df = pd.read_excel(excel_file)

# DataFrame의 각 행을 반복합니다.
for i, row in df.iterrows():
    if not pd.isnull(row['sfiInfo']) and not pd.isnull(row['union_spotsfs']):
        sfinfo = eval(row['sfiInfo'])
        union_sfinfo = eval(row['union_spotsfs'])

        # sfiInfo 업데이트
        if len(union_sfinfo) > len(sfinfo):
            df.at[i, 'sfiInfo'] = json.dumps(union_sfinfo)  # 데이터를 JSON 문자열로 변환합니다.
        else:
            df.at[i, 'sfiInfo'] = json.dumps(sfinfo)  # 데이터를 JSON 문자열로 변환합니다.
    else:
        print(f"Skipping row {i} due to missing values.")

# 결과를 새 Excel 파일에 저장합니다.
df.to_excel('updated_pre_processing_complete_data.xlsx', index=False)
