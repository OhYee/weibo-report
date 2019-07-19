import time
import requests
import re


def get_timestamp():
    return int(time.time()*1000)


def report(session,  url):
    body = session.get(url).text
    form_data = re.findall(
        r"<input type='hidden' id='extra_data' node-type='extra_data' value='(.*)'/>",
        body
    )[0]
    # print(body,form_data)

    data = {}
    for key, value in map(lambda x: x.split("="), form_data.split("&")):
        data[key] = value

    rep = session.post(
        "https://service.account.weibo.com/aj/reportspamobile?__rnd={}".format(
            get_timestamp()
        ),
        {
            "category": 8,
            "tag_id": 804,
            "url": data["url"],
            "type": data["type"],
            "rid": data["rid"],
            "uid": data["uid"],
            "r_uid": data["r_uid"],
            "from": data["from"],
            "getrid": data["getrid"],
            "appGet": 0,
            "weiboGet": 0,
            "blackUser": 0,
            "_t": 0,
        },
        headers={
            "referer": url,
        }
    )

    return rep.json()
