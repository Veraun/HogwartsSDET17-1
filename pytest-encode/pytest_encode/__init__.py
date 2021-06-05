# def pytest_collection_modifyitems(session, config, items) :
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

import logging
from typing import Tuple, Optional
import pytest

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='w'
                    )
logger = logging.getLogger(__name__)


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
        logger.info(f"item.name : {item.name}")
        logger.info(f"item._nodeid : {item._nodeid}")
        # 加标签
        # if "add" in item._nodeid:
        #     item.add_marker(pytest.mark.add)
        # elif 'div' in item._nodeid:
        #     item.add_marker(pytest.mark.div)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取方法的调用结果
    out = yield
    print('out >>>', out)
    # 钩子方法的调用结果中获取测试报告
    report = out.get_result()
    if report.when == "call":
        logger.info("encoding......")
        logger.info("用例名：%s" % report.nodeid)
        logger.info("运行结果：%s ***" % report.outcome)
        logger.info("运行完整描述：%s ***" % report.longreprtext)


