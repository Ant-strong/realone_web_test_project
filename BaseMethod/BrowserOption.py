#!/usr/bin/python3
# -*- coding: uft-8 -*-
# @Author : ZM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# 浏览器操作
class BrowserDriver(object):

    def open_browser(self, url):
        drivers_base_path = os.getcwd() + os.sep + 'drivers'
        chrome_driver_path = drivers_base_path + 'chromedriver.exe'

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # 窗口最大化启动
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        self.driver.get(url) # 打开网页
