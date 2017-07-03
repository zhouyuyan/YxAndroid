#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/19 14:35
# coding=utf-8

import unittest
import os
import HTMLTestRunner
from Common.sendmail import *

# 遍历测试用例
from Common.yunxiCommon import writeLog


def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = 'D:\\workspace\\YxAndroid\\TestCase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for testcase in discover:
        testunit.addTests(testcase)
    return testunit


# 生成测试报告
now = time.strftime('%Y-%m-%d_%H-%M-%S')
filename = 'D:\\workspace\\YxAndroid\\report\\' + now + '.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'yunxizhibo_Android测试报告' + now, description=u'测试结果')


def sendreport():
    # 获取最新的报告
    report_dir = 'D:\\workspace\\YxAndroid\\report\\'
    lists = os.listdir(report_dir)
    lists.sort()
    file_new = os.path.join(report_dir, lists[-1])
    sendmail(file_new)


if __name__ == '__main__':
    runner.run(creatsuite())

    fp.close()
    time.sleep(3)
    sendreport()
