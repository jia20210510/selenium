# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: conftest.PY
@Date: 2021/8/18 23:42
@Author: jia
@Description: fixture和conftest.py联合使用实现全局共享
conftest.py所在目录及其子目录可以灵活调用fixture修饰的方法
fixture的作用域从大到小：session>module>class>function
"""
import pytest
from Common import files
from selenium import webdriver


# 导出报告前先清除一下temp文件
@pytest.fixture(scope='session')
def new_temp():
    root_path = files.get_project_path('selenium')
    test_data = files.read_file(root_path + '/Data/baidu.CSV')
    browser_name = test_data[0][0]
    url = test_data[0][1]
    env = 'browser = ' + browser_name + '\nurl=' + url + '\n' \
          'System.version = win10\nauthor = jia\npython = 3.8.0\npyTest = 6.2.4\nallure = 2.9.43\n' \
          'flask = 2.0.1\nhtml = 3.1.1'

    temp_path = root_path + "/Report/temp"
    return env, temp_path, browser_name, url




