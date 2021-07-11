from test_feishu.feishu.base import Base


class FeishuOkr(Base):
    def get_information(self):
        """
        获取OKR周期列表信息
        :param
        :return:
        """
        print(self.token)
        headers = {"Authorization":"Bearer " + self.token}
        r = self.send("GET", "https://open.feishu.cn/open-apis/okr/v1/periods", headers=headers)# params=params
        return r.json()


    def get_user_information(self, user_id: str):
        """
        获取某个用户的OKR周期列表信息
        :param
        :return:
        """
        url = "https://open.feishu.cn/open-apis/okr/v1/users/:%s/okrs" % user_id
        print(url)
        params = {
            "user_id_type": user_id,
            "offset": "0",
            "limit": "10",

        }
        headers = {"Authorization":"Bearer " + self.token}
        r = self.send("GET", url=url, headers=headers, params=params)# params=params
        return r.json()



if __name__ == '__main__':
    r = FeishuOkr().get_user_information("1c7dggga")
    print(r)