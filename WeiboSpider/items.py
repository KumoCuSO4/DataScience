# -*- coding: utf-8 -*-
from scrapy import Item, Field


class TweetItem(Item):
    """Tweet information """
    _id = Field()  # 微博id
    weibo_url = Field()  # 微博URL
    created_at = Field()  # 微博发表时间
    like_num = Field()  # 点赞数
    repost_num = Field()  # 转发数
    comment_num = Field()  # 评论数
    content = Field()  # 微博内容
    user_id = Field()  # 发表该微博用户的id
    tool = Field()  # 发布微博的工具
    image_url = Field()  # 图片
    video_url = Field()  # 视频
    origin_weibo = Field()  # 原始微博，只有转发的微博才有这个字段
    location_map_info = Field()  # 定位的经纬度信息
    crawl_time = Field()  # 抓取时间戳
