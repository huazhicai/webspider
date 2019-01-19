## scrapy downloadertest

- **DownloaderMiddleware下载器中间件**
    - 修改User-Agent 、处理重定向、设置代理、失败重试、设置Cookies等功能
    - 核心法法
        - process_request(request, spider)
            - 当返回是None, scrapy将继续处理该Request, 所以返回None
            - 当返回是Request时，更低优先级的middleware 的process_request()会停止执行，
            他会被重新返回到scheduler里，称为了一个全新的Request
        - process_response(request, response, spider)
            - 当返回response时，更低优先级的会处理，所以要返回response
        - process_exception(request, exception, spider)
        
- **Spider Middleware**        
    - Response发送spider前对response处理
    - request发送给scheduler前，对response处理
    - item 发送给ItemPipeline 前，对item处理
    
    - process_spider_input(response, spider)
    - process_spider_output(response, result, spider)
    - process_spider_exception(response, exception, spider)
    - process_start_requests(start_requests, spider)
    
- **Item Pipeline**    
    - 清理HTML数据
    - 验证爬虫数据，检查爬虫字段
    - 查重并丢弃重复内容
    - 将爬取结果保存到数据库
    
    - process_item(item, spider) 必须返回一个item对象或者抛出DropItem异常
    - open_spider(spider)
    - close_spider(spider)
    - from_crawler(cls, crawler)