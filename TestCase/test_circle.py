#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/6/28 16:10
import unittest
from random import choice
from Common import InitDriver
from Common.yunxiCommon import *
from utils import L

L.i('-------开始运行test_circle-------')


class Circle(unittest.TestCase):
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

    def test_a(self):
        """测试登录-关注页面"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.chat_list()
        self.send_message()
        # try:
        #     if a:
        #         self.chat_list()
        # except:
        #     print("点击列表失败")

    def chat_list(self):
        get_xpath(self, "//android.widget.RelativeLayout[@index='1']").click()
        circle_name = get_id(self, 'tv.yunxi.app:id/tv_circle_name')
        # none_trip = get_id(self, 'tv.yunxi.app:id/tv_tip')
        try:
            result01 = lambda action: action.is_element_displayed(circle_name)
            # result02 = lambda action: action.is_element_displayed(none_trip)
            if result01:
                print(circle_name.text)
                circle_name.click()
                # if result02:
                #     if none_trip.text == '您还没有加入圈子':
                #         print("圈子列表为空")

        except:
            print("圈子列表获取失败")

    def send_message(self):

        ciecle_input = get_id(self, 'tv.yunxi.app:id/edt_circle_input')
        mylist = [u'很好', u'不错', u'赞', u'好看', u'受用']
        message = choice(mylist)
        ciecle_input.click()
        # # 一条消息-----
        # ciecle_input.send_keys(message)
        # self.driver.keyevent(66)  # 发送
        # newmessage = u'13071825896' + ':' + ' ' + ' ' + message


        # 多条消息-----
        i = 1
        while (i < 200):
            ciecle_input.send_keys(message + str(i))
            self.driver.keyevent(66)  # 发送
            i = i + 1
        newmessage = u'13071825896' + ':' + ' ' + ' ' + message + str(i)
        print(newmessage)
        message1 = self.driver.find_elements_by_id('tv.yunxi.app:id/tv_content')
        for ms in message1:
            if ms.text == newmessage:
                print(u'消息发送成功')
                break

    def circle_detail(self):
        try:
            bt_detail = get_xpath(self, "//android.widget.LinearLayout[@index='3']")
            bt_circleout = get_id(self, 'tv.yunxi.app:id/tv_logout_circle')
            re = lambda action: action.is_element_displayed(bt_detail)
            re1 = lambda action: action.is_element_displayed(bt_circleout)

            if re:
                bt_detail.click()
                L.i("点击按钮查看成员")
                if re1:
                    L.i("页面跳转成功")
                    bt_circleout.click()
                    L.i("退出圈子")
        except:
            L.i("查看群成员失败")


if __name__ == '__main__':
    unittest.main()
