# import login_test
import requests

global url
url = 'http://test.tianwashangmeng.com/twweb'
def queryAll():
    '''
    美食下单
    :return:
    '''
    query_url = url + '/FoodOrderController_4M/selectFoodOrder.action?'
    requests.post(query_url,data={'user_id':'e041765ecb6b4c089cbf110f02c3f98a',
                                  'shop_info_id':'e19094bbe2444b6bb3e21771f71942a7',
                                  'shop_info_desktop_number':None,
                                  'goodslist':'e9b0ccc4973e4317b3e891483865d11e',
                                  'numberlist':1,'order_amount':138})





if __name__ == '__main__':

    pass
