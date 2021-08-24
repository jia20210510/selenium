# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: test_keywords.PY
@Date: 2021/8/9 0:10
@Author: jia
@Description: 关键字驱动实现UI自动化,
baidu.csv测试用例
"""

from Config import log
from Common import action
from Common import files
from time import sleep
import pytest
import traceback
import allure

logger = log.log_execute("debug_logger")


class TestKeyWords:
    # 基础数据准备
    root_path = files.get_project_path('selenium')
    test_data = files.read_file(root_path+'/Data/baidu.CSV')
    browser_name = test_data[0][0]
    case = test_data[2:]
    ui = action.Action(browser_name)
    driver = ui.driver

    # 打开浏览器
    def test_class(self, new_temp):
        env_text = new_temp[0]
        temp_path = new_temp[1]
        files.new_file(temp_path)
        files.write_file(temp_path+'/environment.properties', env_text)
        logger.info('清除temp文件，重新写入配置')

        url = new_temp[3]
        browser = new_temp[2]
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(3)
        logger.info('打开浏览器:'+browser)

    # 执行测试用例
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('执行{title}模块')
    @allure.title('用例名：{step}')
    @pytest.mark.parametrize('sn,title,step,selector,elements,act,input_t,expect', case)
    def test_baidu(self, sn, title, step, selector, elements, act, input_t, expect):
        try:
            self.ui.operation(selector, elements, act, input_t, expect)
            sleep(1)
            logger.info(step)
        except Exception:
            logger.debug('['+title+']['+step+']执行错误信息：%s', str(traceback.format_exc()))
            raise

    # 关闭浏览器
    def teardown_class(self):
        logger.info('关闭浏览器')
        self.driver.quit()

