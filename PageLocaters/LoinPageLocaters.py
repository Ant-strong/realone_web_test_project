# 封装集成平台项目端首页的元素
from selenium.webdriver.common.by import By


class LoginElement(object):

    tab_password = (By.ID, 'tab_password')
    input_account = (By.XPATH, '//input[1]')
    input_password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    login_button = (By.XPATH, '//div[@class="form-bottom"]/button')
    policy_checkbox = (By.XPATH, '//span[@class="el-checkbox__input"]')
    login_error_message = (By.XPATH, '//*[@id="pane-password"]/form/div[1]/div/span')
    login_success_text = (By.XPATH, '//*[@class="header-title"]')


class LoginPhoneElement(object):

    input_phone = (By.ID, 'el-id-308-9')
    input_verification_code = (By.ID, 'el-id-308-10')
    button_verification_code = (By.CLASS_NAME, 'el-button send-code')
    tab_phone = (By.ID, 'tab-phone')
    login_phone_error_message = (By.XPATH, '//*[@id="pane-phone"]/form/div[1]/div/span')
