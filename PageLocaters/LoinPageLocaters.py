# 封装集成平台项目端首页的元素
from selenium.webdriver.common.by import By


class LoginElement(object):

    tab_password = (By.ID, 'tab_password')
    input_account = (By.ID, 'el-id-308-7')
    input_password = (By.ID, 'el-id-308-8')
    login_button = (By.CLASS_NAME, 'el-button el-button--primary el-button--large is-disabled bottom-btn')
    policy_checkbox = (By.CLASS_NAME, 'el-checkbox_inner')
    login_error_message = (By.XPATH, '//*[@id="pane-password"]/form/div[1]/div/span')


class LoginPhoneElement(object):

    input_phone = (By.ID, 'el-id-308-9')
    input_verification_code = (By.ID, 'el-id-308-10')
    button_verification_code = (By.CLASS_NAME, 'el-button send-code')
    tab_phone = (By.ID, 'tab-phone')
    login_phone_error_message = (By.XPATH, '//*[@id="pane-phone"]/form/div[1]/div/span')
