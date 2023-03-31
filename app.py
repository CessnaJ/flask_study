'''
예상 추천 시나리오
1. 세부정보 눌러서 자동으로 나오는 item 기반 유사도 추천 (시설 정보는 근데.. 유저가 필요하다고 한거랑 유사도 맞춰주는게 맞지 않나? )

2. 카테고리를 눌러서 유저기반 추천을 받는 메인 추천기능
'''
from flask import Flask, request, redirect, jsonify, Blueprint, abort
import pymysql
import json
import ast

import numpy as np
import pandas as pd

from content_filtering import content_based_recom
from colab_filtering import colab_filtering
from views_module import transform_dto_to_spot_arr, transform_dto_to_spot_matrix, transform_dto_to_ref_user_arr, transform_dto_to_user_matrixes

app = Flask(__name__)
recom_bp = Blueprint('recom', __name__, url_prefix='/recom')


@app.route('/')
def index():
    try:
        return 'test_hello?'

    except Exception as e1:
        print(e1)
        return e1


@app.route('/post_test/', methods=['POST'])
def post_test():
    try:
        data = request.json
        print(request)
        print(data)
        return data
    except Exception as e2:
        print(e2)
        return e2


@app.route('/read/<id>/')
def read(id):
    return id


# 기준이 되는 장소의 pk
# 해당 장소와 같은 카테고리의 비슷한 장소 추천해주는 함수.
# @recom_bp.route('/content_based/', methods=['POST'])
@app.route('/content_based', methods=['POST'] )
def content_recom():
    try:
        print(request)
        data = request.json
        # print(data)
        ref_spot_dict_str = data['userSpot']
        print(1)
        ref_spot_dict = json.loads(ref_spot_dict_str)
        print(2)
        cat_num = ref_spot_dict.get('category')
        print(3)
        
        spot_info_matrix_dto = data['spots']
        print(4)
        # temp_dto = json.loads(spot_info_matrix_dto)
        
        ref_arr = transform_dto_to_spot_arr(ref_spot_dict)
        print(5)
        spot_info_matrix = transform_dto_to_spot_matrix(spot_info_matrix_dto)
        print(6)

        # 추천 메인로직 모듈화
        res = content_based_recom(ref_arr, spot_info_matrix, cat_num)
        print(7)
        # res = res
        # [(환산합산점수0-1, pk, 맨하탄거리)...] 로 되어있는 모든 장소의의 배열이 나옴. top10개로 추리는 과정 필요.

        top10_res = res[:10]
        print(8)
        print(top10_res)
        top10_res_formatted = [(item[1], round(item[2]*1000,-2)) for item in top10_res]
        print(10)
        return jsonify(top10_res_formatted)
    
    except ValueError as e:
        print(e)
        abort(400, str(e))
    except KeyError as e:
        print(e)
        abort(400, f'Missing key: {str(e)}')
    except Exception as e:
        print(e)
        abort(500, str(e))



# pk랑 매핑 필요.
# @recom_bp.route('/hybrid/', methods=['POST'])
@app.route('/hybrid', methods=['POST'])
def hybrid_filtering():
    # print(request)
    # print(request.json)
    # return request.json
    
    try:
        topK = 10
        data = request.json # json 객체를 일단 통째로 가져옴.
        # json 객체 변환부
        ref_facility_arr = data['user_arr'] # 1번 파라미터
        spot_info_matrix = data['spot_matrix'] # 2번 파라미터

        user_rating_arr = data['user_rating_arr'] # user_arr에서 추출해서 새로운 arr구성 필요.
        rating_matrix = data['rating_matrix'] # 3번파라미터-1

        user_like_arr = data['user_like_arr'] # user_arr에서 추출해서 새로운 arr 구성 필요.
        like_matrix = data['like_matrix'] # 3번파라미터 -2

        # 😀여기서부터 아래로 다시 파싱하는 로직.
        ref_user_str = data['user']
        user_dto_str = data['users']
        spot_dto_str = data['spots']

        ref_user_dict = json.loads(ref_user_str)
        users_dict = json.loads(user_dto_str)
        spots_dict = json.loads(spot_dto_str)


        spots_matrix = transform_dto_to_spot_matrix(spots_dict)
        ref_user_arr, user_rating_arr, user_like_arr = transform_dto_to_ref_user_arr(ref_user_dict, len(spots_matrix))
        users_rating_matrix, users_like_matrix = transform_dto_to_user_matrixes(users_dict)


        # 계산부
        content_sim_arr = content_based_recom(ref_facility_arr, spot_info_matrix, category=None)
        # [(0.2418561222123986, 1, 10.899476864300897), (0.2533676665221327, 2, 10.882014520230928), (변환 스코어0-1, pk, 맨하탄거리..) ... ]
        user_sim_arr = colab_filtering(user_rating_arr, rating_matrix, user_like_arr, like_matrix)

        res_sim_arr = content_sim_arr + user_sim_arr
        res_spots = res_sim_arr[:topK]
        # top K의 pk 매칭해서 돌려주기

        # res_spots = [2500, 500, 9, 11, 1]

        return jsonify(res_spots)

    except ValueError as e:
        abort(400, str(e))
    except KeyError as e:
        abort(400, f'Missing key: {str(e)}')
    except Exception as e:
        abort(500, str(e))

# 아래에 위치해야함.
app.register_blueprint(recom_bp)

# 모든 host로부터의 요청 허용. 시스템 허용 옵션도 받는다.
# terminal에서 export FLASK_RUN_HOST=0.0.0.0 으로 해야 설정이 먹는거 수정해야함.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)


