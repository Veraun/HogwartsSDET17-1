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
    - pip install -r requirement.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
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
 
