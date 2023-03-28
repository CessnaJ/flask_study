import pandas as pd
import json

excel_file = 'pk_restored.xlsx'
df = pd.read_excel(excel_file)



arr = []
matching_dict = {}


df['related_pk'] = ""
df['related_idx'] = ""
df['union_spotsfs'] = ""
# temp = 0
# 각 행 순회하기
for i, base_row in df.iterrows():
    base_df_name = base_row['spotName']


    related_pk_arr = []
    related_idx_arr = []
    union_spotsfs = []

    for j, row in df.iterrows():
        if base_df_name == row['spotName']:
            related_pk_arr.append(row['pk'])
            related_idx_arr.append(row['Unnamed: 0'])
            union_spotsfs += eval(row['sfiInfo'])
            # union_spotsfs.union(eval(row['sfiInfo']))
            
            # print(type(eval(row['sfiInfo'])))
            # print(j)
            # print(union_spotsfs)
            # print(sorted(list(set(union_spotsfs))))
            # print(set(list(row['sfiInfo'])))
            # print(type(set(list(row['sfiInfo']))))

    if len(related_pk_arr) == 1:
        related_pk_arr = []
    if len(related_idx_arr) == 1:
        related_idx_arr = []

    df.at[i, 'related_pk'] = related_pk_arr
    df.at[i, 'related_idx'] = related_idx_arr
    df.at[i, 'union_spotsfs'] = sorted(list(set(union_spotsfs)))
    
    # if i >30:
        # break
        # if j < temp: # 이전에 답이 나온 index를 저장해두고 거기서부터 다시 시작하는 dp
        #     continue

        # pk_df_name = pk_row['spotName']
        # if df_name == pk_df_name:
        #     df.at[i, 'pk'] = pk_df.at[j, 'spotSeq']
        #     temp = j

        #     break

            
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

