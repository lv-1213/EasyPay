import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
class Page:
    username_css = ["css selector", '[id="username"]']
    password_css = ["css selector", '[id="password"]']
    button_css = ["css selector", '[ng-click="login()"]']
    url = "http://172.16.100.115/Eviews/static/login.html"
    #故障台数
    xpathNum = ["xpath",'//*[text()="故障台数"]']
    #故障记录
    xpathRecord = ["xpath", '//*[text()="故障记录"]']
    list_css = ["css selector",'li[class="ng-scope status_normal"]']
    starttime_css = ["css selector",'.search>input[placeholder="开始日期"]']
    datatime_css=["css selector",'.search>input[placeholder="结束日期"]']
    nowtime_xpath = ["xpath",'//*[text()="今天"]']
    #设备类型
    select_css = ["xpath",'//*[@id="main"]/div[1]/div[3]/div/div[1]/select']
    #查询按钮
    query_xpath = ["xpath",'//*[@id="main"]/div[1]/div[3]/div/div[1]/a']
    #输入设备编号
    inputNum_css = ["css selector",'[placeholder="设备编号"]:nth-of-type(3)']
    #页面展示多少条数据
    statsdata_xpath=["xpath",'//*[@id="main"]/div[1]/div[3]/div/div[2]/a[6]']
    #页面共多少页
    numberpage_xpath=["xpath",'//*[@id="main"]/div[1]/div[3]/div/div[2]/a[3]']

    #故障码
    faultcode_css = ["css selector",'[placeholder="故障码"]']
    #tag_NAME
    tagName = ["tag name","span"]
    #第几页
    howpage =["css selector",'#main [ng-show*="breakdown"] div[class="page"]>a:nth-child(3)']
    #下一页按钮
    nextpage = ["css selector",'#main [ng-show*="breakdown"] div[class="page"]>a:nth-child(4)']

    ssss = ["xpath",'//*[@id="body"]/div[2]/ul/li[2]/a']

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)
    def element_element(self,li,a):
        return li.find_elements_by_tag_name(a)

    def get_web_picture(self,userpath):
        self.driver.get_screenshot_as_file(userpath)
    #点击
    def click_element(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()
    #清空
    def clear_element(self, locator):
        self.driver.find_element(locator[0], locator[1]).clear()
    #输入
    def input_text(self, locator, text):
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)
    # 获取复数元素
    def get_webelements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])
    # 获取单数元素
    def get_webelement(self, locator):
        return self.driver.find_element(locator[0], locator[1])
    # 选择下拉框
    def select_option(self, locator, option):
        select = Select(self.get_webelement(locator))
        select.select_by_visible_text(option)
    def get_url(self):
        time.sleep(1)
        return self.driver.current_url
    # 关闭浏览器
    def closr_browser(self):
        self.driver.quit()
