'''
작성 목록
1. 거리계산 맨하탄거리. 하버사인거리는 라이브러리로 대체 (km로 나옴)

2. 시설 코사인 유사도 (0-1 사이 유사도로 나옴)
2-1. 시설 코사인 유사도 계산 최적화 위한 유저정보배열 0값 제거 로직

3. 
'''

from sklearn.metrics.pairwise import cosine_similarity
from haversine import haversine
from math import radians

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

def content_based_recom(ref_facility_arr, spot_matrix, category):
    ref_facility_arr = ref_facility_arr

    # 위에서 형변환이랑 다 되었다고 치고..






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



# 시설 유사도 arr로 반환, idx 유지
def facility_cos_sim(ref_facility_arr, facility_matrix=None):
    ref_facility_arr = np.array(ref_facility_arr).reshape(1,-1)
    facility_matrix = [spot1, spot2, spot3, spot4]
    res = cosine_similarity(ref_facility_arr, facility_matrix)
    print(res[0])
    print(type(res))


# 1번 방식
matrix = np.array([user_no1, spot1, spot2, spot3, spot4])
similarity_matrix = cosine_similarity(matrix)
result = similarity_matrix[0][1:]
print(result) # User정보 자기자신을 제외한 유사도.
# User정보에서 0이 있는걸 굳이 쓸 필요도 없어보인다. 해당 필드를 matrix에서 애초에 제거하고
# 행렬계산하면 불필요한 계산이 줄어든다.

# 2번 방식
# 건물 정보를 2차원 배열로 만듦
matrix = np.array([spot1, spot2, spot3, spot4])
# 코사인 유사도를 계산
similarities = cosine_similarity(matrix, [user_no1])

print(similarity_matrix)

# 개선 필요 -> 불필요한 계산이 많다. 사실 matrix[0]만 있어도 됨.
# 모든 원소끼리의 유사도를 구하는식이 되어버렸다.

'''
pivot_location = location[0]
distance = []

#a to b (a가 base)
def manhatan_distance(location_a, location_b):
    lng_subtract_from_a = abs(location_b[0] - location_a[0])
    lat_subtract_from_a = abs(location_a[1] - location_b[1])

    return lng_subtract_dist + lat_subtract_dist
    

def rating_score(avg_score, count):
    score_weight = 1
    count_weight = 1

    return avg_score*score_weight + count*count_weight



for spot_location in locations:
    distance.append(harversine(pivot_location, spot_location))
    distance.append(harversine(pivot_location, spot_location))    


lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

haversine(lyon, paris)
>> 392.2172595594006  # in kilometers

'''

# weighted_score