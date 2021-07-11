from test_feishu.feishu.base import Base


class FeishuCalendar(Base):
    def get_information(self):
        """
        获取日历列表
        :param
        :return:
        """
        headers = {"Authorization": "Bearer " + self.token,
                   "content-type": "application/json; charset=utf-8"}
        r = self.send("GET", f"https://open.feishu.cn/open-apis/calendar/v4/calendars",headers = headers)
        return r.json()

    def create_calendar(self, summary: str, description: str, permissions: str, color: int, summary_alias: str):
        """
        创建日历
        :param :
        :param
        :param
        :return:
        """
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars"
        headers = {"Authorization": "Bearer " + self.token,
                   "content-type": "application/json; charset=utf-8"}
        data = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias
        }
        r = self.send("POST", url, headers = headers, json=data)
        return r.json()


    def delete_calendar(self, calendar_id):
        params = {"calendar_id": calendar_id}
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/:calendar_id'
        r = self.send("DELETE", url, params=params)
        return r.json()



if __name__ == '__main__':
    r1 = FeishuCalendar().get_information()
    # r2 = FeishuCalendar().create_calendar()
    print(r1)