'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_market.py
@time: 2021/3/12 09:09
@Email: Warron.Wang
'''
from ui_framework.page.app import App


class TestMarket:
    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_goto_market(self):
        self.main.goto_market()
