import requests
import json
import os
import pandas as pd

excel_file = 'result.xlsx'
df = pd.read_excel(excel_file)


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
                },

                'sfInfos': sfInfos
            }

            file_path = './duck.jpeg'
            img_file = open(file_path, 'rb')

            # form-data 만들기
            form_data = {
                "spotDto": (None, json.dumps(body_dict, ensure_ascii=False), "application/json"),
                "spotImages": (file_path.split("/")[-1], img_file, "image/jpeg")
            }

            url = 'http://192.168.31.134:8080/api/spot/save'

            res2 = requests.post(url, files=form_data)

        print(res2)

    except Exception as e:
        print(e)


handleSubmit()
