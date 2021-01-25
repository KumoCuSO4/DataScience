import pyecharts.options as opts
from pyecharts.charts import Radar
from math import log2
import jieba.analyse
import json

if __name__ == '__main__':
    # 导入心态词典
    moodwords = [line.strip() for line in open('心态词典.txt', encoding='UTF-8').readlines()]
    moodwords1 = [line.strip() for line in open('开心.txt', encoding='UTF-8').readlines()]
    moodwords2 = [line.strip() for line in open('赞美.txt', encoding='UTF-8').readlines()]
    moodwords3 = [line.strip() for line in open('关切.txt', encoding='UTF-8').readlines()]
    moodwords4 = [line.strip() for line in open('感动.txt', encoding='UTF-8').readlines()]
    moodwords5 = [line.strip() for line in open('坚定.txt', encoding='UTF-8').readlines()]
    moodwords6 = [line.strip() for line in open('期盼.txt', encoding='UTF-8').readlines()]
    moodwords7 = [line.strip() for line in open('悲伤.txt', encoding='UTF-8').readlines()]
    moodwords8 = [line.strip() for line in open('反对.txt', encoding='UTF-8').readlines()]
    moodwords9 = [line.strip() for line in open('担忧.txt', encoding='UTF-8').readlines()]
    moodwords10 = [line.strip() for line in open('愤怒.txt', encoding='UTF-8').readlines()]
    moodwords11 = [line.strip() for line in open('恐惧.txt', encoding='UTF-8').readlines()]
    moodwords12 = [line.strip() for line in open('急切.txt', encoding='UTF-8').readlines()]

    with open("第四阶段评论.json", 'rb') as load_f:
        loads = json.load(load_f)
        wordnum = 0  # 文档总词数
        num1 = 0  # 总的文档数
        dict = {}
        mood = {'开心': 0, '赞美': 0, '关切': 0, '感动': 0, '坚定': 0, '期盼': 0, '悲伤': 0, '反对': 0, '担忧': 0,
                '愤怒': 0, '恐惧': 0, '急切': 0}
        x = ["开心", "赞美", "关切", "感动", "坚定", "期盼", "悲伤", "反对", "担忧", "愤怒", "恐惧", "急切"]
        y = []
        # 加载数据
        for w in loads:
            # 采用jieba分词并统计词频
            num1 += 1
            cutwords = jieba.cut(w['content'])
            for word in cutwords:
                wordnum += 1
                if word in moodwords:
                    if (dict.get(word, 'null') == 'null'):
                        dict[word] = w['like_num']  #加权
                    else:
                        dict[word] = dict[word] + w['like_num']

        #统计对应心态的占比
        for word in dict:
            if word in moodwords1:
                mood['开心'] += dict[word]
            if word in moodwords2:
                mood['赞美'] += dict[word]
            if word in moodwords3:
                mood['关切'] += dict[word]
            if word in moodwords4:
                mood['感动'] += dict[word]
            if word in moodwords5:
                mood['坚定'] += dict[word]
            if word in moodwords6:
                mood['期盼'] += dict[word]
            if word in moodwords7:
                mood['悲伤'] += dict[word]
            if word in moodwords8:
                mood['反对'] += dict[word]
            if word in moodwords9:
                mood['担忧'] += dict[word]
            if word in moodwords10:
                mood['愤怒'] += dict[word]
            if word in moodwords11:
                mood['恐惧'] += dict[word]
            if word in moodwords12:
                mood['急切'] += dict[word]
        for i in mood:
            y.append(mood[i])
        print(y)

        #建立镭射图
        (
            Radar()
                .add_schema(
                schema=[
                    opts.RadarIndicatorItem(name="开心", max_=8000000),
                    opts.RadarIndicatorItem(name="赞美", max_=8000000),
                    opts.RadarIndicatorItem(name="关切", max_=8000000),
                    opts.RadarIndicatorItem(name="感动", max_=8000000),
                    opts.RadarIndicatorItem(name="坚定", max_=8000000),
                    opts.RadarIndicatorItem(name="期盼", max_=8000000),
                    opts.RadarIndicatorItem(name="悲伤", max_=8000000),
                    opts.RadarIndicatorItem(name="反对", max_=8000000),
                    opts.RadarIndicatorItem(name="担忧", max_=8000000),
                    opts.RadarIndicatorItem(name="愤怒", max_=8000000),
                    opts.RadarIndicatorItem(name="恐惧", max_=8000000),
                    opts.RadarIndicatorItem(name="急切", max_=8000000),
                ]
            )
                .add("第四阶段群众心态", [y])
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                legend_opts=opts.LegendOpts(selected_mode="single"),
                title_opts=opts.TitleOpts(title="心态分布图"),
            )
                .render("第四阶段群众心态分布图.html")
        )