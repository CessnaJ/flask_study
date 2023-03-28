from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
'''
Main category를 내가 걸러서 행렬계산하나? 이거 상의하자.

들어올 수 있는 예상 input
1-1. 유사도 구하는 기준 user의 가게별 평점 arr ( 1 x 총 가게 숫자  - sparse matrix ) 이거는 0 쳐내면 안되나?
user가 매긴 평점 matrix ( user No )
1-2. 다른 모든 유저들의 가게별 평점 matrix (이래서 별점이 0점이 없구나. 평가 안한거랑 최저점으로 평가한걸 Implicit하게 구분하려고.)

2-1. 기준 user의 따봉, 싫어요 먹인 arr (좋아요1, 싫어요-1, 평가안함 NaN이나 0)
2-2. 다른 모든 User들의 가게별 평점 matrix


고려할 점 
- 평점을 먹인거는 평가를 했다는거니까 이미 갔다는뜻임. (재추천이 안나오느게 맞음.)
- 좋아요/싫어요는 기존 추천에 대한 적합도를 바로 보기 위한 장치인거지 거기를 갔다는 뜻은 아님. 그래서 재추천이 나올 수 있음.

- 단순히 예상 적합도를 구해서 item을 봐주는거면.. 점수를 구하고나서, "기존평가" item들의 적합도점수를 0으로 만들고 정렬을 해서 10개정도 뽑아주면 되는거 아니야?
    이러면 겹칠 일 없다. 깔끔함.



완전 콜드스타트면 어떻게 하지?
'''

target_user = [5,0,1,0,0]
matrix =[[5,0,1,0,0],
[0,0,0,0,0],
[0,1,1,0,1],
[5,0,0,5,5],
[1,0,1,1,1]]


# rating 유사도 arr, like 유사도 arr 합해서 최종 유사도 구하기 (0-1 유사도만 나옴. 예상평점은 필요 없어서 일부러 안구했음.)
# 예외처리 시나리오 - 전체 유저의 숫자가 K명 미만, 평가한 항목이 K개 미만 (colab filtering 반영 안하는게 맞음.)
def colab_filtering(user_rating_arr, rating_matrix, user_like_arr, like_matrix):
    rating_sim_arr = rating_cos_sim(user_rating_arr, rating_matrix) # npArr
    like_sim_arr = like_cos_sim(user_like_arr, like_matrix) # npArr 이거 수정 필요.

    res_sim = rating_sim_arr + like_sim_arr
    res_sim /= 2
    return res_sim


# rating 기준으로 한 유사도 구하기 0-1
def rating_cos_sim(user_rating_arr, rating_matrix): # 둘중 하나가 0이면, 유사도 분모에 안들어감.
    user_rating_arr = np.array(user_rating_arr).reshape(1,-1)
    res = cosine_similarity(user_rating_arr, rating_matrix)
    return res


# like/dislike 기준으로 한 유사도 구하기 0-1
def like_cos_sim(user_like_arr, like_matrix):
    user_like_arr = np.array(user_like_arr).reshape(1,-1)
    res = cosine_similarity(user_like_arr, like_matrix)
    return res


def expected_rating():
    pass



'''
import numpy as np

# 유저별 평점 행렬
ratings = np.array([[0, 1, 5], [2, 2, 5], [0, 5, 2]])

# 유저간 유사도
similarity = np.array([0.998, 0.775, 0.6])

# 이미 평가한 아이템 제외하고 추천 아이템 추출
def recommend_items(user_id, ratings, similarity):
    # 해당 유저가 평가한 아이템 제외
    unrated_items = np.where(ratings[user_id] == 0)[0]
    # 다른 유저들의 해당 아이템 평점 가져오기
    item_ratings = ratings[:, unrated_items]
    # 다른 유저들의 해당 아이템에 대한 유사도 가져오기
    item_similarity = similarity[:, np.newaxis][:, unrated_items]
    # 예상 평점 계산
    pred_ratings = np.sum(item_ratings * item_similarity, axis=0) / np.sum(item_similarity, axis=0)
    # 예상 평점이 가장 높은 아이템 추천
    top_items = unrated_items[np.argsort(pred_ratings)[::-1]]
    return top_items

# 예시로 첫번째 유저가 어떤 아이템을 추천받아야 하는지 확인해보기
recommended_items = recommend_items(0, ratings, similarity)
print("Recommended items for user 0:", recommended_items)
'''