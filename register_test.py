#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
from urllib import parse
import HTMLTestRunner
import random
import sys
import json

'''定义链接地址'''
global url
url = 'http://test.tianwashangmeng.com/twweb'
#url = 'http://www.tianwashangmeng.com/twweb'    #生产环境
#url = 'http://39.105.191.175:8080/twweb'

#随机生成手机号和验证码

def mobile_code():
    mobile = random.randint(14611110200, 14611119999)
    code_url = url + '/UserController_4M/registeMessage.action?'
    respon_text = requests.post(code_url, data={'mobile': mobile})
    # code_text = parse.unquote(parse.unquote(respon_text.text))  #解密接口返回结果
    # '''实例化unittest'''
    # a = unittest.TestCase()
    # a.assertIn(member='天娃新时代', container=code_text)
    code_text = parse.unquote(parse.unquote(eval(respon_text.text)['data']))
    data = json.loads(code_text)
    if data['data']['logicStatus']=="01":
        return mobile, code_text.split(',')[0].split(':')[2][8:14]
    else:
        print(mobile, data['data']['msg'])
        return "0", "0"



#测试注册接口----->成功
def register_success():
        '''
        注册成功
        :return:
        '''
        url_register = url + '/UserController_4M/insertUser.action?'
        get_value = mobile_code()
        if get_value[0]!="0":

            respon_text = requests.post(url_register, data={'mobile': get_value[0],
                                                            'password': 'e10adc3949ba59abbe56e057f20f883e',
                                                            'presenterMobile': '14611110001',
                                                            'checkCode':get_value[1],
                                                            'fan_shop_mobile':None})
            #respon_text_unquote = parse.unquote(parse.unquote(respon_text.text))
            respon_text_unquote = parse.unquote(parse.unquote(eval(respon_text.text)['data']))
            data = json.loads(respon_text_unquote)

            print((get_value[0]), data['data']['msg'])

            '''实例化断言'''
            # a = unittest.TestCase()
            #
            # if respon_text_unquote
            # a.assertIn(member='注册成功', container=respon_text_unquote)
            # print(get_value[0])
            # print('注册成功')

#测试注册接口----->失败
def register_fail():
    '''
    验证码错误时注册失败
    :return:
    '''
    url_register = url + '/UserController_4M/insertUser.action?'
    get_value = mobile_code()
    respon_text_error = requests.post(url_register, data={'mobile':get_value[0],
                                                    'password': 'ce44b4675012e666879afd3605e63f7c',
                                                    'presenterMobile': '14611110001',
                                                    'checkCode':'abcds',
                                                    'fan_shop_mobile': None})
    respon_text_unquote = parse.unquote(parse.unquote(respon_text_error.text))
    '''实例化断言'''
    a = unittest.TestCase()
    a.assertIn(member='验证码输入错误', container=respon_text_unquote)
    print('注册失败')





if __name__ == '__main__':
    for a in range(0, int(sys.argv[1])):
        register_success()
        #register_fail()

