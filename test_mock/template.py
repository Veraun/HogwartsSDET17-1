import requests
def request_demo():
    res = requests.request(method="GET", url="https://stock.xueqiu.com/v5/stock/stare/notice.json?_t=1NETEASEb20b9d59c2ee254b8d246e70128389c5.1127230531.1616403769052.1616403785890&_s=29d998&x=0.178&stare_type=dynamic%2Cevent")


if __name__ == '__main__':
    request_demo()