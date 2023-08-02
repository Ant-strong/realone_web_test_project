#!/usr/bin/python3
# -*- coding: uft-8 -*-
# @Author : ZM

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# 浏览器操作
class BrowserDriver(object):
    drivers_base_path = os.getcwd() + os.sep + 'drivers'
    chrome_driver_path = drivers_base_path + 'chromedriver.exe'

    def open_browser(self, url):

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized') # 窗口最大化启动
        browser = webdriver.Chrome()