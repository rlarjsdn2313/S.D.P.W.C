import os
import time

from selenium import webdriver

def ChangeIP():
    os.system('/etc/init.d/tor restart')
    time.sleep(1)

driver = webdriver.Firefox(executable_path=f'{os.getcwd()}/geckodriver')

driver.get('http://icanhazip.com/')
print(driver.page_source)
driver.quit()
