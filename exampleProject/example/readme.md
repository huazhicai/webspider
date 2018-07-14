## Scrapy Redis Example Project

- 此目录包含使用scrapy-redis集成的示例Scrapy项目。 默认情况下，所有字段都
将发送到redis（key <spider>：items）。 所有爬虫通过redis调度requests，
因此你可以启动其他爬虫来加速爬行。

### Spider
- dmoz
    - 这个爬虫爬取 dmoz-odp.org 网站
- myspider_redis
    - 这个爬虫使用redis作为共享请求队列，并使用myspider：
    start_urls作为起始URL种子。 对于每个URL，爬虫输出一个字段。
- mycrawler_redis
    - 这个爬虫使用redis作为共享请求队列，并使用mycrawler：start_urls作为
    起始URL种子。 对于每个URL，这个爬虫爬取的是链接。

#### Note
- 默认情况下，所有请求都会保留。您可以使用SCHEDULER_FLUSH_ON_START设置清除队列。
例如：scrapy crawl dmoz -s SCHEDULER_FLUSH_ON_START = 1。

### Processing items
- The process_items.py provides an example of consuming the items queue:
> python process_items.py --help



