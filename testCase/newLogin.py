#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lenovo'
__mtime__ = '2020/5/15'

"""
import re
import time

from conf import NumDevice,fault_code
from pages.basePage import Page


class LoginPage(Page):
    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)
        self.driver.get(self.url)
        # self.driver.maximize_window()
    def login(self,username,password):
        try:
            self.input_text(self.username_css,username)
            self.input_text(self.password_css,password)
            self.click_element(Page.button_css)
            time.sleep(0.5)
            return self.get_url()
        except Exception as e:
            self.get_web_picture("E:/%s.png" %e)

    def search(self):
    #点击故障台数
        self.click_element(self.xpathNum)
        time.sleep(3)



class Test(Page):
    def __init__(self,driver):
        super(Test,self).__init__(driver)
        self.click_element(Page.xpathRecord)
    '''  #定义点击进入故障记录页面方法
    def record(self):
        self.click_element(Page.xpathRecord)
        return self
    '''
    def dataSelect(self):
        #选择结束时间为今天
        self.click_element(Page.datatime_css)
        time.sleep(0.5)
        self.click_element(Page.nowtime_xpath)
        #选择下拉框
        self.select_option(Page.select_css,"纸币")
        #点击查询
        self.click_element(Page.query_xpath)
        self.click_element(Page.ssss)
        time.sleep(3)

    def deviceSearch(self):
        self.input_text(Page.inputNum_css,NumDevice)
        self.click_element(Page.query_xpath)
    def excelData(self):
        #点击故障记录，导出页面所有的设备故障信息到exls
        # self.click_element(Page.xpathRecord)
        #输入故障码
        self.input_text(Page.faultcode_css,fault_code)
        self.click_element(Page.query_xpath)
        ele = self.get_webelement(Page.numberpage_xpath).text
        time.sleep(0.5)
        x = re.findall('/(.*?) ', ele, re.S)
        list_txt = []
        for i in range(int(len(x))):
            lis = self.get_webelements(Page.list_css)
            for li in lis:
                alist = []
                li = self.element_element(li,"span")
                for a in li:
                    if a.text == '|':
                        continue
                    alist.append(a.text)
                list_txt.append(alist)
        print(list_txt)
