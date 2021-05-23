import os
from lib.ChangeIP import ChangeIP
from lib.Get import Get

from selenium import webdriver



get = Get()
password = get.GetPassword()
port = get.GetPort()

changer = ChangeIP(password, port)

driver = webdriver.Firefox(firefox_profile=changer.SetProfile(), executable_path=f'{os.getcwd()}/geckodriver')


driver.quit()

