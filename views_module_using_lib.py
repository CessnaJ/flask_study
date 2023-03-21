from sklearn.metrics.pairwise import cosine_similarity
from harversine import harversine
from math import radians

import numpy as np

user_no1 = [1, 0, 0, 0, 0, 0, 0, 0, 1]
spot1 = [1, 0, 0, 0, 0, 0, 0, 0, 1]
spot2 = [1, 0, 1, 0, 0, 0, 0, 0, 1]
spot3 = [1, 0, 1, 1, 0, 0, 0, 0, 1]
spot4 = [0, 1, 0, 1, 0, 0, 1, 0, 1]

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


def manhatan_distance(location_a, location_b):
    lng_subtract_dist = abs(location_a[0] - location_b[0])
    lat_subtract_dist = abs(location_a[1] - location_b[1])
    return lng_subtract_dist + lat_subtract_dist
    

def rating_score(avg_score, count):
    avg_score
    count



for spot_location in locations:
    distance.append(harversine(pivot_location, spot_location))
    distance.append(harversine(pivot_location, spot_location))    


lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

haversine(lyon, paris)
>> 392.2172595594006  # in kilometers

'''

def manhattan_distance(lat1, lon1, lat2, lon2):
    """
    두 지점의 위도와 경도를 입력받아 맨하탄 거리를 계산하여 반환합니다.
    """
    # 위도와 경도를 라디안 단위로 변환합니다.
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    # 맨하탄 거리를 계산합니다.
    distance = abs(lat1 - lat2) + abs(lon1 - lon2)

    # 맨하탄 거리를 반환합니다.
    return distance


# weighted_score