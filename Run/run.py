# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: run.PY
@Date: 2021/8/9 0:14
@Author: jia
@Description:
"""
import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '../Common/test_keywords.py'])  # action/test_keywords
    # pytest.main(['-vs', '../Case/test_web.py'])


# Terminal
# 此时运行路径为 项目的目录 运行前先cd到Run的目录下
# pytest -s ../Common/test_keywords.py --alluredir=../Report/temp
# allure generate ../Report/temp -o ../Report/allure_report --clean
# pytest -s -m "login" Case/debug.py
