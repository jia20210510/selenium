# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: selenium
@File: Action.PY
@Date: 2021/8/10 23:51
@Author: jia
@Description:
"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep


class Action(object):

    # 实例化driver
    def __init__(self, browser_name):
        if browser_name == 'Chrome':
            option = webdriver.ChromeOptions()
            # 屏蔽V76以上自动化受控提示 ，开发者提示
            option.add_experimental_option('useAutomationExtension', False)
            option.add_experimental_option("excludeSwitches", ['enable-automation'])

            # 屏蔽保存密码提示框
            prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
            option.add_experimental_option("prefs", prefs)

            # 指定新用户数据目录，避免页面提示"data"不安全
            option.add_argument("user-data-dir=E:/PycharmProject/selenium/profile")

            self.driver = webdriver.Chrome(options=option)
        elif browser_name == 'Firefox':
            self.driver = webdriver.Firefox()

        elif browser_name == 'IE':
            self.driver = webdriver.Ie()

    # 定位元素
    def operation(self, selector_type, elements_value, action, input_content, expect):

        # x path 选择器
        if selector_type == 'xpath':
            if action == 'click':
                self.driver.find_element_by_xpath(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_xpath(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_xpath(elements_value).clear()
            elif action == 'assert':
                actual = self.driver.find_element_by_xpath(elements_value)
                assert actual == expect
            elif action == 'submit':
                self.driver.find_element_by_xpath(elements_value).submit()
            elif action == 'select':
                """下拉框：先定位到下拉框，再从下拉框选择value"""
                s = Select(self.driver.find_element_by_xpath(elements_value))
                s.select_by_value(input_content)  # s.select_by_index()
            elif action == 'get_text_num':
                """ 检查文本的数量"""
                num = self.driver.find_element_by_xpath(elements_value).text
                assert num == expect
            elif action == 'backspace':
                """删除一个字"""
                self.driver.find_element_by_xpath(elements_value).send_keys(Keys.BACK_SPACE)
            elif action == 'space':
                """输入一个空格"""
                self.driver.find_element_by_xpath(elements_value).send_keys(Keys.SPACE)
            elif action == 'enter':
                """键盘回车"""
                self.driver.find_element_by_xpath(elements_value).send_keys(Keys.ENTER)
            elif action == 'ctrl+a':
                """ 模拟键盘全选"""
                self.driver.find_element_by_xpath(elements_value).send_keys(Keys.CONTROL, 'a')
            elif action == 'upload_file':
                """点击上传按钮，上传文件路径D:\\upload_file.txt"""
                self.driver.find_element_by_xpath(elements_value).send_keys(input_content)

        # id 选择器
        elif selector_type == 'id':
            if action == 'click':
                self.driver.find_element_by_id(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_id(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_id(elements_value).clear()

        # class_name  选择器
        elif selector_type == 'class_name':
            if action == 'click':
                self.driver.find_element_by_class_name(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_class_name(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_class_name(elements_value).clear()

        # 精确匹配超连接 eg:<a href='http:xxx' name= xxx>新闻</a> ,elements_value = '新闻'
        elif selector_type == 'link_text':
            if action == 'click':
                self.driver.find_element_by_link_text(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_link_text(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_link_text(elements_value).clear()

        # 标签名 选择器
        elif selector_type == 'tag_name':
            if action == 'click':
                self.driver.find_element_by_tag_name(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_tag_name(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_tag_name(elements_value).clear()

        # name 定位
        elif selector_type == 'name':
            if action == 'click':
                self.driver.find_element_by_name(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_name(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_name(elements_value).clear()

        # css定位器
        elif selector_type == 'css_selector':
            if action == 'click':
                self.driver.find_element_by_css_selector(elements_value).click()
            elif action == 'send_keys':
                self.driver.find_element_by_css_selector(elements_value).send_keys(input_content)
            elif action == 'clear':
                self.driver.find_element_by_css_selector(elements_value).clear()

        # 不使用选择器的操作如：前进，后退，划动，刷新
        elif selector_type == 'None':
            if action == 'scroll_top':
                """ 划到页面顶部,也可以划动到指定像素 """
                self.driver.execute_script("document.documentElement.scrollTop=0")
            elif action == 'scroll_bottom':
                """划到页面底部 """
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            elif action == 'scroll_left':
                """滚动条划到左边"""
                self.driver.execute_script("document.documentElement.scrollLeft=0")
            elif action == 'scroll_right':
                """滚动条划到右边"""
                self.driver.execute_script("document.documentElement.scrollLeft=10000")
            elif action == 'scroll_to':
                """使用java_script设置浏览器滚动条位置,左边距，上边距"""
                js = "window.scrollTo("+input_content[0]+","+input_content[1]+");"
                self.driver.execute_script(js)
            elif action == 'back':
                self.driver.back()
            elif action == 'forward':
                self.driver.forward()
            elif action == 'refresh':
                self.driver.refresh()
            elif action == 'sleep':
                sleep(input_content)
            elif action == 'switch_to_frame':
                """frame只能用id或name定位"""
                self.driver.switch_to.frame(elements_value)
            elif action == 'default_frame':
                """取消选中frame，跳回最外层的页面"""
                self.driver.switch_to.default_content()
            elif action == 'MouseOver':
                """ 对定位元素执行鼠标悬停"""
                ActionChains(self.driver).move_to_element(elements_value).perform()
            elif action == 'check_title':
                """ 断言当前页面的title是否符合预期"""
                title = self.driver.title
                assert title == expect
            elif action == 'check_url':
                """ 断言当前页面URL是否符合预期"""
                url = self.driver.current_url
                assert url == expect
            elif action == 'switch_handle':
                """ 切换窗口"""
                search_handle = self.driver.current_window_handle
                self.driver.switch_to.window(search_handle)
            elif action == 'confirm_ok':
                """confirm弹窗有两个按钮，一个确定，一个取消，点击弹窗的确定"""
                self.driver.switch_to.alert.accept()
            elif action == 'confirm_no':
                """confirm弹窗有两个按钮，一个确定，一个取消, 点击弹窗的取消"""
                self.driver.switch_to.alert.dismiss()
            elif action == 'screen_shot':
                """截取当前窗口，保存到指定路径 input_content(D:\\screen_shot.jpg)"""
                self.driver.get_screenshot_as_file(input_content)


if __name__ == '__main__':
    ui = Action("Chrome")
    ui.driver.get('http://www.baidu.com')
    sleep(2)
