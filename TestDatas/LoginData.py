# 存放登录页面测试数据

def tab_password_data():
    user_name = {"correct_name": "admin", "wrong_name": "aaaaa"}
    user_password = {"correct_password": "123456", "wrong_password": "aaaaa"}
    check_message = {"wrong_user_password": "用户不存在/密码错误"}


def phone_password_data():
    phone_number = {"correct_number": "18661285711", "wrong_number": "186612877777"}
    verification_code = {"wrong_code": "a11111"}
    check_message = {"wrong_ver_code": "验证码错误", "wrong_nuber": "输入正确的手机号码", "timeout_ver_code": "验证码已失效"}