"""
AQI计算
"""

def cal_pm_iaqi():
    "计算pm2.5的iaqi"
    pass

def cal_co_iaqi():
    "计算CO的iaqi"
    pass

def cal_aqi(param_list):
    "AQI计算"
    pm_val = param_list[0]
    co_val = param_list[1]
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)
    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

def main():
    "主函数"
    input('请输入以下信息，用空格分割')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split('')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    #调用AQI计算函数
    aqi_val = cal_aqi(param_list)

    print('空气质量指数为：{}',aqi_val)

if __name__ == '__main__':
        main()

