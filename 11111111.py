import urllib.request
import urllib.parse
import requests
import random

from bs4 import BeautifulSoup


def get_name(url):
    name_list = []
    #发起一个request请求,得到返回对象
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')  # 生成可分析对象
    #print(soup)
    if soup.find_all("a",class_="btn btn2"):
        for name in soup.find_all("a",class_="btn btn2")[:50]:  # 遍历所有的姓氏链接，此处只获取前100个姓氏
            url1 = 'http:' + name.attrs['href']  #找到姓氏链接，再次返回此函数
            get_name(url1)
            res1 = requests.get(url1)
            soup1 = BeautifulSoup(res1.text, 'html.parser')  # 生成可分析对象
            if soup1.find_all('a', class_='btn btn-link'):
                for name in soup1.find_all('a', class_='btn btn-link')[:50]:  # 找到不同姓氏的名字，此处只获取每个姓氏的前10个
                    name_list.append(name.text)
                    # print(name.text)
                # return name.text
        slice = random.sample(name_list, 1000)

        ran_name = random.choice(slice)
        print(ran_name)
        return ran_name
    # elif soup.find_all('a', class_='btn btn-link'):
    #     for name in soup.find_all('a', class_='btn btn-link')[:10]:  #找到不同姓氏的名字，此处只获取每个姓氏的前10个
    #         name_list.append(name.text)
    #         #print(name.text)
    # #return name.text
    # slice = random.sample(name_list, 1)
    # print(slice)
    # ran_name = random.choice(slice)
    # print(ran_name)
    # return ran_name
    #return name_list


if __name__ == '__main__':
    url = 'http://www.resgain.net/xsdq.html'
    get_name(url)


