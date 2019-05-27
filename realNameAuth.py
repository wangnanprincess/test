import requests
import unittest
from urllib import parse
import json
import random
import time
import urllib3
import sys
from bs4 import BeautifulSoup
# reload(sys)
sys.setdefaultencoding("utf-8")

global url
url = 'http://test.tianwashangmeng.com/twweb'

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

#新用户用户注册
def userRegister():
    getvalue = mobile_code()
    reg_url = url + '/UserController_4M/insertUser.action?'
    reg_text = requests.post(reg_url,data={'mobile':getvalue[0],
                                           'password': 'e10adc3949ba59abbe56e057f20f883e',
                                           'presenterMobile':'13080030058','checkCode':getvalue[1],'fan_shop_mobile':None})
    reg_back = parse.unquote(parse.unquote(reg_text.text))
    a=unittest.TestCase
    a.assertIn(member='注册成功', container=reg_back)
    print('注册成功')


#获取当前登录用户的id
def getUserId():
    global userifo
    get_value = mobile_code()
    info_url = url + '/LoginController_4M/login.action?'
    info_text = requests.post(info_url,data={'mobile':get_value[0],'password':'e10adc3949ba59abbe56e057f20f883e','logintype':2})
    back_info = parse.unquote(parse.unquote(info_text.text['data']))

    jsonData = json.loads(back_info)  # 将json串转化为字典
    userId = jsonData['user']['id']

    return userId
#生成用户注册姓名
def getName():
    pass


#用户实名认证
def nameAuth():
    name = getName()
    getValue = getUserId()
    nameAuth_url = url + '/RealNameAuthApplicationController_4M/insertRealNameAuthApplication.action?'
    nameAuth_respon = requests.post(nameAuth_url,data={'name':name[0],
                                     'user_id':getValue[0],
                                     'face_id':'%2F9j%2F',
                                     'ident_id':'%2F9j%2F',
                                     'id_end_time':time.strftime('%Y-%m-%d',time.localtime(time.time())),
                                     'alipay_user_id':'2088022880191155',
                                     'pt_id_number':'110101199003071110',
                                     'open_user':'%E5%93%A6%E5%95%A6%E5%95%A6&',
                                     'bank_id':'-1&',
                                     'open_bank':'-1&',
                                     'mobile':'-1&','my_photo':'%2F9j%2F4'})
    respon_unquote = parse.unquote(parse.unquote(nameAuth_respon))




#验证当前用户是否实名认证
def realNameVerif():
    getValue = getUserId()
    name_url = url + '/ApplyEntrepreneurialInfo_Controller_4M/selectApplyEntrepreneurialRecent.action?'
    name_text = requests.post(name_url,data={'userId':getValue[0]})
    respon_txt = parse.unquote(parse.unquote(eval(name_text.text)['data']))#eval 将str转换成字典
    data = json.loads(respon_txt)#将json串转换为字典
    info = data['data']['msg']
    if info == '您未申请实名认证!':
        nameAuth()
    else:
        print('该用户已实名认证完成！')









if __name__ == '__main__':
    getUserId()