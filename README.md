## 第一部分---pytest实战
霍格沃兹测开17期实战演练---计算器

## 霍格沃兹论坛
- [测试人论坛](https://ceshiren.com/)

## 目的
- Pytest框架实战
- 计算器功能实战

## 参考链接
pytest：https://docs.pytest.org/en/stable/getting-started.html

## 西西老师课堂资源
- https://ceshiren.com/t/topic/9879
- https://ceshiren.com/t/topic/9936

## 个人作业地址
- https://github.com/wiki918/HogwartsSDET17.git

## 项目框架结构
- Testcases：主要测试用例文件夹 
  - test_calculatorNew.py：主要测试用例
    - 使用fixture进行参数化
    - 引入allure测试组件添加到测试用例中，使其在报告中更具可读性 
  - conftest.py：包括get_data代码，使用pytest可以自动激活
  - report.log：由编写的logger自定义的fixture生成
  - reports/allure_results：使用pytest.ini设置自动生成
    - 与检查 allure serve reports/allure_results
  - datas：使用yaml格式测试数据，让测试用例管理更人性化
- pythoncode：被测方法目录
  - Calculator.py：计算器功能
- pytest-encode：有关编码和日志的自定义fixture
  - 使用以下命令安装此插件：
    - pip install dist/pytest_encode-1.0-py3-none-any.whl
  - 安装后，您可以使用日志和中文用例显示功能
- requirement.txt：插件和依赖项，它们需要安装在您的虚拟环境中
    - 安装：pip install -r requirement.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
    - 导出：pip freeze > requirements.txt
- pytest.ini：一些有用的命令行，包括addopts设置和诱人的报告生成，它们会在程序启动时自动激活

## 使用Allure报告
- 1. 安装 allure2
- 2. Allure help  帮助文档 
- 3. 生成 allure 测试结果 ：切到用例执行文件下，如testing文件下。
  - pytest —alluredir=./report/allure_results
- 4. 展示报告：allure serve ./report/allure_results
- 5. 生成最终版本的报告：   allure generate ./report/allure_results
- 6. 在本地搭建一个网站服务（例如：Django）
  - python manage.py runserver  (http://127.0.0.1:8000/)
  

************************************************
************************************************


## 第二部分---selenium实战
selenium实战联演

## 项目框架结构
- selenium_demo：测试demo
- selenium_event:各种事件
- selenium_frame_window:多窗口、frame
- selenium_file_alert:文件上传、alert弹窗
- selenium_js:js操作

************************************************
************************************************ 
 
## 第三部分---appium实战

### 环境准备
- jdk 1.8版本
- Android sdk
- Nodejs(>=10版本)、npm(>=6版本)
- python3
- appium-desktop
- Appium python client
- windows + 是夜神/木木这类模拟器 是需要手动adb connect一下
- mac + 是夜神/木木这类模拟器 ,只需adb kill-server，然后再adb devices

### 常用命令
#### app信息
- 获取当前界面元素:adb shell dumpsys activity top（推荐）（重点）
- 获取任务列表:adb shell dumpsys activity activities
#### app入口
- 获取appPackage和appActivity：adb logcat | grep -i displayed （推荐）（重点）
如：02-18 16:07:42.819   479   690 I ActivityManager: Displayed com.xueqiu.android/.view.WelcomeActivityAlias: +5s97ms
- 在模拟器当前页面，获取appPackage和appActivity ： adb shell dumpsys window | grep mCurrent
- aapt dump badging mobike.apk | grep launchable-activity
- apkanalyzer最新版本的sdk中才有
#### 启动应用
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S （重点）

### 三种经典等待方式
#### 强制等待 
- sleep 不推荐
#### 隐式等待
- (全局性)生效
- 设置一个超时时间，服务端appium会在给定的时间内，不停地查找，默认值是0
- 用法：driver.implicitly_wait(10, TimeUnit.SECONDS)
- 在服务端等待
- 默认尽量加上，限定在3-6秒，为了所有的find_element方法都有一个很好的缓冲
#### 显示等待(等待某个元素)
- (局部)生效
- Element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))
- 在客户端等待
- 用来处理隐式等待无法解决的一些问题。如：文件上传
- 显示等待可以设置的长一点
### 定位方法
#### 测试步骤三要素
- 定位、交互、断言
#### 测试步骤三要素
- id定位
- accessibility_id定位
- xpath定位
- classname定位(不推荐)
### 定位工具
#### uiautomatorviewer工具(only android)
- 推荐使用
- sdk路径下的工具
#### Appium inspector工具

### 高阶定位方法
- uiautomator
  - self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("wiki")

- 滚动查找指定元素
  - self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("轻金融").'
                                                        'instance(0));').click()

### toast定位
- appium使用uiautomator底层的机制来分析抓取toast，并且把toast放到控件树里，但本身并不属于控件
- automatorName：uiautomator2
- 必须使用xpath查找
  - //*[@class='android.widget.Toast']
  - //*[contains(@text, 'popup menu item Search')]
  
### 属性获取
- print(search_ele.get_attribute("content-desc"))
- print(search_ele.get_attribute("resource-id"))
- print(search_ele.get_attribute("enabled"))
- print(search_ele.get_attribute("clickable"))
- print(search_ele.get_attribute("bounds"))

### 断言
- 普通断言
  - assert
- Hamcrest断言
  - github地址：https://github.com/hamcrest/PyHamcrest
  - hamcrest框架是一个为了测试为目的，能组合成灵活表达式的匹配器类库。
  - 提供了大量被称为"匹配器"的方法。每个匹配器都设计用于执行特定的比较操作
  - 支持多种语言。如java、python等
  
  
### 参数化用例
