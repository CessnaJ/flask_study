import requests
import csv
import pandas as pd
import numpy as np
import time
import random
import re
import json
from bs4 import BeautifulSoup

csv_file = './fetching_cid_sid_title.csv'

bf_df = pd.read_csv(csv_file)

cid = 'cid'
sid = 'sid'

bf_df['naver_serach_id'] = ""
bf_df['cid_sid_equals'] = ""
bf_df['naver_rating_score'] = ""
bf_df['naver_rating_count'] = ""
bf_df['naver_place_title'] = ""
bf_df['card_review_json'] = ""

def element_content_as_dict(li_elements):
    reviews = []
    for li_element in li_elements:
        review_text = li_element.find("span", {"class": "nWiXa"}).text
        review_count = int(li_element.find("span", {"class": "TwM9q"}).text)
        review_dict = {review_text: review_count}
        reviews.append(review_dict)
    json_reviews = json.dumps(reviews)
    return json_reviews


def regex_rating_count(text_val):
    regex = r"\((\d+)명 참여\)"
    matches = re.search(regex, text_val)
    num = matches.group(1)
    return num


