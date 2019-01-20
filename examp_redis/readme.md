## scrapy redis 


- **创建爬虫**
    - scrapy genspider -t crawl dmoz www.dmoz-odp.org
    
    
- **CrawlerSpider**
    - 为全站爬取而生
    
- **分布式爬虫**
    - 将多台主机组合起来，共同完成一个爬取人物
    - 一个主机，多个从机
    - 结构：一个爬取队列，多个调度器        
    
    - 维护爬取队列
    - 基于内存存储的Reids： 列表、集合、有序集合
        - 列表有lpush()/lpop()/rpush()/rpop() 可以实现fifo, filo队列
        - 集合无序不重复， 有序集合可以控制优先级
        
    - 如何去重
        - Request指纹  
        
    - 防止中断
        - 将队列中的Request保存起来，JOB_DIR指定保存路径
        - 存在Redis队列中       