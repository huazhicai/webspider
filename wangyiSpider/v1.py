'''
使用urllib.request 请求一个网页，并打印出来
'''

from urllib import request


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # 打开相应的url, 读取来的内容为bytes
    resp = request.urlopen(url)
    html = resp.read()
    print(type(html))
    # 需要解码
    html = html.decode('utf-8')
    print(html)