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
        self.driver.find_element(*loc.tab_password).click()
        self.driver.find_element(*loc.input_account).send_keys(username)
        self.driver.find_element(*loc.input_password).send_skys(password)
        self.driver.find_element(*loc.policy_checkbox).click()
        self.driver.find_element(*loc.login_button).click()
        text = self.driver.find_element(*loc.login_success_text).text  # 获取登录成功后页面的驾驶舱字串用来做校验
        return text

