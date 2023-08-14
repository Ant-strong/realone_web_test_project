#!/usr/bin/python3
# @Author : ZM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from selenium.webdriver import Chrome

drivers_base_path = os.getcwd() + os.sep + 'drivers' + os.sep
chrome_driver_path = drivers_base_path + 'chromedriver.exe'
options = Options()
options.add_argument('--start-maximized')
options.binary_location = chrome_driver_path


# 浏览器操作
class BrowserDriver(object):
    # chromedriver地址

    def __init__(self):
        self.driver = None

    def open_browser(self, url):
        # options = Options()  # options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')  # 窗口最大化启动
        # options.binary_location = chrome_driver_path

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.get(url)  # 打开网页
        sleep(10)
        page_title = self.driver.title
        return page_title

# 关闭浏览器
    def close_browser(self):
        self.driver.quit()


class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome(options=options)  # 在这里初始化 webdriver
        return cls._instance

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    x = BrowserDriver()
    x.open_browser('https://www.baidu.com')
    sleep(3)
    x.close_browser()
