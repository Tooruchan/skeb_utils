# -*- encoding:utf-8 -*-
from skeb_utils import skeb_user, get_artist_info

hy = skeb_user("foivrchat")
first_works = hy.get_user_info()["sent_public_works_count"]
user_info = hy.get_user_info()
print("用户 {0} 共向画师发送了 {1} 份约稿申请。".format(user_info["name"], first_works))
artists = list(set([x["path"].split("/")[1] for x in hy.get_user_sent_works()]))
strs = []
with open("./skeb.txt", "w", encoding="utf-8") as skeb_list:
    for i in artists:
        info = get_artist_info(i)
        if info["acceptable"]:
            strs.append(
                "画师名字: {0}\n画师用户名: {1}\n画师Skeb主页: https://skeb.jp/{1}\n画师接稿状态：{2}\n画师价格: {3}\n\n".format(
                    info["name"],
                    info["screen_name"],
                    info["acceptable"],
                    info["skills"][0]["default_amount"],
                )
            )
            print(
                "画师名字: {0}\n画师用户名: {1}\n画师Skeb主页: https://skeb.jp/{1}\n画师接稿状态：{2}\n画师价格: {3}\n".format(
                    info["name"],
                    info["screen_name"],
                    info["acceptable"],
                    info["skills"][0]["default_amount"],
                )
            )
    skeb_list.writelines(strs)
