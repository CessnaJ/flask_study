import pandas as pd
import json

excel_file = 'before_processing.xlsx'

df = pd.read_excel(excel_file)

# 첫 번째 행은 이전 행이 없으므로 건너뜀
to_drop = []
for i in range(1, len(df)):
    # 현재 행과 이전 행의 spotLat, spotLng 값을 비교하여 같으면 해당 행 삭제
    # if df.loc[i, 'spotLat'] == df.loc[i-1, 'spotLat'] and df.loc[i, 'spotLng'] == df.loc[i-1, 'spotLng']:
    if df.loc[i, 'spotName'] == df.loc[i-1, 'spotName']:
        to_drop.append(i)

# 인덱스가 꼬이지 않도록, 삭제할 행의 인덱스를 한 번에 삭제
print(to_drop)
print(len(to_drop))
df.drop(to_drop, inplace=True)


# 결과 데이터프레임을 csv 파일로 저장하기
# df.to_csv("result.csv", index=True)
df.to_excel("result.xlsx", index=True)

