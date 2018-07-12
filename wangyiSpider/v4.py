'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

from urllib import request, parse


if __name__ == '__main__':
    base_url = 'http://www.baidu.com/s?'
    url = "http://www.baidu.com/s?wd=大熊猫"
    wd = input("Input your keyword:")
    # 字典结构
    qs = {
        "wd": wd
    }
    # 转换为url编码
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = base_url + qs
    print(fullurl)
    resp = request.urlopen(fullurl)
    print(resp.read())
