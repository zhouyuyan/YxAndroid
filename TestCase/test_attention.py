#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/19 14:35
import unittest

from Common import InitDriver
from Common.action import ElementActions
from Common.yunxiCommon import *
from Common.Element import *
from appium import webdriver as appdriver
from utils import L

L.i('-------开始运行test_attention-------')


class Attention(unittest.TestCase):
    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.driver.implicitly_wait(5)
        global action
        action = ElementActions(driver=self.driver)
        print("----------------setup-------------")

    def tearDown(self):
        print("-------------teardown------------------")
        self.driver.close_app()
        self.driver.quit()

    def test_d(self):
        """测试登录-关注页面"""
        goto_login(self)
        a = login(self, '13071825896', '3279')
        if a:
            self.attention()
        else:
            print("登录失败--->关注失败")

    def attention(self):
        at = get_name(self, '关注')
        self.assertIsNotNone(at)
        at.click()
        tabs = get_id(self, 'tv.yunxi.app:id/tv_tab_title')
        self.assertIsNotNone(tabs)
        tabs.click()

        try:
            get_id(self, 'tv.yunxi.app:id/tv_to_obsever')

            get_id(self, 'tv.yunxi.app:id/tv_to_obsever').click()
            get_id(self, 'tv.yunxi.app:id/img_activity_bg').click()
            sleep(2)
            print(u'随便点一个播放')
        except:
            print(u'关注列表为空,您关注的主播不在直播中')
        self.driver.keyevent(4)


if __name__ == '__Attention__':
    unittest.main()
