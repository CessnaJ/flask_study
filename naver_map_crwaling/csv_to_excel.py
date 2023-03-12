import pandas as pd

# CSV 파일 경로와 파일 이름 지정
csv_file = 'fetching_cid_sid_title.csv'

# CSV 파일을 DataFrame 객체로 불러오기
df = pd.read_csv(csv_file, encoding='utf-8')

# Excel 파일로 저장하기
excel_file = f'{csv_file[:-4]}.xlsx'
df.to_excel(excel_file, index=False)