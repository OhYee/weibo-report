from weibo import *
import requests
import random
from proxy import get_proxy


def read_user():
    with open("./user.txt", "r") as f:
        users = f.read()
    return list(map(lambda x: x.split(" "), users.split("\n")))


def read_url():
    with open("./url.txt", "r") as f:
        urls = f.read()
    return urls.split("\n")



if __name__ == "__main__":
    users = read_user()
    urls = read_url()

    for username, passwd in users:
        proxy = get_proxy()
        print("用户 {} (proxy: {})".format(username, proxy))

        weibo = WeiboLogin(username, passwd, proxy)
        session, data = weibo.login()
        print("{}({}) 登陆成功".format(data["username"], data["uid"]))

        for url in urls:
            result = report(session, url)
            print("举报结果: {}".format(result["msg"]))
