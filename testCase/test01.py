import time,os,unittest,pathlib
from selenium import webdriver
from pages.basePage import Page
from pages.login import LoginPage
from conf import username,password,NewUrl,NumDevice,path

class TestEasyPay(unittest.TestCase,Page):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        cls.lp.closr_browser()
    def list_txt(self,locator,tag):
        time.sleep(1)
        lis = self.get_webelements(locator)
        self.alist = []
        for li in lis:
            li = li.find_elements_by_tag_name(tag)
            for a in li:
                self.alist.append(a.text)
        return self.alist
    def test01(self):
        #断言登录后URL是否正确
        self.assertEqual(self.lp.login(username, password), NewUrl)
    #测试故障记录页面数据不为空
    def test02(self):
        self.lp.search()
        #断言页面展示文本不为空
        self.assertIsNotNone(self.list_txt(self.list_css, "span"))
    #筛选结束日期为今天，设备类型为纸币
    def test03(self):
        self.lp.dataSelect()
        #断言页面文本包含“纸币”
        self.assertIn("纸币",self.list_txt(self.list_css, "span"))
    #输入设备编号点击查询
    def test05(self):
        self.lp.deviceSearch()
        self.assertIn(NumDevice, self.list_txt(self.list_css, "span"))
    #开始结束日期都选择今天
    def test04(self):
        self.lp.today()
        self.stats = self.get_webelement(Page.statsdata_xpath)
        self.assertIn('共',self.stats.text)
    #翻页查看设备记录并输出到excel
    def test06(self):
        self.lp.excelData()
        # 断言文件路径是否存在
        # self.assertTrue(os.path.exists(path))
        # 断言文件是否可读R，W可写入，X可执行（存取）
        # self.assertTrue(os.access(path, os.R_OK))
        self.assertTrue(os.access(path, os.X_OK))
    #断言翻页功能
    def test07(self):
        whithpage,nextpage = self.lp.turnPage()
        self.assertEqual(whithpage,nextpage)
        # self.assertTrue(self.lp.turnPage())

    #     ele = Page.xpathRecord