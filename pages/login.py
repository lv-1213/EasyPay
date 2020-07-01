import time,xlwt,re
from selenium import webdriver
from pages.doexcel import readExcel
from pages.basePage import Page
from conf import NumDevice,title,path,fault_code

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
            self.get_web_picture("E:/%s.png" %"元素定位失败")
# class FaultLog(Page):
    def search(self):
        # 点击故障台数
        self.click_element(self.xpathNum)
        # 点击故障记录
        self.click_element(Page.xpathRecord)
    def dataSelect(self):
        #点击故障记录
        self.click_element(Page.xpathRecord)
        #选择结束时间为今天
        self.click_element(Page.datatime_css)
        time.sleep(0.5)
        self.click_element(Page.nowtime_xpath)
        #选择下拉框
        self.select_option(Page.select_css,"纸币")
        #点击查询
        self.click_element(Page.query_xpath)
    #输入设备编号点击查询
    def deviceSearch(self):
        self.click_element(Page.xpathRecord)
        self.input_text(Page.inputNum_css,NumDevice)
        self.click_element(Page.query_xpath)
    #开始结束都为今天
    def today(self):
        self.click_element(Page.xpathRecord)
        self.click_element(Page.starttime_css)
        time.sleep(0.5)
        self.click_element(Page.nowtime_xpath)
        self.click_element(Page.query_xpath)
    def excelData(self):
        #点击故障记录，导出页面所有的设备故障信息到exls
        self.click_element(Page.xpathRecord)
        #输入故障码
        self.input_text(Page.faultcode_css,fault_code)
        self.click_element(Page.query_xpath)
        ele = self.get_webelement(Page.numberpage_xpath).text
        time.sleep(0.5)
        x = re.findall('/(.*?) ', ele, re.S)
        list_txt = []
        for i in range(int(x[0])):
            lis = self.get_webelements(Page.list_css)
            for li in lis:
                alist = []
                li = self.element_element(li,"span")
                # li = li.find_elements_by_tag_name('span')
                for a in li:
                    if a.text == '|':
                        continue
                    alist.append(a.text)
                list_txt.append(alist)
        readExcel(title,list_txt,path)

    #测试翻页功能
    def turnPage(self):
        self.click_element(Page.xpathRecord)
        time.sleep(0.5)
        whithpage = self.get_webelement(Page.howpage).text
        self.click_element(Page.nextpage)
        nextpage = self.get_webelement(Page.howpage).text
        return whithpage,nextpage


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     # driver.find_element_by_xpath().click()
#     lp= LoginPage(driver)
#     lp.login("10838","123456")
#     lp.dataSelect()

