import json
import math
import numpy as np
import pandas as pd
# def missing_val_impulation():
#     pass
#     res = 1
#     res_json = json.dump(res)
#     return res_json

'''
Content Based Filtering을 하고 싶어.
유사도를 구하려고 하는 기준이 되는 arr의 특징이 아래 user_no1과 같아.
user_no1 = [1, 0, 0, 0, 0, 0, 0, 0, 1]

그리고 아래 건물들의 시설정보들이 있는데 user_no1과 각 건물들의 유사도를 계산하고 싶어.
spot1 = [1, 0, 0, 0, 0, 0, 0, 0, 1]
spot2 = [1, 0, 1, 0, 0, 0, 0, 0, 1]
spot3 = [1, 0, 1, 1, 0, 0, 0, 0, 1]
spot4 = [0, 1, 0, 1, 0, 0, 1, 0, 1]

이렇게 주어지는데,
matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 1, 0, 0, 0, 0, 1], 
    [0, 1, 0, 1, 0, 0, 1, 0, 1]] 이렇게 matrix로 주어질 수도 있어. 파이썬 코드로 짜주고 결과를 보여줄 수 있어?
'''

def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


def calculate_similarity(user_profile, building_profiles):
    similarities = []
    for profile in building_profiles:
        similarity = cosine_similarity(user_profile, profile)
        similarities.append(similarity)
    return similarities


user_profile = np.array([1, 0, 0, 0, 0, 0, 0, 0, 1])
# building_profiles = np.array([[1, 0,]])


def binary_vectorize(arr):
    # 9개짜리 vector 배열만듬
    bin_vector = np.zeros(8)
    # arr[[1, 5, 9]] = 1
    bin_vector[np.array(arr)-1] = 1
    return bin_vector


# spot_dto 전처리해서 arr로 return해주는 함수.
def transform_dto_to_spot_arr(spot_dict):
    spotSfInfos = spot_dict['spotSfInfos']   #->     [1]
    spotId = spot_dict['spotId'] #-> 1
    spotLat = spot_dict['spotLat'] #-> 36.39665
    spotLng = spot_dict['spotLng'] #-> 127.4027
    reviewRating = spot_dict['reviewRating'] #-> 4.49
    reviewCount = spot_dict['reviewCount'] #-> 244
    
    sfvector = binary_vectorize(spotSfInfos)

    return [pk] + sfvector + [spotLat, spotLng, reviewRating, reviewCount]
    
    

# spot_dto_list를 받아서 순회하면서 전처리하고 다시 matrix로 합친걸 return 해주는 함수.
def transform_dto_to_spot_matrix(dto_matrix):
    spot_matrix = []
    
    for spot_dict in dto_matrix:
        spot_matrix.append(transform_dto_to_spot_arr(spot_dict))

    return spot_matrix

