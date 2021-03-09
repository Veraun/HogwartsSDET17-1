'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_contact.py
@time: 2021/3/9 22:54
@Email: Warron.Wang
'''
import pytest
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        try:
            name = "hogwarts5"
            phonenum = "13100000005"
            editpage = self.main.goto_addresslist().click_addcontact().addcontact_menual()
            editpage.edit_contact(name, phonenum)
            editpage.verify_ok()
        except Exception as e:
            print(e)
        finally:
            self.app.goto_main().backward(MobileBy.XPATH, "//*[@text='工作台']")

    @pytest.mark.skip
    def test_delcontact(self):
        try:
            search_name = "hogwarts_3"
            func_name = "删除成员"
            search_page = self.main.goto_addresslist().goto_search()
            element_len, personPage = search_page.search_and_click(search_name)
            personPage.click_more().edit_person().del_contact()
        finally:
            # 保证后续正常运行
            self.app.goto_main().backward(MobileBy.XPATH, "//*[@text='工作台']")
