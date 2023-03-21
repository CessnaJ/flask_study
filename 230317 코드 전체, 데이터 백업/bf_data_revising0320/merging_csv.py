import pandas as pd


# CSV 파일 경로와 파일 이름 지정
base_csv = 'detail_info_added (version 1).csv' # row의 개수가 다 있음.
aux_csv = 'fetching_rating_data.csv' # 쳐내졌음.

# df로 불러오기
base_df = pd.read_csv(base_csv, encoding='utf-8')
aux_df = pd.read_csv(aux_csv, encoding='utf-8')

# 새 필드들 추가
base_df["naver_search_id"] = "" # aux_df는 naver_serach_id로 오타났음.
base_df["cid_sid_equals"] = ""
base_df["naver_rating_score"] = ""
base_df["naver_rating_count"] = ""
base_df["naver_place_title"] = ""
base_df["card_review_json"] = ""


# aux_df에서 필요한 column들만 추출하여 새로운 DataFrame 생성
aux_df_subset = aux_df[["spotSeq", "naver_serach_id", "cid_sid_equals", "naver_rating_score", "naver_rating_count", "naver_place_title", "card_review_json"]]

# base_df의 각 row에 대해 반복문 실행
for i, row in base_df.iterrows():
    # aux_df_subset에서 pk 값이 현재 row의 pk와 같은 행을 찾음
    matching_row = aux_df_subset.loc[aux_df_subset["spotSeq"] == row["spotSeq"]]
    
    # 만약 찾은 행이 있다면, 값을 대입함
    if not matching_row.empty:
        base_df.at[i, "naver_search_id"] = matching_row["naver_serach_id"].iloc[0]
        base_df.at[i, "cid_sid_equals"] = matching_row["cid_sid_equals"].iloc[0]
        base_df.at[i, "naver_rating_score"] = matching_row["naver_rating_score"].iloc[0]
        base_df.at[i, "naver_rating_count"] = matching_row["naver_rating_count"].iloc[0]
        base_df.at[i, "naver_place_title"] = matching_row["naver_place_title"].iloc[0]
        base_df.at[i, "card_review_json"] = matching_row["card_review_json"].iloc[0]


csv_file = 'merged.csv'
# csv 파일로 저장
base_df.to_csv(csv_file, index=True)






