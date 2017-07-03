#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhouyuyan on 2017/5/24 17:28
# 发送邮件
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(file_new):
    # 读取报告内容
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    mail_host = 'smtp.qq.com'
    mail_user = '791430360@qq.com'
    mail_pass = 'xhiuqsvtdokebcge'

    # 发送附件
    nowtime = time.strftime('%Y-%m-%d')
    msg = MIMEMultipart()
    part = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    part.add_header('Content-Disposition', 'attachment', filename="测试报告" + nowtime + ".html")
    msg.attach(part)

    # 设置收发件人信息和邮件主题
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    msg['From'] = '791430360@qq.com'
    msg['To'] = '2434665131@qq.com'
    msg['Subject'] = "APP_Android测试报告" + nowtime
    smtp = smtplib.SMTP_SSL(mail_host)
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()
