import json
import requests
import pandas as pd
# config.py
import config
import random

api_key = config.HOTPEPPER_API_KEY

i_start = 1
restaurant_datas=[]


def pick_restaurant():
    rand_pick = random.randrange(1,30090)
    print(rand_pick)
    query = {
        'key': api_key,
        'large_area': 'Z011', # 東京
        'order': 1, #名前の順
        'start': rand_pick, #検索結果の何番目から出力するか
        'count': 1, #最大取得件数
        'format': 'json'
    }
    url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    responce = requests.get(url_base, query)
    result = json.loads(responce.text)['results']['shop']
    print(result)
    for restaurant in result:
        restaurant_datas.append([restaurant['name'], restaurant['address'], restaurant['budget']['name'], restaurant['genre']['name'], restaurant['urls']['pc']])

    print(restaurant_datas)

pick_restaurant()