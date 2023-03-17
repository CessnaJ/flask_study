from flask import Flask, request, redirect
import pymysql

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='root',
                     db='dbname',
                     charset='utf8')

cursor = db.cursor()

@app.route('/')
def index():
    return 'hello?'

@app.route('/read/<id>/')
def read(id):
    return id



@app.route('/hybrid_filtering/')
def hybrid_filtering():
    # 아이템 프로파일링
    items_df = pd.read_csv('items.csv') # 아이템 데이터를 불러옵니다.
    item_features = items_df[['disabled_facility', 'distance', 'rating', 'num_reviews']] # 사용할 아이템 특성 정보를 선택합니다.

    # 사용자 프로파일링
    users_df = pd.read_csv('users.csv') # 사용자 데이터를 불러옵니다.
    user_id = 'user_1' # 현재 사용자 ID
    user_features = users_df.loc[users_df['user_id']==user_id, ['preferred_facility', 'current_location']] # 사용자의 프로파일을 선택합니다.

    # Content-based Filtering
    item_sim_matrix = cosine_similarity(item_features) # 아이템 간의 유사도 행렬을 계산합니다.
    user_profile = np.dot(user_features['preferred_facility'], item_sim_matrix) / np.sum(item_sim_matrix, axis=0) # 사용자 프로파일을 계산합니다.
    recommended_items = np.argsort(-user_profile)[:10] # 사용자에게 추천할 아이템을 선택합니다.

    # Collaborative Filtering
    users_df['similarity'] = cosine_similarity(users_df['current_location'].values.reshape(1,-1), user_features['current_location'].values.reshape(1,-1)).squeeze() # 현재 사용자와 다른 사용자들의 유사도를 계산합니다.
    similar_users = users_df.sort_values('similarity', ascending=False).iloc[1:11] # 현재 사용자와 가장 유사한 10명의 사용자를 선택합니다.
    recommended_items_collab = similar_users.iloc[:,2:].sum().sort_values(ascending=False)[]:10].index.tolist() # 가장 많이 구매한 아이템을 선택합니다.

    # Hybrid Filtering
    content_weight = 0.7 # Content-based Filtering 결과에 대한 가중치
    collab_weight = 0.3 # Collaborative Filtering 결과에 대한 가중치
    recommended_items_hybrid = content_weight * recommended_items + collab_weight * recommended_items_collab # 두 결과를 조합하여 최종 추천 결과를 생성합니다.


if __name__ == '__main__':
    app.run(port=5000, debug=True)





