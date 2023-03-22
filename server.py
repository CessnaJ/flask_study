'''
예상 추천 시나리오
1. 세부정보 눌러서 자동으로 나오는 item 기반 유사도 추천 (시설 정보는 근데.. 유저가 필요하다고 한거랑 유사도 맞춰주는게 맞지 않나? )

2. 카테고리를 눌러서 유저기반 추천을 받는 메인 추천기능
'''
from flask import Flask, request, redirect, jsonify
import pymysql

import numpy as np
import pandas as pd

from content_filtering import content_based_recom
from colab_filtering import colab_filtering



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
    return 'test_hello?'


@app.route('/read/<id>/')
def read(id):
    return id


# 해당 장소와 비슷한 장소 추천해주는 함수.
@app.route('/content_recom/<int:cat_num>', methods=['POST'])
def content_recom(cat_num):
    try:
        data = request.json
        
        # 기준이 되는 arr -> 변수명 추후 수정 😀
        ref_facility_arr = data['spotsfs_arr']
        spot_info_matrix = data['spot_matrix']
        
        # 추천 메인로직 모듈화
        res = content_based_recom(ref_facility_arr, spot_info_matrix, cat_num)

        return jsonify(res)
    
    except ValueError as e:
        abort(400, str(e))
    except KeyError as e:
        abort(400, f'Missing key: {str(e)}')
    except Exception as e:
        abort(500, str(e))



# pk랑 매핑 필요.
@app.route('/hybrid_filtering_recom/', methods=['POST'])
def hybrid_filtering():
    try:
        topK = 10
        data = request.json

        ref_facility_arr = data['user_arr']
        spot_info_matrix = data['spot_matrix']

        user_rating_arr = data['user_rating_arr']
        rating_matrix = data['rating_matrix']

        user_like_arr = data['user_like_arr']
        like_matrix = data['like_matrix']

        content_sim_arr = content_based_recom(ref_facility_arr, spot_info_matrix, category=None)
        user_sim_arr = colab_filtering(user_rating_arr, rating_matrix, user_like_arr, like_matrix)

        res_sim_arr = content_sim_arr + user_sim_arr
        res_sim_arr[:topK]
        # top K의 pk 매칭해서 돌려주기

        res_spots = [2500, 500, 9, 11, 1]

        return jsonify(res_spots)

    except ValueError as e:
        abort(400, str(e))
    except KeyError as e:
        abort(400, f'Missing key: {str(e)}')
    except Exception as e:
        abort(500, str(e))




if __name__ == '__main__':
    app.run(port=5000, debug=True)





