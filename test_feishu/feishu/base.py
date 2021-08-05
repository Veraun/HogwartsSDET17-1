import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        params = {"app_id": "cli_a06fdb373efb100b",
                  "app_secret": "YMw4bRJOfxeOsh58rShffQhIJQaeSVqr"}
        r = self.s.post(url, headers=headers, params=params)
        print(r.json())
        return r.json()['tenant_access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)

#
# if __name__ == '__main__':
#     b = Base()
#     print(b.token())
