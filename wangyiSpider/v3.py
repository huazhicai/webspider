from urllib import request

import chardet

if __name__ == '__main__':
    url = 'http://hz.fang.com/'
    resp = request.urlopen(url)
    print(type(resp))
    print(resp)

    print("URL: {0}".format(resp.geturl()))
    print("Info: {0}".format(resp.info()))
    print("Code: {0}".format(resp.getcode()))
    html = resp.read()
    charset = chardet.detect(html)
    print(html.decode(charset.get('encoding', 'utf-8')))