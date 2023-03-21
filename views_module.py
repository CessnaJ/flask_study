import json
import math
import numpy as np
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