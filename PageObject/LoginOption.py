# 登录测试各测试用例的执行步骤

# 导入测试前提需求
import selenium
from selenium import webdriver
from BaseMethod.BrowserOption import *  # 导入浏览器打开关闭方法
from PageLocaters.LoinPageLocaters import *  # 导入登录界面的定位元素
# from TestDatas.LoginData import *  # 导入测试数据
from selenium.webdriver.support.wait import WebDriverWait


loc = LoginElement()
loc_phone = LoginPhoneElement()


class LoginTabPassword(BrowserDriver):

    def login_success(self, username, password):
        self.implicitly_wait(10)
        self.driver.find_element(*loc.tab_password).click()
        self.driver.find_element(*loc.input_password)

