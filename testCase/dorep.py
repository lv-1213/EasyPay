#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lenovo'
__mtime__ = '2020/5/15'

"""
from ClassicHTMLTestRunner import HTMLTestRunner
import unittest
suite = unittest.defaultTestLoader.discover("testCase",pattern="unittestpage.py")
report = open(r"E:/123456测试报告.html","wb")
runner001=HTMLTestRunner(stream=report,verbosity=3,description='用例执行详细信息',title='测试报告',tester='lv同学')
runner001.run(suite)