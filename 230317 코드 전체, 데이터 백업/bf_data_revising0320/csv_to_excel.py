import pandas as pd

# csv파일경로
csv_file = 'tel_review_added.csv'

# csv 파일 읽기
df = pd.read_csv(csv_file)

# Excel 파일로 저장하기
excel_file = f'{csv_file[:-4]}.xlsx'
df.to_excel(excel_file, index=True)