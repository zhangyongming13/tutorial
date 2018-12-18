# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
import pymongo


class TextPipeline(object):
    def __init__(self):
        self.limt = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limt:
                # 如果text字段长度大于50，就截取前50，rstrip去掉多余的空格，然后拼接省略符
                item['text'] = item['text'][0:self.limt].rstrip() + '...'
            return item
        else:
            # 没有字符则抛出DropItem错误
            return DropItem('Missing Test')


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod  # 一种依赖注入的方式，方法参数就是crawler，这样就通过crawler
    # 拿到全局配置settings.py，在其中可以定义MONOGO_URL和MONOGO_DB来指定需要连接的地址和数据库名称
    def from_crawler(cls, crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):  # 打开数据库
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        # 执行了数据的插入操作
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):  # 关闭数据库
        self.client.close()
