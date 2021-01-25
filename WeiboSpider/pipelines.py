# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from settings import MONGO_HOST, MONGO_PORT


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['weibo']
        self.Tweets = db["Tweets"]

    def process_item(self, item, spider):
        if spider.name == 'tweet_spider':
            self.insert_item(self.Tweets, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass
