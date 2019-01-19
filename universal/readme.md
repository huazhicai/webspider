## scrapy universal 


- **通用爬虫**
   
- **创建**
    - scrapy genspider -t crawl china tech.china.com
    
- ItemLoader提供填充容器机制
- iteme对象提供add_css()、add_xpath()、add_value()等方法填充Item对象
- Input Processor 和 Out Processor 
- TakeFirst返回列表第一个非空值
- Join 相当于字符串的join
- Compose 多个函数组合构造Processor,其输出再传递到第二个函数
- MapCompose处理一个列表输入值       