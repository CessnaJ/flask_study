import requests
import json
import os
import pandas as pd

excel_file = 'result.xlsx'
df = pd.read_excel(excel_file)


def get_image_files(row):
    related_pk = eval(row['related_pk'])
    img_files = []
    # 이미지 파일을 저장하는 폴더 경로입니다. 이 경로를 변경해 주세요.
    img_folder_path = './imgs/'

    if related_pk == []:
        pk = row['pk']
        index = 0
        while True:
            file_name = f'img_spotSeq_{pk}_{index}.jpg'
            file_path = os.path.join(img_folder_path, file_name)
            if os.path.exists(file_path):
                img_files.append((file_name, open(file_path, 'rb'), 'image/jpeg'))
                index += 1
            else:
                break
    else:
        for pk in related_pk:
            index = 0
            while True:
                file_name = f'img_spotSeq_{pk}_{index}.jpg'
                file_path = os.path.join(img_folder_path, file_name)
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as img_file:
                        img_files.append((file_name, img_file.read(), 'image/jpeg'))
                        index += 1
                else:
                    break
    return img_files


def handleSubmit():
    try:
        for i, row in df.iterrows():
            if i > 0:
                break

            sfinfo = eval(row['sfiInfo'])
            union_sfinfo = eval(row['union_spotsfs'])

            if len(union_sfinfo) > len(sfinfo):
                sfInfos = union_sfinfo
            else:
                sfInfos = sfinfo

            body_dict = {
                'spot': {
                    'spotName': row['spotName'],
                    'spotAddress': row['spotAddress'],
                    'spotBuildingName': row['spotBuildingName'],
                    'spotCategory': row['New_cat'],
                    'spotTelNumber': row['spotTel'],
                    'spotLat': row['spotLat'],
                    'spotLng': row['spotLng'],
                    'reviewRating': row['naver_rating_score'],
                    'reviewCount': row['naver_rating_count']
                },

                'sfInfos': sfInfos
            }

            img_files = get_image_files(row)

            # form-data 만들기
            form_data = {
                "spotDto": (None, json.dumps(body_dict, ensure_ascii=False), "application/json"),
            }

            # 이미지파일을 1개씩 매칭해야되는경우 😀
            for index, img_file in enumerate(img_files):
                form_data[f"spotImages[{index}]"] = img_file

            # 이미지 파일을 1개 key에 싸그리 넣어서 보내는 경우 😀 이 경우에는, 위에 있는 form_data 이렇게 다시 갱신함. 둘 중 하나 선택해서 보내야됨.
            form_data = {
                "spotDto": (None, json.dumps(body_dict, ensure_ascii=False), "application/json"),
                "spotImages": img_files
            }



            url = 'http://192.168.31.134:8080/api/spot/save'

            res2 = requests.post(url, files=form_data)

        print(res2)

    except Exception as e:
        print(e)


handleSubmit()
