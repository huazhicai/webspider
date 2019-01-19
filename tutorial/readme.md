## scrapy tutorial

- **创建Spider**
    - scrapy startproject tutorial && cd tutorial
    - scrapy genspider quotes quotes.toscrape.com
    - name 每个项目的唯一名字，用来区分不同的的Spider
    - allowed_domains 如果初始或后续的请求链接不是这个域名下的，则请求链接会被过滤掉
    - start_urls 定义初始请求
    - custom_settings 字典，专属于本spider的配置，覆盖全局配置
    - crawler 它由from_crawler()方法设置，代表本spider类对应的 Crawler 对象。
    - start_requests() 此方法用于生成初始请求，他返回一个可迭代对象，默认使用start_urls里的url
    而且是GET请求方法，如果要POST，可以重写这个方法
    - parse 解析返回的响应

- **运行爬虫**
    - scrapy crawl quotes
    - scrapy crawl quotes -o quotes.json/quotes.jl (jsonline的缩写)
    - scrapy crawl quotes -o quotes.csv/quotes.xml/quotes.pickle
    - ftp://user:password@ftp.example.com/path/to/quotes.csv

- **Item Pipeline 项目管道**
    - 清理HTML数据
    - 验证爬虫数据，检查爬虫字段
    - 查重并丢弃重复内容
    - 将爬取的结果保存到数据库
    
    - 定义一个类实现process_item()方法即可
    - @classmethod  # 类方法在此方法内部使用类和类属性而不需要实例调用

