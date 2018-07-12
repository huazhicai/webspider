# 爬虫准备工作
- 参考资料
    - python网络数据采集 图灵工业出版
    - 精通Python爬虫框架Scrapy 人民邮电出版
    - [python3网络爬虫](http://blog.csdnnet/c406495762/article/details/72858983)
    - [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
- 前提知识
    - url
    - http协议
    - web前端 HTML，css, js
    - ajzx
    - re, xpath
    - xml

## 1. 爬虫简介

- 两大特征
    - 能按照作者的要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页执行上面两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络爬虫包简介
    - Python2.x: urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python3.x: urllib, urllib3, httplib2, requests
    - Python2: urllib和urllib2配合使用requests
    - Python3: urllib * requests

## 2. urllib
- 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error: 包含urllib.request产生的常见的错误， 使用try捕捉
    - urllib.parse: 包含一解析url的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例v1

- 网页编码问题的解决
    - chardet 可以自动检测页面的文件的编码格式， 但是 ，可能有误。
    - 需要安装 conda install chardet
    - 案例v2

- urlopen 返回对象
    - 案例v3
    - geturl:  返回请求的 url
    - info: 请求反馈对象的额 meta 信息
    - getcode: 返回码

- request.data
    - get:
        - 利用参数给服务器传递信息。
        - 参数为 dict, 然后用parse编码
        - 案例v4
    - post:
        - 一般向服务器传递参数
        - post是把信息自动加密处理
        - 需要用到data参数
        - 使用post意味着Http的请求头 可能需要更改
            - Content-Type: application/x-www.form-urlencode
            - Content-Length: 数据长度
            - 简而言之， 一旦更改请求方法，请注意其他请求头部信息相适应
        - urllib.parse.urlencode可以将字符串自动转换成上面的
        - 案例v5
        - 为了更多的设置请求信息， 单纯的通过urlopen函数已经不太好用了
        - 需要利用request.Request 类
        - 案例v6

- urllib.error
    - URLError产生的原因：
        - 没网
        - 服务器连接失败
        - 不知道服务器
        - 是OSError的子类
        - 案例v7
    - HTTPError, 是URLError的一个子类
        - 案例v8
    - 两者的区别
        - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发 HTTPError
        - URLError对应的是一般网络出现的 问题， 包括url问题
        - OSError - URLError - HTTPError
- UserAgent
    - UserAgent: 用户代理，简称 UA， 属于heads的一部分，服务器通过UA来判断访问者的信息
    - 可以到浏览器去复制
    - 设置UA两种方式
        - heads
        - add_header() 方法
        - 案例v9
- ProxyHandler 处理（代理服务器）
    - 使用代理IP, 是爬虫常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实的访问，代理不允许频繁访问某一个固定网站，所以代理一定要很多
    - 基本使用步骤：
        1. 设置代理池
        2. 创建ProxyHandler
        3. 创建 Openner
- cookie & session
    - 由于http协议的无记忆性， 人们为了弥补这个缺憾 ，所以采用的一个补充协议
    - cookie 是发放给客户用的,(即http浏览器)的一段信息， session是保存在服务上的对应一半信息，用来记录 用户信息
    - cookie & session 的区别
        - 存放不同，cookie在客户端，session在服务器端
        - cookie 不安全
        - session会保存在服务器上一定时间
        - 单个cookie保存数据不超过4k, 很多浏览器限制一个站点最多20个
        - session的存放位置
            - 存在服务器端
            - 一半情况下session是放在内存或者数据库中
            - 没有cookie登陆 案例v11, 可以看到没用cookie则反馈网页未登录状态

- 使用cookie登陆
    - 直接把cookie复制下来，然后手动收入请求头
    - http模块包含一些 关于cookie的模块， 通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie,向传出的http请求添加cookie,
            - cookie存储在内存中， CookieJar实例回收后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None):
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookJar(filename, delayload=None, policy=None):
            - 创建与mocilla浏览器cookietxt兼容的FileCookieJar实例
        - LwpCookieJar
            - 创建与libwww-perl标准兼容的 Set-Cookie3格式的FielCookieJar实例
        - 他们的关系是： CookieJar-->FileCookieJar-->MOzillaCookieJar& LwpCookieJar
    - 利用CookieJar访问人人网， 案例13
        - 自动使用cookie登录， 大致流程是
        - 打开登录页面后自动通过用户名和密码登录
        - 自动提取反馈回来的 cookie
        - 利用提取的cookie登录隐私页面
    - handler是Handler的实例，常用的有
        -  用来处理复杂请求
    - 创立handler后，使用opener打开， 打开后相应的业务有相应的handler处理
    - cookie作为一个变量，打印出来,案例v14
        - cookie属性
            - name:名称
            - value: 值
            - domain: 可以访问此cookie的域名
            - path：可以访问此cookie的页面路径
            - expire: 过期时间
            - size 大小
            - HTTP字段
    - cookie的保存-FileCookieJar， 案例v15
    - cookie的读取， 案例16

- SSL
    - SSL证书就是指遵守SSL安全套接层协议的服务器数字证书(SercureSockerLayer)
    - 美国网景公司开发
    - CA(CertifacateAuthority)是数字认证中心，发放管理废除数字证书的收信任的第三方机构
    - 遇到不信任的 SSL证书，需要单独处理， 案例17

- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5值）
    - 经过加密，传输的是密文，但是
    - 加密函数或者过程一定是在浏览器上完成的，也就是一定会把代码（js代码 ）暴露给使用者
    - 通过阅读加密算法，就可以 模拟出加密过程，从而达到破解
    - 过程参看v18， v19
    - 过程比较啰嗦，笔记比较少，仔细看视频

- ajax
    - 异步请求
    - 一定会有url请求方法，可能有数据传输
    - 一般使用json格式
    - 案例，爬取豆瓣电影， 案例v20

## Requests-献给人类
- HTTP for Humans, 更简洁更友好
- 继承了urllib的所有特性
- 底层是urllib3
- get 请求:
    - requests.get(url)
    - requests.request("get", url)
- proxy
    proxies = {
        "http": "address of proxy",
        "https": "address of proxy"
        }
- 用户验证
    - 代理验证
        ### 可能要使用HTTP basic Auth:
        proxy = {"http": "chian:123456@192.168.11.124:888"}
        rsp = requests.get("http://baidu.com", proxies=proxy)

- web客户端验证
    - auth=(username, password)
    - rsp=request.get("http://baidu.com", auth=auth)

- cookie
    - requests 可以自动处理cookie信息


## XML
- XML(ExtensibleMarkupLanguage)
- w3school.com
- 案例v28.xml
- 概念：父节点，子节点，先辈节点，子孙节点

# XPath
- XPath(XML Path Language), 是一门在XML中查找的语言
- 官方文档 w3school
- XPath开发工具
    - XMQuire
    - chrome插件: Xpath Helper
    - Firefox插件: Xpath Checker

- 常用格式
    - nodename：选取此节点所有子节点
    - / : 从根节点开始选取
    - // : 从当前节点开始选取

## lxml库
- python的HTML/XML的解析器
- 官方文档：http://www.
- 案例v29
- 功能:
    - 解析HTML
    - 文档读取 ，案例v30.html, v31
    - etree和Xpath配合使用， 案例v32

## CSS选择器 BeautifSoup4
- 官方文档
- 几个常用提取信息工具比较：
    - 正则: 很快， 不太好用, 常用。
    - beautifulsoup: 慢， 使用简单，小型爬虫配合requests使用
    - lxml: 比较快， 使用简单。
- 案例v33

## 动态html

## 爬虫和反爬虫

## 动态html介绍
- JavaScript
- JQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript*直接采集浏览器看到的页面
## Selenium + PhantomJS
- Selenium: web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48.0
    - document:
- PhantomJs
    - 基于Webkit的无界面浏览器
    - 官网：http://phantomjs.org/download.html
- Selenium 库有一个WebDriver的API库

- chrome + chromedriver
    - 下载安装

- 验证码: 判断机器人是不是爬虫
- 分类:
    - 简单图片
    - 极验：官网www.geetest.com
    - 12306
    - 电话
    - google验证
- 破解验证码
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证码
    - 简单图片
        - 使用图像识别或者文字识别软件
        - 使用第三方图像验证码破解网站 www.chaojiying.com
    - 极验
        - 破解比较麻烦
        - 可以模拟鼠标移动
        - 一直在进化
