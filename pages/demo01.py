from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
'''
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    ele =  WebDriverWait(driver,5,0.5).until(ec.presence_of_element_located((By.ID,'kw1')))
    ele.send_keys("00")
except Exception as e:
    driver.quit()
    raise e
# ec._find_element((By.ID,'kw1'))
# ec.presence_of_element_located((By.ID,'kw1')
'''
class A():
    def b(self):
        print(1)
        return self
print(A())
