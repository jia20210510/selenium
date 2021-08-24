# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: find_elements.PY
@Date: 2021/8/9 0:08
@Author: jia
@Description:
"""

from selenium import webdriver
from time import sleep

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('http://www.hao123.com')

print(driver.title)
sleep(3)

# 窗口自定义大小
driver.set_window_size(600, 900)
sleep(2)

# 窗口最大化
driver.get('http://www.51zxw.net')
driver.maximize_window()
sleep(2)

# 前进
driver.forward()
sleep(2)
driver.maximize_window()

# link_text定位
driver.find_element_by_link_text('电脑办公').click()
sleep(2)

# 高级用法：父元素+子元素定位
driver.find_element_by_xpath("//div[@id='rank']//a[4]").click()
button = driver.find_element_by_xpath("//div[@id='rank']//a[4]")
assert button == 'abc'

# tag_name标签定位
driver.find_elements_by_tag_name('input')[2].click()
# 元素组合定位
driver.find_element_by_xpath("//input[@class='loinp' and @name='username'] ").send_keys('123')
# class name 定位
driver.find_element_by_class_name('help').click()
sleep(2)
driver.get('http://www.baidu.com')
driver.find_element_by_name('wd').send_keys('abc')
driver.find_element_by_id('su').click()
sleep(2)
driver.find_element_by_xpath("//div[@id='2']//a[contains(text(),'_')]").click()
driver.find_element_by_id('baidu_translate_input').send_keys('div')
sleep(2)

# 返回
driver.back()
sleep(1)

# 关闭
driver.quit()

"""
CSS定位
# ID定位，前加 # 号
driver.find_element_by_css_selector('#kw').send_keys('123')
# class定位
driver.find_element_by_css_selector('.s_ipt').send_keys('python')
# autocomplete属性定位 加[ ]号
driver.find_element_by_css_selector("[autocomplete='off']")
# name属性定位 加[ ]号
driver.find_element_by_css_selector("[name='wd']").send_keys("selenium")
# 层级关系定位
driver.find_element_by_xpath("form.fm>span>input").send_keys("selenium")
# 索引定位
driver.find_element_by_css_selector("select#nr>option：nth-child(1)").click()
# 逻辑运算定位 两个属性中间没有 and
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("selenium")
"""

"""
# 下拉列表定位
driver.find_elements_by_tag_name('option')[0].click()
driver.find_element_by_css_selector('[value="1"]').click()
"""
