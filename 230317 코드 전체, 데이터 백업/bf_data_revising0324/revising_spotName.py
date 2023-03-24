import pandas as pd

excel_file = 'bf_data_spotName_revised0321.xlsx'

df = pd.read_excel(excel_file)



# 각 행 순회하기
for i, row in df.iterrows():
    # naver_place_title에 값이 있는 경우
    if pd.notnull(row["naver_place_title"]):
        # title 필드값 덮어쓰기
        row["title"] = row["naver_place_title"]
        # title 값이 비어있으면 spotName 필드값으로 덮어쓰기
        if pd.isnull(row["title"]):
            row["title"] = row["spotName"]
    # 수정된 행 다시 저장. title값이 최종본이 됨.
    df.loc[i] = row

# 결과 데이터프레임을 csv 파일로 저장하기
df.to_csv("result.csv", index=True)
df.to_excel("result.xlsx", index=True)

