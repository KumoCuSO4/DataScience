import pyecharts.options as opts
from pyecharts.charts import WordCloud
from math import log2
import jieba.analyse
import json

if __name__ == '__main__':
    # 创建停用词列表
    stopwords = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]

    with open("第四阶段评论.json", 'rb') as load_f:
        loads = json.load(load_f)
        dict = {}
        dict1 = {}
        wordnum = 0  # 文档总词数
        num1 = 0     # 总的文档数

        # 加载数据
        for w in loads:
            # 采用jieba分词并统计词频
            num1 += 1
            cutwords = jieba.cut(w['content'])
            for word in cutwords:
                wordnum += 1
                if word in stopwords:
                    continue
                else:
                    if(dict.get(word,'null')=='null'):
                        dict[word] = 1
                        dict1[word] = 1
                    else:
                        dict[word] = dict[word] + 1
        #tfidf关键词提取
        for w in loads:
            for key in dict1:
                if key in w['content']:
                    dict1[key] = dict1[key] + 1

        tfidf = {}
        for word in dict:
            tfidf[word] = (dict[word]/wordnum) * log2(num1/(dict1 [word]))
        tfidf = sorted(tfidf.items(),key=lambda x:x[1], reverse=True)
        print(tfidf)
        # 形成词云图
        WordCloud().add(series_name="关键词分析", data_pair=tfidf[1:151], word_size_range=[10, 50])
        WordCloud().set_global_opts(title_opts=opts.TitleOpts(title="关键词分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)),
                tooltip_opts=opts.TooltipOpts(is_show=True),)
        WordCloud().render("第四阶段评论关键词.html")
