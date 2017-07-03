#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/6/23 10:30
from appium import webdriver
import time
import requests
from utils.environment import Environment

env = Environment().get_environment_info()

server_url = 'http://localhost:4723/wd/hub'


def start_driver():
    print('--------------------Start Driver------------------------')

    caps = {

        'platformName': env.devices[0].platform_name,

        'platformVersion': env.devices[0].platform_version,

        'deviceName': env.devices[0].device_name,

        'appPackage': env.app_package,

        'appActivity': env.app_activity,

        'app': env.apk,
        'automationName': 'Appium',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'autoLaunch': True,
        'autoAcceptAlerts': True
    }
    driver = webdriver.Remote(server_url, caps)
    time.sleep(10)
    return driver


# 判断appium server是否已启动
def is_running():
    url = server_url + '/status'
    response = requests.get(url)
    if str(response.status_code).startswith("2"):
        return True
    else:
        return False
