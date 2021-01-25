import pyecharts.options as opts
from pyecharts.charts import Bar
import jieba.analyse
import json
from datetime import datetime

if __name__ == '__main__':
    # 导入心态词典
    moodwords1 = [line.strip() for line in open('赞美.txt', encoding='UTF-8').readlines()]
    moodwords2 = [line.strip() for line in open('悲伤.txt', encoding='UTF-8').readlines()]

    with open("Comments.json", 'rb') as load_f:
        loads = json.load(load_f)
        dict1 = {}
        dict2 = {}
        x_data = []
        y1_data = []
        y2_data = []

        # 加载数据
        for w in loads:
            # 采用jieba分词并统计词频
            dt = datetime.strptime(w['created_at'], '%Y-%m-%d %H:%M:%S').date()
            cutwords = jieba.cut(w['content'])
            for word in cutwords:
                if (dict1.get(dt, 'null') == 'null'):
                    dict1[dt] = 0
                    dict2[dt] = 0
                if word in moodwords1:
                    dict1[dt] = dict1[dt] + w['like_num']#加权
                if word in moodwords2:
                    dict2[dt] = dict2[dt] + w['like_num']
        for i in dict1:
            x_data.append(i)
            y1_data.append(dict1[i])
            y2_data.append(dict2[i])
        print(y1_data)
    #建立柱状图
    (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis("赞美", y1_data)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="疫情期间群众心情变化分析图：赞美"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
            .render("心态变化图：赞美.html")
    )