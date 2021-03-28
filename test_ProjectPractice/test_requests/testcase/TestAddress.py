'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: TestAddress.py
@time: 2021/3/28 19:33
@Email: Warron.Wang
'''
import pytest

from test_ProjectPractice.test_requests.wework.WeWorkAddress import WeWorkAddress


class TestAddress:
    name = "warron_"
    def setup_class(self):
        self.address = WeWorkAddress()
        # 初始化 测试数据
        self.user_id = "warron018"
        # self.name = "沃伦"
        self.mobile = "13671890000"
        self.department = [1]

    def setup(self):
        self.address.delete_member(self.user_id)

    def teardown(self):
        self.address.delete_member(self.user_id)

    # 获取通讯录某个成员
    def test_get_information(self):
        # 数据处理
        # 先调新增成员接口
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)

        # 用户信息是否正确
        r = self.address.get_information(self.user_id)
        # print(r)
        assert r["name"] == self.name


    def test_create_member(self):
        r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        assert r.get("errmsg") == "created"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info["name"] == self.name

    @pytest.mark.parametrize("new_name", [name+"tmp1", name+"tmp2", name+"tmp3", name+"tmp4"])
    def test_update_member(self, new_name):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        # new_name = self.name + 'tmp'
        r = self.address.update_member(self.user_id, new_name)
        assert r.get("errmsg") == "updated"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info["name"] == new_name

    def test_delete_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_member(self.user_id)
        assert r.get("errmsg") == "deleted"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info["errcode"] == 60111