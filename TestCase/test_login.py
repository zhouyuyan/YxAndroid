#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/19 14:35
import unittest

from Common import InitDriver
from Common.yunxiCommon import *
from utils import L

L.i('-------开始运行test_login-------')


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.driver.implicitly_wait(5)
        global action
        action = ElementActions(driver=self.driver)
        self.driver.update_settings({"ignoreUnimportantViews": True})
        # 判断是否出现权限弹窗
        sleep(3)
        print("----------------setup-------------")

    def tearDown(self):
        print("-------------teardown------------------")
        self.driver.close_app()
        self.driver.quit()

    def test_login01(self):
        u"""用户名为空，密码为空----登录失败"""
        goto_login(self)

        a = login(self, '', '')
        self.assertFalse(a, False)

    def test_login02(self):
        u"""13071825896，密码为空----登录失败"""
        goto_login(self)

        a = login(self, '13071825896', '')
        self.assertFalse(a, False)

    def test_login03(self):
        u"""用户名为空，密码为3279----登录失败"""
        goto_login(self)

        a = login(self, '', '3279')
        self.assertFalse(a, False)

    def test_login04(self):
        u"""用户名为13071825896，密码为3279----登录成功"""
        goto_login(self)
        a = login(self, '13071825896', '3279')

        self.assertTrue(a, True)
        print('登录成功')

    def test_wxlogin(self):
        u"""微信登录"""

        goto_login(self)
        # self.wx_login()

    def test_userAgree(self):
        u"""用户协议----跳转成功"""
        goto_login(self)
        a = user_agree(self)
        print(a)
        self.assertTrue(a, True)


if __name__ == '__Login__':
    unittest.main()
