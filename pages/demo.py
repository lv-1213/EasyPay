import time, re, xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://172.16.100.115/Eviews/static/login.html")
driver.find_element_by_css_selector('[id="username"]').send_keys('10838')
driver.find_element_by_css_selector('[id="password"]').send_keys('123456')
driver.find_element_by_css_selector('[ng-click="login()"]').click()
driver.find_element_by_xpath('//*[text()="故障台数"]').click()
driver.find_element_by_xpath('//*[text()="故障记录"]').click()
time.sleep(1)
# ele=driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/select')
# Select(ele).select_by_index(1)
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/a').click()
# time.sleep(1)
# lis = driver.find_elements_by_css_selector('li[class="ng-scope status_normal"]')
# alist = []
# for li in lis:
#     spans = li.find_elements_by_tag_name("span")
#     for span in spans:
#         alist.append(span.text)
# if "纸币" in alist:
#     print("测试通过")
# driver.find_element_by_css_selector('[placeholder="设备编号"]:nth-of-type(3)').send_keys('225')
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/a').click()
driver.find_element_by_css_selector('[placeholder="故障码"]').send_keys("0502")

ele = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[2]/a[3]').text
time.sleep(2)
x = re.findall('/(.*?) ', ele, re.S)  # findall返回的是一个列表，故需要通过下标来取值
time.sleep(1)
workBook = xlwt.Workbook()
workSheet = workBook.add_sheet('Sheet1123')
lists = ["编号", "名称", "备注"]
for i in range(len(lists)):
    workSheet.write(0, i, lists[i])
list_txt = []
for i in range(5):  # (int(x[0])):
    lis = driver.find_elements_by_css_selector('li[class="ng-scope status_normal"]')
    for li in lis:
        alist = []
        li = li.find_elements_by_tag_name('span')
        for a in li:
            if a.text == '|':
                continue
            alist.append(a.text)
        list_txt.append(alist)
# print(list_txt)

d = 1            #初始化excel一个x坐标（因为第0行为表头，所以变量从1开始，每次循环+1）
for x in list_txt:
    print(x)
    # print(x+"+++++++++++++++++++++++++++")
    for y in range(len(x)):
        print(x[y])
        workSheet.write(d, y, x[y])
    d += 1

workBook.save("E:/exclaaaaaa123.xls")

'''
#点击查询
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/a').click()
time.sleep(0.5)
whithpage = driver.find_element_by_css_selector('#main [ng-show*="breakdown"] div[class="page"]>a:nth-child(3)').text
#点击下一页
driver.find_element_by_css_selector('#main [ng-show*="breakdown"] div[class="page"]>a:nth-child(4)').click()
time.sleep(0.5)
nextpage = driver.find_element_by_css_selector('#main [ng-show*="breakdown"] div[class="page"]>a:nth-child(3)').text
print(whithpage,nextpage)

# driver.quit()'''
