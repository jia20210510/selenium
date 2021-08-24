# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_web.py
# @Time: 8月 21, 2021
# @Author: 周余芳

from selenium import webdriver
from time import sleep
import pytest


class TestMail:
    """
    先实例化driver
    """
    option = webdriver.ChromeOptions()

    # 屏蔽V76以上自动化受控提示 ，开发者提示
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

    # 指定新用户数据目录，避免页面提示"data"不安全
    option.add_argument("user-data-dir=E:/PycharmProject/selenium/profile")

    driver = webdriver.Chrome(options=option)

    @pytest.mark.login
    def setup_class(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://mail.163.com')

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.login
    @pytest.mark.xfail(reruns=1, reruns_delay=5)
    def test_login_email(self):
        # 开始登录
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        self.driver.find_element_by_name('email').send_keys('123')
        self.driver.find_element_by_name('password').send_keys('111')
        self.driver.find_element_by_id('dologin').click()
        self.driver.switch_to.default_content()

# 修改use-data-dir= ''文件目录为自己的
# 根目录加pytest.ini文件，mark下加login标记，否则会有警告输出
# terminal 下执行 pytest -s -m "login" Case/test_web.py

