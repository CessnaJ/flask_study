import pandas as pd
import json
import re

excel_file = 'result.xlsx'
df = pd.read_excel(excel_file)

for i, row in df.iterrows():
    # naver_rating_score 필드 정제
    naver_rating_score = row['naver_rating_score']
    
    if isinstance(naver_rating_score, str):
        score_match = re.search(r'\d+(\.\d+)?', naver_rating_score)
        if score_match:
            df.at[i, 'naver_rating_score'] = float(score_match.group())

    # naver_rating_count 필드 정제
    naver_rating_count = row['naver_rating_count']
    
    if isinstance(naver_rating_count, str):
        if naver_rating_count == 'no_rating':
            df.at[i, 'naver_rating_count'] = None
        else:
            count_match = re.search(r'\d+(\.\d+)?', naver_rating_count)
            if count_match:
                df.at[i, 'naver_rating_count'] = float(count_match.group())

# 정제
df.to_excel("pre_processing_complete.xlsx", index=True)
