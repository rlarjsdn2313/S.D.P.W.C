import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def ChangeIP():
    os.system('/etc/init.d/tor restart')
    time.sleep(1)

chrome_options = Options()
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
driver = webdriver.Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)

driver.get('http://icanhazip.com/')

ChangeIP()
driver.quit()

chrome_options = Options()
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
driver = webdriver.Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)

driver.get('http://icanhazip.com/')
time.sleep(3)
driver.quit()

ChangeIP()

