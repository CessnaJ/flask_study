'''
요청형식.
http://bfzido.org/rest/web/v1/spot/spots/093992dd9d7af1b702334b15befb99e920180511095358?restApiKey=gcf703504d5556d38602b1e89db1257d

목적1. sfiInfo 업데이트
목적2. 사진파일 다운받고, 정보 담은json 매칭
'''
import requests
import csv
import pandas as pd
import json


def fetching_data(idx, pk, cid, df, new_csv):
    '''
    :param idx: pandas df의 idx (from csv)
    :param pk: request 보낼 bf지도 pk
    :param cid: 해당 df의 row에 매핑되어있는 네이버 cid
    :param df: df 수정하기 위해 변수로 받음
    :return: None
    '''
    req_url = f'http://bfzido.org/rest/web/v1/spot/spots/{pk}?restApiKey=gcf703504d5556d38602b1e89db1257d'
    res = requests.get(req_url)
    res_json = json.loads(res.content)
    print(res_json)
    
    # 이미지 자체가 없을수도 있음.
    imgs = res_json.spotMainImageDataInfo

    img_json = []
    # 이미지 정보를 순회하면서 파일 다운로드 받는 로직
    for img_info in imgs:
        img_res = requests.get(img_info.spotAwsS3ImageFullUrl)
        img_idx = img_info.spotAwsS3ImageSortNum

        # 이미지를 파일로 만드는 로직.(파일명에 베프지도 pk 이용)
        with open(f'img_{pk}_{img_idx}.jpg', 'wb') as f:
            f.write(img_res.content)
            img_json.append({f'pk_{img_idx}': f'img_{pk}_{img_idx}.jpg'})

        # 이미지를 파일로 만드는 로직.(파일명에 네이버 cid 이용 )
        try:
            with open(f'img_{cid}_{img_idx}.jpg', 'wb') as f2:
                f2.write(img_res.content)
                img_json.append({f'cid_{img_idx}': f'img_{cid}_{img_idx}.jpg'})
        except Exception:
            # 매칭되는 cid 없으면 무시.
            pass
    
    # 시설정보를 순회하면서 csv에 추가하는 로직
    facility_infos = res_json.spotFacilitiesDataInfo
    df.loc[idx, 'sfiInfo'] = facility_infos
    df.loc[idx, 'img_info'] = img_json
    write_csv_by_line(idx, df, new_csv)


def write_csv_by_line(idx, revised_df, writing_csv):
    # CSV 파일 경로와 파일 이름 지정. 이제 csv파일 불러올것임. ( 행렬 순회하면서 검색돌리고 그 결과를 csv에 저장할것임. )
    if idx == 0:
        revised_df.iloc[[idx]].to_csv(writing_csv, header=True, index=False)
    else:
        revised_df.iloc[[idx]].to_csv(writing_csv, header=False, index=False) # 1줄씩 csv파일에 쓰는 코드. 예상못한 에러로 인한 허탕 방지.



# CSV 파일을 DataFrame 객체로 불러오기
input_csv_file = './fetching_cid_sid_title.csv'
bf_df = pd.read_csv(input_csv_file)
new_csv_name = 'detail_info_added.csv'

with open(new_csv_name, 'a', encoding='utf-8', newline='') as new_csv:
    # 새 필드 추가
    bf_df['img_info'] = ""
    
    for idx, row in bf_df[['cid', 'spotSeq']].iterrows():
        spotSeq = row['spotSeq']
        cid = row['cid']
        fetching_data(idx, spotSeq, cid, bf_df, new_csv)
