# -*- coding: utf-8 -*-
from scrapy import Item, Field


class CommentItem(Item):
    """
    微博评论信息
    """
    _id = Field()
    comment_user_id = Field()  # 评论用户的id
    content = Field()  # 评论的内容
    weibo_id = Field()  # 评论的微博的id
    created_at = Field()  # 评论发表时间
    like_num = Field()  # 点赞数
    crawl_time = Field()  # 抓取时间戳
