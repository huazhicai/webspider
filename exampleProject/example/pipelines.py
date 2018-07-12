from datetime import datetime


class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.now()
        item["spider"] = spider.name
        return item