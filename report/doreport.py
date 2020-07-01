from ClassicHTMLTestRunner import HTMLTestRunner
import unittest
from  testCase.test01 import TestEasyPay
suite = unittest.defaultTestLoader.discover("testCase",pattern="test01.py")
report = open(r"E:/EasyPay测试报告.html","wb")
runner001=HTMLTestRunner(stream=report,verbosity=3,description='用例执行详细信息',title='测试报告',tester='lv同学')
runner001.run(suite)