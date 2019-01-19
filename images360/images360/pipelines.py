# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.collection
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline(object):
    def __init__(self, host, user, password, db, port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            db=crawler.settings.get('MYSQL_DATABASE'),
            port=crawler.settings.get('MYSQL_PORT'),
        )
        return cls

    def open_spider(self, spider):
        self.conn = pymysql.connect(self.host, self.user, self.password,
                                    self.db, charset='utf8', port=self.port)
        self.cursor = self.conn.cursor()

    def prosess_item(self, item, spider):
        print(item['title'])
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%S)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()
        return item

    def close_item(self, spider):
        self.cursor.close()
        self.conn.close()


class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        yield Request(item['url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

