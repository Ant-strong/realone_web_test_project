# \TestCases\test_login.py
import pytest
from PageObject.LoginOption import *
from BaseMethod.BrowserOption import *
from TestDatas.LoginData import *


class TestLoginPword:

    @pytest.fixture
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        # 这里可以添加一些代码来保持浏览器窗口打开
        input("Press Enter to close the browser...")
        driver.quit()

    def test_open_website(self):
        h = BrowserDriver()
        title = h.open_browser(open_url)
        assert title == '医院安全生产管理平台', '网页打开失败'

    def test_login_success(self):
        h = LoginTabPassword()
        result = h.login_success(TabPasswordData.user_name['correct_name'],
                                 TabPasswordData.user_password['correct_password'],
                                 open_url)
        assert result == '驾驶舱', '登录失败'
