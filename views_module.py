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
    [0, 1, 0, 1, 0, 0, 1, 0, 1]] 
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
    # 8개짜리 vector 배열만듬
    bin_vector = np.zeros(8)

    # if arr:
    #     bin_vector[np.array(arr)-1] = 1
    #     return bin_vector.tolist()
    # else:
    #     return bin_vector.tolist()


    arr = [int(x) for x in arr]
    try:
        if type(arr) != list:
            print(type(arr))

        
        bin_vector[np.array(arr)-1] = 1
        return bin_vector.tolist()
    except Exception as e:
        print(arr)
        print(type(arr))
        
        for el in arr:
            print("asdasda")
            print(el)
            print(type(el))


# spot_dto 전처리해서 arr로 return해주는 함수.
def transform_dto_to_spot_arr(spot_dict):
    # try:
        spotSfInfos = spot_dict['sfInfoIds']   # ->[1]
        spotId = spot_dict['spotId'] #-> 1
        spotLat = spot_dict['spotLat'] #-> 36.39665
        spotLng = spot_dict['spotLng'] #-> 127.4027
        reviewRating = spot_dict['reviewScore'] #-> 4.49
        reviewCount = spot_dict['reviewCount'] #-> 244
        category = spot_dict['spotCategory'] # 식당 1, 도서관 31, 32 ... 😀
        print(category)

        sfvector = binary_vectorize(spotSfInfos)
        print(123123)
        return [spotId] + sfvector + [spotLat, spotLng, reviewRating, reviewCount, category]
    # except Exception as e:
        # print(e)
        # print(spot_dict)
    
    

# spot_dto_list를 받아서 순회하면서 전처리하고 다시 matrix로 합친걸 return 해주는 함수.
def transform_dto_to_spot_matrix(dto_matrix):
    print(11)
    dto_matrix = json.loads(dto_matrix)
    print(22)
    # print(dto_matrix)
    # print(type(dto_matrix))
    print(33)
    return [transform_dto_to_spot_arr(spot_dict) for spot_dict in dto_matrix]


# def transform_dto_to_spot_matrix(dto_matrix):
#     spot_matrix = []
    
#     for spot_dict in dto_matrix:
#         spot_matrix.append(transform_dto_to_spot_arr(spot_dict))

#     return spot_matrix

def transform_dto_to_ref_user_arr(dto_dict, spot_matrix_length):
    spotSfInfos = dto_dict['sfInfoIds']   # ->[2, 4, 5]
    spotLat = dto_dict['userLat'] #-> 36.39665
    spotLng = dto_dict['userLng'] #-> 127.4027
    reviews_arr = dto_dict['reviews'] #-> 4.49
    like_arr = dto_dict['likeList']
    dislike_arr = dto_dict['disLikeList']
    rating_vector = create_rating_vector(reviews_arr, spot_matrix_length)
    like_vector = create_like_vector(like_arr, dislike_arr, spot_matrix_length)


    spotId = dto_dict['spotId'] #-> 1
    reviewRating = dto_dict['reviewScore'] #-> 4.49
    reviewCount = dto_dict['reviewCount'] #-> 244
    category = dto_dict['spotCategory'] # 식당 1, 도서관 31, 32 ... 😀

    rating_arr = np.zeros(spot_matrix_length)
    like_arr = np.zeros(spot_matrix_length)

    sfvector = binary_vectorize(spotSfInfos)
    return [spotId] + sfvector + [spotLat, spotLng, reviewRating, reviewCount, category]
        
        
def create_rating_vector(arr, spot_matrix_length):
    rating_dict = dict()
    rating_vector = np.zeros(spot_matrix_length)

    for review_item in arr:
        spotId = review_item.get('spotId')
        review_score = review_item.get('reviewScore')
        rating_dict[spotId] = review_score

    for k,v in rating_dict:
        rating_vector[k-1] = v

    return rating_vector.tolist()

like_arr = [1,5,9,11]
dislike_arr = [1,20,23,25]
def create_like_vector(like_arr, dislike_arr, spot_matrix_length):
    like_vector = np.zeros(spot_matrix_length)
    like_vector[np.array(like_arr)-1] = 1
    like_vector[np.array(dislike_arr)-1] = -1
        
    return like_vector.tolist()

