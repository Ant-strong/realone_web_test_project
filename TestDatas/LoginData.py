# 存放登录页面测试数据
import os

open_url = 'http://192.168.42.245/rcms'
login_url = 'http://192.168.42.245/rcms/#/index'
screenshot_path = os.getcwd() + os.sep


class TabPasswordData:
    user_name = {"correct_name": "admin", "wrong_name": "aaaaa"}
    user_password = {"correct_password": "123456", "wrong_password": "aaaaa"}
    check_message = {"wrong_user_password": "用户不存在/密码错误"}


class PhonePasswordData:
    phone_number = {"correct_number": "18661285711", "wrong_number": "186612877777"}
    verification_code = {"wrong_code": "a11111"}
    check_message = {"wrong_ver_code": "验证码错误", "wrong_nuber": "输入正确的手机号码",
                     "timeout_ver_code": "验证码已失效"}
