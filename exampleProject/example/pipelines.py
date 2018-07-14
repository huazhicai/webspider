from datetime import datetime


class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.now()
        item["spiders"] = spider.name
        return item