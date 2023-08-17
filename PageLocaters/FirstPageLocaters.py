# 首页的元素集合
from selenium.webdriver.common.by import By


class FirstPage(object):

    full_screen = (By.XPATH, '//*[@class="header-title"]/div/button')
    personal_cockpit_button = (By.ID, 'tab-2')  # 个人驾驶舱按钮元素
    per_cockpit_edit_button = (By.XPATH, '//*[@class="header-title"]/div/button[2]')
    edit_page_message = (By.XPATH, '//*[@class="header-title"]')  # 编辑驾驶舱页面的校验信息
    cancel_button = (By.XPATH, '//*[@class="header-title"]/div/button')  # 取消按钮
    save_button = (By.XPATH, '//*[@class="header-title"]/div/button[2]')  # 保存按钮
    space_button = (By.XPATH, '//*[@role="tablist"]/div/div/div')  # 空间按钮
    space_statistical_element = (By.XPATH, '//*[@role="tablist"]/div/div[2]')  # 空间简易统计组件
    cockpit_canvas = (By.XPATH, '//*[@class="grid-content"]')  # 驾驶舱组件画布
