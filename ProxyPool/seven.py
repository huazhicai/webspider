# encoding:utf-8
import requests  # 导入requests模块用于访问测试自己的ip
import random

pro = ['221.202.72.250:53281', '111.155.116.232:8123', '140.250.88.243:26500', '122.246.50.9:28378']  # 在(http://www.xicidaili.com/wt/)上面收集的ip用于测试
# 没有使用字典的原因是 因为字典中的键是唯一的 http 和https 只能存在一个 所以不建议使用字典


#  你的请求头信息
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'https://www.baidu.com/'  # 你用于测试自己ip的网站
request = requests.get(url, proxies={'http': 'https://118.31.220.3:8080'}, headers=head)  # 访问这个网页  随机生成一个ip
request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
print(request.status_code)
print(request.url)