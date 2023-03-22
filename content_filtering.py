'''
작성 목록
1. 거리계산 맨하탄거리. 하버사인거리는 라이브러리로 대체 (km로 나옴)

2. 시설 코사인 유사도 (0-1 사이 유사도로 나옴)
2-1. 시설 코사인 유사도 계산 최적화 위한 유저정보배열 0값 제거 로직

3. 
'''

from sklearn.metrics.pairwise import cosine_similarity
from haversine import haversine
from math import radians, log10

import numpy as np
import pandas as pd

# 테스트용 input
ref_facility_arr = [1, 0, 0, 0, 0, 0, 0, 0, 1]
spot1 = [1, 0, 0, 0, 0, 0, 0, 0, 1]
spot2 = [1, 0, 1, 0, 0, 0, 0, 0, 1]
spot3 = [1, 0, 1, 1, 0, 0, 0, 0, 1]
spot4 = [0, 1, 0, 1, 0, 0, 1, 0, 1]

spot_matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    ]

# 통합된 matrix가 들어오니까 쪼개고, 분류해서 기능제공. 😀 pk매핑 유지 해야됨.
def content_based_recom(ref_facility_arr, spot_matrix, category):
    # spot_matrix의 4번째 col이 category정보를 나타냄.
    cat_col_num = 3
    # spot_matrix의 cat이 1(카페)인 곳들만 선택
    
    spot_df = pd.DataFrame(spot_matrix)
    # 카테고리의 정보가 일치하는 row만 살린 df
    cat_filtered_df = spot_df.loc[spot_df.iloc[:, cat_col_num] == category, :]

    # facility_df와 coor_df로 나눠서 저장. 😀 숫자 조정 필요.
    facility_df = cat_filtered_df.iloc[:8, :]
    coor_df = cat_filtered_df.iloc[8:10, :]
    matrix_size = len(coor_df)
    rating_df = cat_filtered_df.iloc[10:, :]
    
    # 1차 - 시설 유사도정보 구함. ndArr.
    facility_scores = facility_cos_sim(ref_facility_arr, facility_df)

    # 기준 좌표정보로부터 각 시설의 맨하탄거리를 구한 list
    ref_facility_coor = ref_facility_arr[9:]
    manhattan_distances = [manhattan_distance(ref_facility_coor, coor_df[idx]) for idx in range(matrix_size)]
    
    # rating_scores = [rating_score(rating_df[idx][0], rating[idx][1]) for idx in range(matrix_size)]
    rating_scores = [rating_score(*rating) for rating in rating_df]
    
    # 각 점수를 0-1사이의 숫자로 치환을 먼저해서 비율을 원하는대로 조절 가능하게 해야함.
    # 위의 시설유사도, 맨하탄거리, rating_score 반영된걸 취합하면 됨.
    content_scores = []




# 거리계산 1 - 맨하탄거리
def manhattan_distance(coor_A, coor_B):
    """
    두 지점의 위도와 경도를 입력받아 맨하탄 거리를 계산하여 반환합니다.
    기본 단위는 km인데 추후 scale 조절.
    """
    a_lng, a_lat = coor_A
    b_lng, b_lat = coor_B
    coor_midpoint = [b_lng, a_lat]

    lng_dist = haversine(coor_A, coor_midpoint)
    lat_dist = haversine(coor_B, coor_midpoint)
    
    # 맨하탄 거리를 계산합니다.
    sum_distance = lng_dist + lat_dist
    return sum_distance


# 시설 유사도 arr로 반환, idx 유지
def facility_cos_sim(ref_facility_arr, facility_matrix):
    ref_facility_arr = np.array(ref_facility_arr).reshape(1,-1)
    res = cosine_similarity(ref_facility_arr, facility_matrix)
    print(type(res))
    print(res)
    return res[0]


# 가중치 조절 추후에 진행
def rating_score(avg_score, count):
    score_weight = 1
    count_weight = 1

    return avg_score*score_weight + log10(count)*count_weight


# 시설유사도 - 속도개선1 (field 축소)
def valid_field(ref_facility_arr):
    '''
    user_pref_arr에서 0인 idx를 싹 날려버림.
    유효한 field idx만 묶어서 반환
    '''
    pass

# 시설유사도 - 속도개선1 (축소된 field 반영)
def apply_valid_field(facility_matrix):
    '''
    valid_field에서 0으로 날아간 idx를 제거한 matrix 반환
    '''
    pass


# weighted_score