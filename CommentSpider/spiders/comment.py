#!/usr/bin/env python
# encoding: utf-8
import json
import re

import pymongo
from lxml import etree
from scrapy import Spider
from scrapy.http import Request
import time
from items import CommentItem
from spiders.utils import extract_comment_content, time_fix


class CommentSpider(Spider):
    name = "comment_spider"
    base_url = "https://weibo.cn"

    def start_requests(self):
        with open("xhsd_tweets.json", 'rb') as load_f:
            load_dict = json.load(load_f)

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['weibo']
        col = db['Comments']

        output = []
        for x in load_dict:
            f = col.find({'weibo_id': x['_id']})
            if f.count() == 0:
                url = f"{self.base_url}/comment/hot/{x['_id']}?rl=1&page=1"
                print(url)
                yield Request(url, callback=self.parse)
            else:
                for comment in f:
                    output.append(comment)
        with open("output.json", "wb") as f:
            f.write(json.dumps(output, indent=4, ensure_ascii=False).encode('utf-8'))

    def parse(self, response):
        tree_node = etree.HTML(response.body)
        comment_nodes = tree_node.xpath('//div[@class="c" and contains(@id,"C_")]')
        for comment_node in comment_nodes:
            comment_user_url = comment_node.xpath('.//a[contains(@href,"/u/")]/@href')
            if not comment_user_url:
                continue
            comment_item = CommentItem()
            comment_item['crawl_time'] = int(time.time())
            comment_item['weibo_id'] = response.url.split('/')[-1].split('?')[0]
            comment_item['comment_user_id'] = re.search(r'/u/(\d+)', comment_user_url[0]).group(1)
            comment_item['content'] = extract_comment_content(etree.tostring(comment_node, encoding='unicode'))
            comment_item['_id'] = comment_node.xpath('./@id')[0]
            created_at_info = comment_node.xpath('.//span[@class="ct"]/text()')[0]
            like_num = comment_node.xpath('.//a[contains(text(),"赞[")]/text()')[-1]
            comment_item['like_num'] = int(re.search('\d+', like_num).group())
            comment_item['created_at'] = time_fix(created_at_info.split('\xa0')[0])
            yield comment_item
