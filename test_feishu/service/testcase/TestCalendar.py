import pytest

from test_feishu.feishu.feishu_calendar import FeishuCalendar


class TestCalendar:

    def setup_class(self):
        self.address = FeishuCalendar()
        self.summary= "测试warron日历"
        self.description= "使用开放接口创建日历"
        self.permissions= "private",
        self.color= -1,
        self.summary_alias= "日历备注名0711"
        self.calendar_id = "feishu.cn_aNfvq85qwPLOMnyX1dfSHg@group.calendar.feishu.cn"


    def teardown_class(self):
        self.address.delete_calendar(self.calendar_id)


    def test_get_information(self):
        # 数据处理
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)

        # 用户信息是不是正确
        r = self.address.get_information(self.user_id)
        assert r["name"] == self.name

    def test_crate_calendar(self):
        r = self.address.create_calendar(self.summary, self.description, self.permissions, self.color, self.summary_alias)
        print(r)
        # 断言
        assert r.get("code") == 0



    def test_delete_calendar(self):
        r = self.address.create_calendar(self.summary, self.description, self.permissions, self.color, self.summary_alias)
        r = self.address.delete_calendar(self.calendar_id)
        assert r.get("errmsg") == "deleted"

