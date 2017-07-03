#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/3 14:14
from time import sleep
from Common.Element import *
from Common.action import ElementActions
from utils.environment import Environment

env = Environment().get_environment_info()


# """"登录页面测试步骤"""

def goto_login(self):
    global action
    action = ElementActions(driver=self.driver)
    sleep(4)
    my = get_name(self, "我的")
    check_my = lambda action: action.is_element_displayed(my)
    if check_my:
        my.click()
    sleep(2)
    try:

        lgbs = get_name(self, '登录')
        check_lgbs = lambda action: action.is_element_displayed(lgbs)

        if check_lgbs:
            lgbs.click()
        sleep(2)
    except:
        print("进入登录页面失败")


def login(self, username, verificationcode):
    sleep(2)
    # phoneLogin = get_id(self, 'tv.yunxi.app:id/rl_phone_login')
    # phoneLogin.click()

    try:
        usernameEt = get_id(self, 'tv.yunxi.app:id/ed_phone_num')
        self.assertIsNotNone(usernameEt)
        usernameEt.clear()
        usernameEt.send_keys(username)
        print(u'--已经输入手机号--')
        sleep(2)
        # get_id(self,'tv.yunxi.app:id/tv_get_verification_first').click()
        # print(u'--获取验证码--')
        # sleep(2)
        et_ver = get_id(self, 'tv.yunxi.app:id/ed_verification')
        self.assertIsNotNone(et_ver)
        et_ver.clear()
        et_ver.send_keys(verificationcode)
        print(u'--已输入验证码--')
        sleep(2)

        get_id(self, 'tv.yunxi.app:id/tv_phone_login').click()
        print(u'--点击登录--')
        sleep(2)
        phone = get_id(self, 'tv.yunxi.app:id/tv_phone')
        Login_successful = self.assertEqual(phone.text, username)  # 判断是否登录成功
        if Login_successful == None:
            return True

    except:
        print(u'--登录失败--')
        sleep(2)


def wx_login(self):
    wxBnt = get_id(self, 'tv.yunxi.app:id/ll_wechat_login')
    self.assertIsNotNone(wxBnt)
    wxBnt.click()
    get_name(self, '确认登录').click()
    sleep(4)


def user_agree(self):
    sleep(4)

    try:
        agree = get_id(self, 'tv.yunxi.app:id/tv_agree')
        self.assertIsNotNone(agree)
        agree.click()
        title = get_id(self, 'tv.yunxi.app:id/tv_title')
        self.assertIsNotNone(title)
        agree = self.assertEqual(title.text, u"用户协议")
        if agree == None:
            return True

    except:
        print('---查看用户协议失败-----')
    self.driver.keyevent(4)
