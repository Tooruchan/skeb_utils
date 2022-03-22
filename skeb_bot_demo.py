from skeb_utils import skeb_user
import requests
import time
import sqlite3

self_hosted_api = ""
bot_api_token = ""
chat_id = ""

artist_list = [
    "@Nakkar7"
]

for i in artist_list:
    artist = skeb_user(i).get_user_info()
    amount = artist["skills"][0]["default_amount"]
    if artist['acceptable']:
        msg = "画师 {0} 在 skeb 上开放接稿了！\nSkeb 主页：{1}\n约稿预计金额：{2} JPY".format(
            artist["name"], "https://skeb.jp/@" + artist["screen_name"], amount
        )
        response = requests.get(self_hosted_api+bot_api_token+"/sendMessage?chat_id={0}&text={1}".format(chat_id,msg))
        time.sleep(5)
    else:
        # 未开放约稿，跳过
        pass
