'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: editcontact_page.py
@time: 2021/3/9 22:37
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage


class EditContactPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def edit_contact(self, name, phonenum):
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

    def verify_ok(self, text, message=""):
        try:
            self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            print(f"{message} 成功")
        except Exception as e:
            print(f"{message} 失败，原因：{e}")
        finally:
            self.backward(MobileBy.XPATH, "//*[@text='工作台']")