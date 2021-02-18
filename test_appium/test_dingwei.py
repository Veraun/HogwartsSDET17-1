'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_dingwei.py
@time: 2021/2/18 17:15
@Email: wei1.wang@ximalaya.com
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true' #去掉页面弹窗
desired_caps['dontStopAppOnReset'] = 'true'  #启动时不停止app(提升app运行速度)
desired_caps['skipDeviceInitialization'] = 'true'  #跳过安装、权限设置等操作(提升app运行速度)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))


driver.implicitly_wait(10) #隐式等待(全局性)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
driver.back() #返回上一个页面
driver.back() #返回上一个页面
driver.quit()


