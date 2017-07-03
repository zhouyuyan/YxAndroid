#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/26 12:04

"""""封装元素"""


def get_id(self, id):
    element = self.driver.find_element_by_id(id)
    return element


def get_name(self, name):
    element = self.driver.find_element_by_name(name)
    return element


def get_xpath(self, xpath):
    element = self.driver.find_element_by_xpath(xpath)
    return element
