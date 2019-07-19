import requests


def check_proxy(proxy):
    try:
        data = requests.get(
            "http://ip-api.com/json",
            proxies={
                "http": proxy,
                "https": proxy,
            },
            timeout=(5, 5)
        ).json()
        print(data)
        return proxy.split(":")[0] == data["query"] and (data["country"] == "China" or data["country"] == "Hong Kong")
    except:
        return False


def get_proxy():
    while 1:
        proxy = requests.get("http://118.24.52.95:5010/get").text
        if check_proxy(proxy):
            return proxy

if __name__ == "__main__":
    get_proxy()
