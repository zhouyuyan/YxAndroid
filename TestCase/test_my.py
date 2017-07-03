#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/19 14:35
import unittest

from Common import InitDriver
from Common.yunxiCommon import *
from Common.Element import *
from appium import webdriver as appdriver
from utils import L

L.i('-------开始运行test_my-------')


class My(unittest.TestCase):
    def setUp(self):

        self.driver = InitDriver.start_driver()

        self.driver.implicitly_wait(5)

        print("----------------setup-------------")

    def tearDown(self):
        print("-------------teardown------------------")
        self.driver.close_app()
        self.driver.quit()

    def test_e(self):
        """测试登录-设置（清除缓存）"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.goto_setting()
        self.setting()

    def test_f(self):
        """测试登录-设置（意见反馈）"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.goto_setting()
        self.feedback()

    def setting(self):

        try:

            sleep(2)
            get_id(self, 'tv.yunxi.app:id/rl_wipe_cache').click()
            L.i('--点击清空缓存按钮--')
            sleep(2)
            get_id(self, 'tv.yunxi.app:id/dialog_ok').click()
            sleep(2)
            L.i('--点击清空缓存dialog--')
            sleep(2)
            get_id(self, 'tv.yunxi.app:id/ll_back').click()
            sleep(2)
            self.driver.keyevent(4)  # 硬件返回
        except:
            L.w('--操作失败--')

        sleep(2)

    def goto_setting(self):
        get_id(self, 'tv.yunxi.app:id/rl_setting').click()
        L.i('--点击设置按钮--')

    def feedback(self):
        try:
            feedback = get_xpath(self, "//android.widget.EditText[@text='请简要描述您的问题和意见']")
            re = lambda action: action.is_element_displayed(feedback)
            if re:
                feedback.send_keys("hahhahahahahahahahhahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                sleep(1)
            get_xpath(self, "//android.widget.EditText[@text='请留下邮箱方便我们联系您']").send_keys("11@qq.com")
            sleep(1)
            get_xpath(self, "//android.view.View[@content-desc='提交']").click()
        except:
            print("提交反馈失败")


if __name__ == '__My__':
    unittest.main()
