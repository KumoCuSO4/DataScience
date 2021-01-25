# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from settings import MONGO_HOST, MONGO_PORT


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['weibo']
        self.Comments = db["Comments"]

    def process_item(self, item, spider):
        if spider.name == 'comment_spider':
            self.insert_item(self.Comments, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass
