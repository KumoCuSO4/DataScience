import json
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']

bits = 2

ax1 = plt.subplot(3, 1, 1)
plt.xlabel("点赞")
plt.ylabel("概率")
ax2 = plt.subplot(3, 1, 2, sharey=ax1)
plt.xlabel("评论")
plt.ylabel("概率")
ax3 = plt.subplot(3, 1, 3, sharey=ax1)
plt.xlabel("转发")
plt.ylabel("概率")


def paint(name):
    with open(name + "_tweets.json", 'rb') as load_f:
        load_dict = json.load(load_f)

    likes_dict = {}
    comments_dict = {}
    reposts_dict = {}
    likes_list = []
    comments_list = []
    reposts_list = []
    i = 0
    for d in load_dict:
        i = i + 1
        like_num = d['like_num']
        comment_num = d['comment_num']
        repost_num = d['repost_num']

        likes_list.append(like_num)
        comments_list.append(comment_num)
        reposts_list.append(repost_num)

        x = round(like_num / 10000, bits)
        if x in likes_dict.keys():
            likes_dict[x] = likes_dict[x] + 1
        else:
            likes_dict[x] = 1

        x = round(comment_num / 1000, bits)
        if x in comments_dict.keys():
            comments_dict[x] = comments_dict[x] + 1
        else:
            comments_dict[x] = 1

        x = round(repost_num / 1000, bits)
        if x in reposts_dict.keys():
            reposts_dict[x] = reposts_dict[x] + 1
        else:
            reposts_dict[x] = 1
    likes = sorted(likes_dict.items(), key=lambda p: p[0])
    comments = sorted(comments_dict.items(), key=lambda p: p[0])
    reposts = sorted(reposts_dict.items(), key=lambda p: p[0])

    x1 = []
    y1 = []
    for d in likes:
        x1.append(d[0])
        y1.append(float(d[1]) / (i * pow(0.1, bits)))

    x2 = []
    y2 = []
    for d in comments:
        x2.append(d[0])
        y2.append(float(d[1]) / (i * pow(0.1, bits)))

    x3 = []
    y3 = []
    for d in reposts:
        x3.append(d[0])
        y3.append(float(d[1]) / (i * pow(0.1, bits)))

    if name == 'ysxw':
        c = "red"
        l = "央视新闻"
    elif name == 'rmrb':
        c = "blue"
        l = "人民日报"
    elif name == 'ttxw':
        c = "green"
        l = "头条新闻"
    elif name == 'xhsd':
        c = "yellow"
        l = "新华视点"

    ax1.plot(x1, y1, color=c, label=l)
    ax2.plot(x2, y2, color=c, label=l)
    ax3.plot(x3, y3, color=c, label=l)

    n1 = np.array(likes_list)
    n2 = np.array(comments_list)
    n3 = np.array(reposts_list)
    chart = np.array([n1, n2, n3])

    chart_pd = pd.DataFrame(chart.T, columns=['点赞', '评论', '转发'])
    chart_corr = chart_pd.corr(method='pearson')  # 相关系数矩阵
    print(chart_corr)

if __name__ == '__main__':
    paint('ysxw')
    paint('rmrb')
    paint('xhsd')
    paint('ttxw')

    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    ax3.legend(loc='upper right')
    plt.show()
