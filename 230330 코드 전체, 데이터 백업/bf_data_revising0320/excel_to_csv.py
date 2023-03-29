import pandas as pd



# xlsx 파일 경로
xlsx_file = 'detail_info_added (version 1).xlsx'

# CSV 파일 경로와 파일 이름 지정
csv_file = xlsx_file[:-5]+'.csv'

print(csv_file)

# xlsx 파일 읽기
df = pd.read_excel(xlsx_file)

'''
# CSV 파일을 DataFrame 객체로 불러오기
df = pd.read_csv(csv_file, encoding='utf-8')
'''




'''
# Excel 파일로 저장하기
excel_file = f'{csv_file[:-4]}.xlsx'
df.to_excel(excel_file, index=False)
'''

# csv 파일로 저장
df.to_csv(csv_file, index=True)






