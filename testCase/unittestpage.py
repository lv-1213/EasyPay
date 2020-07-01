#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Lenovo'
__mtime__ = '2020/5/15'

"""
import conf
from selenium import webdriver
from pages.basePage import Page
from testCase.newLogin import LoginPage,Test
import unittest
class demo(unittest.TestCase,Page):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test2(self):
        self.lp.login(conf.username,conf.password)
    def test3(self):
        self.lp.search()

    def test4(self):
        Test(self.driver).dataSelect()


    def test5(self):
        Test(self.driver).excelData()