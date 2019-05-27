#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
from urllib import parse
import HTMLTestRunner
import random
import HTMLTestRunner


'''定义链接地址'''
global url
url = 'http://test.tianwashangmeng.com/twweb'
#url = 'http://39.105.191.175:8080/twweb'

#随机生成手机号和验证码

def mobile_code():
    mobile = random.randint(14611110200, 14611119999)
    code_url = url + '/UserController_4M/registeMessage.action?'
    respon_text = requests.post(code_url, data={'mobile': mobile})
    code_text = parse.unquote(parse.unquote(respon_text.text))  #解密接口返回结果
    '''实例化unittest'''
    a = unittest.TestCase()
    a.assertIn(member='天娃新时代', container=code_text)
    return mobile, code_text.split(',')[0].split(':')[3][8:14]


#测试注册接口
class RegisterTest(object):

    def register_success(self):
        '''
        注册成功
        :return:
        '''
        url_register = url + '/UserController_4M/insertUser.action?'
        get_value = mobile_code()
        respon_text = requests.post(url_register, data={
            'mobile': get_value[0],
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'presenterMobile': '14611110000',
            'checkCode': get_value[1],
            'fan_shop_mobile': '14611110008'
        })
        respon_text_unquote = parse.unquote(parse.unquote(respon_text.text))
        '''实例化断言'''
        a = unittest.TestCase()
        a.assertIn(member='注册成功', container=respon_text_unquote)



if __name__ == '__main__':
    '''类实例化'''
    t = RegisterTest()
    t.register_success()
