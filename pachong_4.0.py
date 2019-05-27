
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():

    """主函数"""
    aqi_data =pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5)) #查看前5行
    # print(aqi_data['AQI'])   #只输出某一列，即AQI列
    # print(aqi_data[['city','AQI']]) #输出两列
    print('基本信息：')
    print(aqi_data.info())
    print('数据预览：')
    print(aqi_data.head())


    #数据清洗
    #只保留AQI>0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    #基本统计
    print('AQI最大值:',clean_aqi_data['AQI'].max())
    print('AQI最小值:', clean_aqi_data['AQI'].min())
    print('AQI均值:', clean_aqi_data['AQI'].mean())

    #top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar',x='city',y='AQI',title='空气质量最好的50个城市',
                      figsize=(20,10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


    
    #数据保存CSV文件
    # top10_cities.to_csv('top10_aqi.csv',index=False)#index=False的作用是不保存索引
    # bottom10_cities.to_csv('bottom10_aqi.csv',index=False)



if __name__ == '__main__':

    main()
