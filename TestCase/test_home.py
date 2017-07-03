#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/19 14:34
import unittest
from random import choice

from appium import webdriver as appdriver

from Common import InitDriver
from Common.Element import *
from Common.action import ElementActions
from Common.yunxiCommon import *
from utils import L

L.i('-------开始运行test_home-------')


class Home(unittest.TestCase):
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
        """测试登录-发现-搜索-评论"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.goto_faxian()
        self.search()
        self.pinglun()

    def test_b(self):
        """测试登录-发现页面-关注-评论"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.faxian()
        self.guanzhu()

    def test_c(self):
        """测试未登录-发现页面-搜索"""

        self.goto_faxian()
        self.search()

    def test_sharefriend(self):
        """测试登录-发现页面-分享到微信/朋友圈"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.goto_faxian()
        self.search()
        self.wx_share()
        # self.wx_cricle()

    def test_videoSetting(self):
        """测试登录-发现页面-播放界面设置"""
        b = 0
        self.goto_faxian()
        self.search()
        a = self.open_fullScreen()
        if a == 1:
            b = self.open_danm()
            L.i('open_danm success')
        else:
            L.w('open_danm failed')
            pass

        if b == 1:
            self.close_danm()
            L.i("close_danm success")
        else:
            L.w("close_danm failed")
            pass
        if a == 1:
            self.close_fullScreen()
            L.i('open_danm success')
        else:
            L.w('open_danm failed')
            pass

    def test_f(self):
        """测试登录-发现-评论"""
        goto_login(self)
        login(self, '13071825896', '3279')
        self.faxian()
        self.pinglun()

    def test_lefttolist(self):
        self.list_to_left()

    def test_downtolist(self):
        self.list_to_more()

    # def test_g(self):
    #     """测试发现-播放页面设置"""
    #     self.faxian()
    #     self.video_setting()
    #     print("---------------------this is test_g-----------------------")

    def search(self):
        ser = get_id(self, 'tv.yunxi.app:id/img_right')
        self.assertIsNotNone(ser)
        ser.click()
        print(u'--点击搜索按钮--')
        sleep(2)
        get_id(self, 'tv.yunxi.app:id/ed_search').send_keys(u'啊啊啊啊啊')
        print(u'--输入搜索内容--')
        self.driver.keyevent(66)
        sleep(5)
        try:
            get_id(self, 'tv.yunxi.app:id/tv_search_title')
            print(u'搜索成功')
            get_id(self, 'tv.yunxi.app:id/img_search').click()


        except:
            print(u'搜索失败')
            pass
            self.driver.keyevent(4)

    def faxian(self):
        # 发现页面
        get_name(self, '发现').click()
        print(u'--进入发现页面--')
        sleep(2)

        get_id(self, 'tv.yunxi.app:id/img_activity_bg').click()  # 点击视频直播
        print(u'--点击视频直播--')
        sleep(6)

    def goto_faxian(self):
        fx = self.driver.find_element_by_name('发现')
        fx.click()
        print(u'--进入发现页面--')
        sleep(2)

    def pinglun(self):
        # 详情页评论
        mylist = [u'很好', u'不错', u'赞', u'好看', u'受用']
        message = choice(mylist)
        get_id(self, 'tv.yunxi.app:id/tv_input_click').click()
        # sleep(2)
        # 多条评论-----
        # i = 1
        # while (i < 200):
        #     get_id(self,self,'tv.yunxi.app:id/tv_input_click').send_keys(message + str(i))
        #     self.driver.keyevent(66)  # 发送
        #     i = i + 1
        # newmessage = u'13071825896' + ':' + ' ' + ' ' + message + str(i)
        # print(newmessage)
        # message1 = self.driver.find_elements_by_id('tv.yunxi.app:id/tv_content')
        # for ms in message1:
        #     if ms.text == newmessage:
        #         print(u'消息发送成功')
        #         break
        #         ------一条评论------
        get_id(self, 'tv.yunxi.app:id/tv_input_click').send_keys(message)
        self.driver.keyevent(66)  # 发送
        newmessage = u'13071825896' + ':' + ' ' + ' ' + message
        print(newmessage)
        message1 = self.driver.find_elements_by_id('tv.yunxi.app:id/tv_content')
        for i in message1:
            if i.text == newmessage:
                print(u'消息发送成功')
                break
            sleep(2)

    def guanzhu(self):
        try:
            get_id(self, 'tv.yunxi.app:id/img_up_head').click()
            sleep(2)
            print(u'--点击主播头像，进入企业主页--')

            get_id(self, 'tv.yunxi.app:id/tv_to_observe').click()
            print(u'--点击关注--')

            sleep(4)
            get_id(self, 'tv.yunxi.app:id/tv_to_observe').click()
            print(u'--再次点击关注--')
            sleep(2)

            self.driver.keyevent(4)
            get_id(self, 'tv.yunxi.app:id/img_activity_bg').click()
            sleep(2)
            print(u'--点击企业列表--')

            get_id(self, 'tv.yunxi.app:id/tv_to_observe').click()
            print(u'--直播页面点击关注--')
            sleep(2)
            get_id(self, 'tv.yunxi.app:id/tv_to_observe').click()
            print(u'--直播页面再次点击关注--')
            sleep(2)
            self.driver.keyevent(4)
            sleep(3)

        except:
            print(u'--发现--')

    def list_to_left(self):
        action.swip_left(8)
        print('左滑动')

    def list_to_more(self):
        sleep(2)
        swip_down(self, count=1)
        print('swip_down')
        swip_up(self, count=100, method=is_text_displayed(self, "没有更多了"))

        print('swip_up')

    def open_fullScreen(self):
        # 开启全屏
        sleep(5)
        fusc = get_id(self, 'tv.yunxi.app:id/img_full_Screen')
        # fusc = get_id(self,'tv.yunxi.app:id/img_full_Screen')
        giftLl = get_id(self, 'tv.yunxi.app:id/giftLl')
        # result01 = self.assertIsNotNone(fusc)
        result01 = lambda action: action.is_element_displayed(fusc)
        try:
            if result01:
                fusc.click()
                L.i('点击op全屏按钮02')
                print(result01)
                a = 1

            else:
                giftLl.click()
                L.i('点击屏幕')
                if result01:
                    fusc.click()
                    L.i('点击op全屏按钮01')
                a = 1

        except:
            a = 2

            L.w("横屏播放failed")
        print(a)
        return a

    def open_danm(self):
        # 开启弹幕

        try:
            bottom_control = get_id(self, 'tv.yunxi.app:id/rl_bottom_control')
            danm = get_id(self, 'tv.yunxi.app:id/img_danmaku_control')
            result02 = lambda action: action.is_element_displayed(danm)
            if result02:
                print(result02)
                bottom_control.click()
                L.i('点击屏幕')
                if result02:
                    danm.click()
                    print('点击opdanm按钮01')

            else:
                danm.click()
                print('点击opdanm按钮02')
            od = 1

        except:
            L.w("open_danm failed")
            od = 2
        print(od)

        return od

    def close_fullScreen(self):
        # 关闭全屏

        a = 0
        try:
            fusc = get_id(self, 'tv.yunxi.app:id/img_full_Screen')
            giftLl = get_id(self, 'tv.yunxi.app:id/giftLl')
            result01 = lambda action: action.is_element_displayed(fusc)
            if not result01:
                sleep(5)
                giftLl.click()
                if result01:
                    fusc.click()
                    L.i('点击cl全屏按钮01')
                a = 1
            else:
                if result01:
                    fusc.click()
                fusc.click()
                L.i('点击cl全屏按钮02')
                a = 1


        except:

            L.w("竖屏failed")
            a = 2
        print(a)
        return a

    def close_danm(self):
        # 关闭弹幕

        try:
            bottom_control = get_id(self, 'tv.yunxi.app:id/rl_bottom_control')
            danm = get_id(self, 'tv.yunxi.app:id/img_danmaku_control')
            result02 = lambda action: action.is_element_displayed(danm)
            if not result02:
                print(result02)
                bottom_control.click()
                L.i('点击屏幕')
                if result02:
                    danm.click()
                    L.i('点击danm按钮01')
            else:
                if result02:
                    danm.click()
                    L.i('点击danm按钮02')

        except:
            L.w("close_danm  failed")
        sleep(5)

    def wx_share(self):
        # 微信分享
        try:
            if self.assertIsNotNone(self.share):
                self.play.click()
                self.share.click()
            else:
                self.share.click()

            sleep(2)
            get_xpath(self, "//android.widget.LinearLayout[@index='0']").click()
            sleep(10)
            get_xpath(self, "//android.widget.LinearLayout[@index='1']").click()
            sleep(2)
            get_name(self, u'分享').click()
            sleep(2)
            get_name(self, u'返回云犀直播').click()
            sleep(3)
        except:
            print(u"分享到好友失败")

    def wx_cricle(self):
        # 朋友圈分享
        try:
            self.play = get_id(self, 'tv.yunxi.app:id/ll_player_control')
            self.share = get_id(self, 'tv.yunxi.app:id/img_activity_share')  # 进入到详情界面
            if self.assertIsNotNone(self.share):
                print(self.assertIsNotNone(self.share))
                self.play.click()
                self.share.click()
            else:
                self.share.click()
            sleep(2)
            get_xpath(self, "//android.widget.LinearLayout[@index='1']").click()
            sleep(2)
            get_xpath(self, "//android.widget.TextView[@text='发送']").click()
        except:
            print(u"分享到胖友圈失败")


if __name__ == '__Home__':
    unittest.main()
