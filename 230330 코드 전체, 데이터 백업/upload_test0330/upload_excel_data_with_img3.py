import requests
import json
import os
import pandas as pd

excel_file = 'pre_processing_complete_data.xlsx'
df = pd.read_excel(excel_file)

def get_image_files(row):
    related_pk = eval(row['related_pk'])
    img_files = []
    img_folder_path = './imgs/'

    if related_pk == []:
        pk = row['pk']
        index = 0
        while True:
            file_name = f'img_spotSeq_{pk}_{index}.jpg'
            file_path = os.path.join(img_folder_path, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as img_file:
                    # img_files.append(('spotImages', img_file.read(), file_name))
                    img_files.append(('spotImages', (file_name, img_file.read(), 'image/jpeg')))

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
                        # img_files.append(('spotImages', img_file.read(), file_name))
                        img_files.append(('spotImages', (file_name, img_file.read(), 'image/jpeg')))

                    index += 1
                else:
                    break
    return img_files

def handleSubmit():
    # try:
        for i, row in df.iterrows():
            if i > 0:
                break

            sfInfos = eval(row['sfiInfo'])
            # union_sfinfo = eval(row['union_spotsfs'])

            # if len(union_sfinfo) > len(sfinfo):
            #     sfInfos = union_sfinfo
            # else:
            #     sfInfos = sfinfo

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

            form_data = [
                ("spotDto", (None, json.dumps(body_dict, ensure_ascii=False), "application/json")),
                *img_files,
            ]
            # form_data = [
            #     ("spotDto", (None, json.dumps(body_dict, ensure_ascii=False), "application/json")),
            #     ("spotImages", (None, *img_files, "image/jpeg"))
            # ]

            url = 'http://192.168.31.134:8080/api/spot/save'

            res2 = requests.post(url, files=form_data)

        print(res2)

    # except Exception as e:
    #     print(e)

handleSubmit()
