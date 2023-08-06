#!/usr/bin/python3
# @Author : ZM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep


# 浏览器操作
class BrowserDriver(object):
    # chromedriver地址
    drivers_base_path = os.getcwd() + os.sep + 'drivers' + os.sep
    chrome_driver_path = drivers_base_path + 'chromedriver.exe'

    def __init__(self):
        self.driver = None

    def open_browser(self, url):
        options = Options()  # options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # 窗口最大化启动
        options.binary_location = self.chrome_driver_path

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)  # 打开网页
        sleep(10)

# 关闭浏览器
    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    x = BrowserDriver()
    x.open_browser('https://www.baidu.com')
    sleep(3)
    x.close_browser()
