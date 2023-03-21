import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User가 선택한 시설 정보
user_no1 = np.array([1, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)

# 건물들의 시설 정보
spot1 = np.array([1, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)
spot2 = np.array([1, 0, 1, 0, 0, 0, 0, 0, 1]).reshape(1, -1)
spot3 = np.array([1, 0, 1, 1, 0, 0, 0, 0, 1]).reshape(1, -1)
spot4 = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1]).reshape(1, -1)

# 건물들의 시설 정보를 하나의 matrix로 만듦
matrix = np.concatenate((spot1, spot2, spot3, spot4), axis=0)

# 코사인 유사도 계산
similarity = cosine_similarity(user_no1, matrix)

# 결과 출력
print(similarity)