#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/26 12:04
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from exception.exceptions import NotFoundTextError
from utils import L

"""""封装元素"""
import time


def get_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element


def get_name(self, name):
    element = self.driver.find_element_by_name(name)
    return element


def get_xpath(self, xpath):
    element = self.driver.find_element_by_xpath(xpath)
    return element


def over(self):
    element = self.driver.quit()
    return element


def get_screen(self, path):
    self.driver.get_screenshot_as_file(path)


def swipe_to_up(self):
    global window_size, width, height
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)


def swipe_to_down(self):
    # window_size = self.driver.get_window_size()
    # width = window_size.get("width")
    # height = window_size.get("height")
    self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)


def swipe_to_left(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)


def swipe_to_right(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)


def swip_left(self, count=1):
    """向左滑动,一般用于ViewPager

    Args:
        count: 滑动次数

    """
    for x in range(count):
        self.sleep(1)
        self.driver.swipe(width * 9 / 10, height / 2, width / 10, height / 2, 1500)


def swip_right(self, count=1):
    """向右滑动,一般用于ViewPager

    Args:
        count: 滑动次数

    """
    for x in range(count):
        time.sleep(1)
        self.driver.swipe(width * 9 / 10, height / 10, width / 2, height / 2, 1500)


def swip_down(self, count=1, method=None):
    """向下滑动,常用于下拉刷新

    Args:
        count: 滑动次数
        method: 传入的方法 method(action) ,如果返回为True,则终止刷新

    Examples:
        swip_down(self, count=100, method=is_text_displayed(self, "没有更多了"))
        上面代码意思:当页面不展示"暂无可配送的订单"时停止刷新,即有单停止刷新
    """
    if count == 1:
        self.driver.swipe(width / 2, height * 2 / 5, width / 2, height * 4 / 5, 2000)
        time.sleep(1)
    else:
        for x in range(count):
            self.driver.swipe(width / 2, height * 2 / 5, width / 2, height * 4 / 5, 2000)
            time.sleep(1)
            try:
                if method(self):
                    break
            except:
                pass


def swip_up(self, count=1, method=None):
    """向上滑动,常用于上拉加载

    Args:
        count: 滑动次数
        method: 传入的方法 method(action) ,如果返回为True,则终止加载

    Examples:
        swip_down(self, count=100, method=is_text_displayed(self, "没有更多了"))
        上面代码意思:当页面不展示"暂无可配送的订单"时停止加载,即有单停止加载
    """
    if count == 1:
        self.driver.swipe(width / 2, height * 4 / 5, width / 2, height * 2 / 5, 2000)
        time.sleep(1)
    else:
        x = 0
        for x in range(count):
            self.driver.swipe(width / 2, height * 4 / 5, width / 2, height * 2 / 5, 2000)
            time.sleep(1)
            try:
                if method(self):
                    break
            except:
                pass
        L.i('上拉加载的次数：' + str(x))


def is_text_displayed(self, text, is_retry=True, retry_time=5, is_raise=False):
    """检查页面中是否有文本关键字

    如果希望检查失败的话,不再继续执行case,使用 is_raise = True

    Args:
        text: 关键字(请确保想要的检查的关键字唯一)
        is_retry: 是否重试,默认为true
        retry_time: 重试次数,默认为5
        is_raise: 是否抛异常
    Returns:
        True: 存在关键字
    Raises:
        如果is_raise = true,可能会抛NotFoundElementError

    """

    try:
        if is_retry:
            return WebDriverWait(self.driver, retry_time).until(
                lambda driver: self._find_text_in_page(text))
        else:
            return self._find_text_in_page(text)
    except TimeoutException:
        print("[Text]页面中未找到 %s 文本" % text)
        if is_raise:
            raise NotFoundTextError
        else:
            return False
