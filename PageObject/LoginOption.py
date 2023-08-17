# 登录测试各测试用例的执行步骤

# 导入测试前提需求
import selenium
from selenium import webdriver
from BaseMethod.BrowserOption import *  # 导入浏览器打开关闭方法
from PageLocaters.LoinPageLocaters import *  # 导入登录界面的定位元素
# from TestDatas.LoginData import *  # 导入测试数据
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from TestDatas.LoginData import *


loc = LoginElement()
loc_phone = LoginPhoneElement()
driver_singleton = WebDriverSingleton()


class LoginTabPassword(BrowserDriver):

    def login_success(self, username, password, url):
        driver = driver_singleton.get_driver()
        driver.get(url)
        sleep(4)
        driver.save_screenshot(r'{}\screenshot\open_url.png'.format(screenshot_path))
        driver.find_element(*loc.input_account).send_keys(username)
        driver.find_element(*loc.input_password).send_keys(password)
        driver.find_element(*loc.policy_checkbox).click()
        driver.save_screenshot(r'{}\screenshot\before_login.png'.format(screenshot_path))
        driver.find_element(*loc.login_button).click()
        sleep(10)
        driver.save_screenshot(screenshot_path + 'screenshot\\after_login.png')
        text = driver.find_element(*loc.login_success_text).text  # 获取登录成功后页面的驾驶舱字串用来做校验
        return text
