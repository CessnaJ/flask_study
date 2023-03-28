import pandas as pd
import json

excel_file = 'delete_dup_by_name.xlsx'
df = pd.read_excel(excel_file)

pk_excel_file = 'merged.xlsx'
pk_df = pd.read_excel(pk_excel_file)


arr = []
matching_dict = {}
# 각 행 순회하기
for i, row in df.iterrows():
    df_name = row['spotName']

    for j, pk_row in pk_df.iterrows():
        pk_df_name = pk_row['spotName']
        if df_name == pk_df_name:
            df.at[i, 'pk'] = pk_df.at[j, 'spotSeq']
            matching_dict[i].append(j)

            break

            
            # if abs(i - j) > 3:
            # print(i,':', j, 'matched', df_lat, pk_df_lat, '/', df_lng, pk_df_lng)
        
    

    # if i > 300:
    #     break
# print(arr[-1])
# print(len(arr))

    # if pd.notnull(row["sfiInfo"]):
#     if len(row["sfiInfo"]) > 3:
#         item = row['sfiInfo']
#         json_items = json.loads(item)

#         arr = []
#         for dict_item in json_items:
#             converted_sfInfo = sfInfo_dict.get(dict_item.get('sfsSeq'))
#             if converted_sfInfo:
#                 arr.append(converted_sfInfo)
        
#         arr.sort()

#     else:
#         arr = [1]
    

#     # sfiInfo 필드값 덮어쓰기
#     row["sfiInfo"] = arr

#     # 수정된 행 다시 저장. title값이 최종본이 됨.
#     df.loc[i] = row

# 결과 데이터프레임을 csv 파일로 저장하기
# df.to_csv("result.csv", index=True)
df.to_excel("result.xlsx", index=True)

