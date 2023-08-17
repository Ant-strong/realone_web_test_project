# 首页执行操作

from PageLocaters.FirstPageLocaters import *
from BaseMethod.BrowserOption import *
from TestDatas.LoginData import *
from PageLocaters.LoinPageLocaters import *
from selenium.common.exceptions import NoSuchElementException   # 处理无元素异常


driver_singleton = WebDriverSingleton()
driver = driver_singleton.get_driver()
loc = FirstPage()
loc1 = LoginElement()  # 登录页面的定位元素


#  验证进入驾驶舱进入全屏模式
def full_screen():
    driver.get(login_url)
    driver.find_element(*loc.full_screen).click()
    try:
        text = driver.find_element(*loc1.login_success_text).text
    except NoSuchElementException:
        text = 'PASS'
    if text == 'PASS':
        driver.
    return text

#  验证退出驾驶舱全屏模式
def cancel_full_screen():

