# \TestCases\test_login.py
import pytest
from PageObject.LoginOption import *
from BaseMethod.BrowserOption import *
from TestDatas.LoginData import *


class TestLoginPword:
    def test_open_website(self):
        h = BrowserDriver()
        title = h.open_browser(open_url)
        assert title == '医院安全生产管理平台', '网页打开失败'

    def test_login_success(self):
        h = LoginTabPassword()
        result = h.login_success(tab_password_data().)
        assert result == '驾驶舱', '登录失败'
