'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_jiaohu.py
@time: 2021/3/11 14:07
@Email: Warron.Wang
'''
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaohu:
    def setup(self):
        desirecaps = {}
        desirecaps['platformName'] = "android"
        desirecaps['platformVersion'] = "6.0"
        desirecaps['deviceName'] = "emulator-5554"
        desirecaps['appPackage'] = "com.tencent.wework"
        desirecaps['appActivity'] = ".launch.LaunchSplashActivity"
        desirecaps['unicodeKeyBoard'] = "true"
        desirecaps['resetKeyBoard'] = "true"
        desirecaps['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desirecaps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # 测试过程中模拟来电
        self.driver.make_gsm_call('13524630000', GsmCallActions.CALL)
        # 测试过程中模拟来短信
        self.driver.send_sms('13524630000', 'hello appium api')
        # 测试过程中模拟切换网络
        self.driver.set_network_connection(1)
        # 测试过程中截图
        self.driver.get_screenshot_as_file('./photos/img.png')
        # 测试过程中模拟开始视频录制
        self.driver.start_recording_screen()
        # 测试过程中模拟结束视频录制
        self.driver.stop_recording_screen()


