#!/usr/bin/env python
# encoding: utf-8
#origin: https://github.com/nghuyong/WeiboSpider
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.tweet import TweetSpider

if __name__ == '__main__':
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(TweetSpider)
    process.start()
