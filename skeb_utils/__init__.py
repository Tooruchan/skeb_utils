from json import JSONDecodeError
import requests

headers = {
    'authority': 'skeb.jp',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',    
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'authorization': 'Bearer null',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://skeb.jp/',
    'accept-language': 'zh-CN,zh;q=0.9',
}
class skeb_user:
    __user_info = {}
    def __init__(self, name:str):
        """ Fetch user info from skeb API. 
            从 Skeb 官方 API 中拉取用户信息。

        Args:
            name: User's twitter username. It can have @ prefix. 
                  用户的推特用户名，可以带有 @ 前缀。
        
        Returns:
            从 Skeb 拿到的用户信息类，带有几个get函数和几个打印输出函数。
            User info get from skeb. It has some get functions and some print functions.
        """
        self.name = name.strip("@")
        response = requests.get('https://skeb.jp/api/users/'+self.name, headers=headers)
        try:
            self.user_info = response.json()
            self.__user_info = response.json()
        except JSONDecodeError:
            return
    def get_user_info(self):
        # Client Example
        # {'id': 234173, 'acceptable': False, 'creator': False, 'avatar_url': 'https://pbs.twimg.com/profile_images/1504649334289182723/r3iKZe7R.jpg', 'name': 'ふぉいぶ🐇', 'nsfw_acceptable': False, 'private_acceptable': True, 'screen_name': 'foivrchat', 'language': 'ja', 'header_url': 'https://pbs.twimg.com/profile_banners/1116144237957894144/1642424825/1500x500', 'body_size': 1000, 'received_works_count': 0, 'received_private_works_count': 0, 'received_nsfw_works_count': 0, 'sent_requests_average_cancel_time': 232251, 'appeal_receivable': True, 'request_master_rank': None, 'first_requester_rank': None, 'sent_first_works_count': 1, 'sent_public_works_count': 93, 'popular_creator_rank': None, 'instruction': 'unspecified', 'asct': None, 'description': '🇰🇷 🇯🇵OK\n男(Male)\nVRC(2018.08.05~...)\nからぱり(2019.10.14〜...)\nアイコン(@blancpig_yryr)\nヘッダー(@marekamico)\nBooth (http://foiv.booth.pm)   )\n- 作曲、衣装依頼はDM -', 'twitter_screen_name': 'foivrchat', 'nijie_id': None, 'dlsite_id': None, 'fanza_id': None, 'pixiv_id': None, 'booth_id': 'foiv', 'fantia_id': None, 'fanbox_id': None, 'skima_id': None, 'coconala_id': None, 'enty_id': None, 'patreon_id': None, 'busy': False, 'url': 'https://soundcloud.com/foiv', 'wishlist_id': '1M4IHVSIJ430F', 'youtube_id': None, 'complete_rate': None, 'show_social_profile': True, 'foriio': False, 'twitter_uid': '1116144237957894144', 'accept_expiration_days': 30, 'complete_expiration_days': 60, 'banned': False, 'og_image_url': 'https://skeb.imgix.net/static/ogp.png?auto=format%2Ccompress&fit=crop&crop=top&w=1200&h=630&s=895f3a59e8f71d0de10154ea7e4bed90', 'skills': [{'genre': 'art', 'default_amount': 5000}], 'payment_methods': {'credit_cards': {'master_card': {'nsfw': True}, 'visa': {'nsfw': True}}}, 'genre': 'art', 'default_amount': None, 'similar_creators': []}
        # Creator Example
        # {'id': 1136950, 'acceptable': True, 'creator': True, 'avatar_url': 'https://pbs.twimg.com/profile_images/1482745199159701504/HLedBl6n.jpg', 'name': '佐藤さら𖠚ᐝ✨skeb募集中✨', 'nsfw_acceptable': False, 'private_acceptable': True, 'screen_name': 'sarasuty1221', 'language': 'ja', 'header_url': 'https://pbs.twimg.com/profile_banners/1282611561320742912/1642348843/1500x500', 'body_size': 500, 'received_works_count': 9, 'received_private_works_count': 0, 'received_nsfw_works_count': 0, 'sent_requests_average_cancel_time': None, 'appeal_receivable': False, 'request_master_rank': None, 'first_requester_rank': None, 'sent_first_works_count': 0, 'sent_public_works_count': 0, 'popular_creator_rank': None, 'instruction': 'unspecified', 'asct': None, 'description': '神絵師目指してます✨/→pixiv(https://www.pixiv.net/users/33095581)→Skeb(https://skeb.jp/@sarasuty1221)/Vの娘→桜花やよい(@sakuraha_yayoi)/gmail(satousara12zi@gmail.com) ↓↓↓マシュマロ', 'twitter_screen_name': 'sarasuty1221', 'nijie_id': None, 'dlsite_id': None, 'fanza_id': None, 'pixiv_id': 33095581, 'booth_id': None, 'fantia_id': None, 'fanbox_id': None, 'skima_id': None, 'coconala_id': None, 'enty_id': None, 'patreon_id': None, 'busy': False, 'url': 'https://marshmallow-qa.com/sarasuty1221?utm_medium=url_text&utm_source=promotion', 'wishlist_id': '1PXZ7GVHO7ET5', 'youtube_id': None, 'complete_rate': 1.0, 'show_social_profile': True, 'foriio': False, 'twitter_uid': '1282611561320742912', 'accept_expiration_days': 30, 'complete_expiration_days': 60, 'banned': False, 'og_image_url': 'https://skeb-avatar.imgix.net/https%3A%2F%2Fskeb.jp%2Fapi%2Fusers%2Fsarasuty1221%2Fbackground%3Fd%3Db72e0a?blend64=aHR0cHM6Ly9hc3NldHMuaW1naXgubmV0L350ZXh0P3R4dDY0PVVrVkRUMDFOUlU1RVJVUWdVRkpKUTBVJnR4dGNscj1mZmYmdHh0Zm9udDY0PVFYWmxibWx5TFUxbFpHbDFiUSZ0eHRhbGlnbj1jZW50ZXImdHh0c2l6ZT00MCZ0eHRzaGFkPTEwJmZtPXBuZyZ3PTEyMDA&bm=normal&by=360&mark64=aHR0cHM6Ly9hc3NldHMuaW1naXgubmV0L350ZXh0P3R4dDY0PU9Td3dNREFnU2xCWiZ0eHRjbHI9ZmZmJnR4dGZvbnQ2ND1RWFpsYm1seUxVSnNZV05yJnR4dGFsaWduPWNlbnRlciZ0eHRzaXplPTgwJnR4dHNoYWQ9MTAmZm09cG5nJnc9MTIwMA&marky=415&txt64=5L2Q6Jek44GV44KJ8JagmuGQneKcqHNrZWLli5_pm4bkuK3inKg&txtclr=fff&txtfont64=QXZlbmlyLUJsYWNr&txtfit=max&txtalign=middle%2Ccenter&txtsize=60&txtshad=10&auto=format%2Ccompress&fit=crop&crop=top&w=1200&h=630&s=bf8ebaaa7f7cbeacde6c940a9ecf90fb', 'skills': [{'genre': 'art', 'default_amount': 9000}, {'genre': 'correction', 'default_amount': 3000}], 'payment_methods': {'credit_cards': {'master_card': {'nsfw': True}, 'visa': {'nsfw': True}}}, 'genre': 'art', 'default_amount': 9000, 'similar_creators': []}
        try:
            account_info = self.user_info
            del account_info["sent_works"] # 去掉申请的约稿
            del account_info["received_works"] # 去掉收到的约稿
            return account_info
        except AttributeError:
            return "error"
    def get_user_sent_works(self):
        # 获取画师完成约稿信息
        if not self.__user_info.get("creator"):
            return "Not a creator!"
        try:
            return self.__user_info["sent_works"]
        except KeyError:
            return "error"
    def get_user_received_works(self):
        # 获取客户发送约稿请求信息
        try:
            return self.__user_info["received_works"]
        except KeyError:
            return "error"
    def print_user_info(self):
        print("Skeb 用户："+self.__user_info['screen_name'])
        print("Twitter 用户名："+self.__user_info['name'])
        print("Twitter 简介："+self.__user_info['description'])
        if self.__user_info["creator"]:
            if self.__user_info["acceptable"]:
                acceptable = "正在募集"
            else:
                acceptable = "停止了"
            print("是否允许接稿："+acceptable)
            if self.__user_info["acceptable"]:
                skills = self.__user_info["skills"]
                for i in skills:
                    if i["genre"] == "art":
                        print("类型：插画")
                        print("おまかせ金額："+str(i["default_amount"]))
                    if i["genre"] == "correction":
                        print("类型：建议")
                        print("おまかせ金額："+str(i["default_amount"]))
            print("总共接收了{0}件约稿，其中私有约稿{1}件，NSFW约稿{2}件。".format(self.__user_info["received_works_count"], self.__user_info['received_private_works_count'], self.__user_info['received_nsfw_works_count']))
            print("平均承认约稿时间：{}".format(self.__user_info["accept_expiration_days"]))
            print("平均完成约稿时间：{}".format(self.__user_info['complete_expiration_days']))

        else:
            print("总共约稿{}件。".format(self.__user_info["sent_public_works_count"]))