'''
利用request下载页面
自动检测页面的charset
'''

from urllib import request
import chardet


if __name__ == '__main__':
    url = 'http://hz.fang.com/'
    resp = request.urlopen(url)
    html = resp.read()
    charset = chardet.detect(html)
    print(charset)
    print(type(charset))
    # 使用get保证不会出错
    html = html.decode(charset.get('encoding', 'utf-8'))
    print(html)