## 项目介绍
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
- requirement.txt：插件和依赖项，它们需要安装在您的虚拟环境中
    - pip install -r requirement.txt
- pytest.ini：一些有用的命令行，包括addopts设置和诱人的报告生成，它们会在程序启动时自动激活
- Testcases：主要测试用例文件夹 
  - test_calculator.py：主要测试用例
    - 使用夹具和屈服功能代替设置和拆卸
    - 将诱惑力描述添加到测试用例中，使其在诱惑力报告中更具可读性 
  - conftest.py：包括get_data代码，可以使用pytest自动激活那些公共功能
  - report.log：由记录器挂钩生成
  - reports/allure_results：使用pytest.ini设置自动生成
    - 与检查 allure serve reports/allure_results
  - datas：使用yaml格式测试数据，测试用例驱动数据
- pythoncode：重用的公共功能
  - Calculator.py：计算器功能
- pytest-encode：创建有关编码和记录器功能的挂钩
  - 随意使用以下命令安装此插件：
    - pip install dist/pytest_encode-1.0-py3-none-any.whl
  - 安装后，您可以很高兴地检查生成的日志并在代码egids中使用中文