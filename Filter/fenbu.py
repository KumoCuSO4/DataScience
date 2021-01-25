# encoding=utf-8
import json
import math

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import scipy.stats as st
plt.rcParams['font.sans-serif'] = ['SimHei']

weight = {'like_num': 50000, 'comment_num': 3000, 'repost_num': 2500}
bits = 2


# 自定义函数 e指数形式
def func(x, a, u, sig):
    return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)) * (431 + (4750 / x))


if __name__ == '__main__':
    with open("ttxw.json", 'rb') as load_f:
        load_dict = json.load(load_f)

    my_dict = {}
    i = 0
    w = []
    for d in load_dict:
        i = i + 1
        weighted = (d['like_num'] / weight['like_num']
                    + d['comment_num'] / weight['comment_num']
                    + d['repost_num'] / weight['repost_num'])
        if weighted < 20:
            w.append(weighted)
        x = round(weighted, bits)
        if x in my_dict.keys():
            my_dict[x] = my_dict[x] + 1
        else:
            my_dict[x] = 1
    items = sorted(my_dict.items(), key=lambda p: p[0])
    print(items)
    x = []
    y = []
    for d in items:
        x.append(d[0])
        y.append(float(d[1]) / (i * pow(0.1, bits)))

    sns.set_palette("hls")  # 设置所有图的颜色，使用hls色彩空间

    # print(scipy.stats.kstest(w, 'norm', alternative='two-sided', mode='approx'))

    sum = 0
    i = 0
    for num in w:
        sum = sum + num
        i = i + 1
    mu = sum / i
    print(mu)
    sum = 0
    for num in w:
        sum = sum + pow(num-mu, 2)
    sig2 = sum/i
    print(sig2)

    print(st.f.fit(w))
    print(st.kstest(w, 'f', args={4.674778113098572, 2.286074375310185}, alternative='two-sided', mode='approx'))
    x1 = np.linspace(-1, 8, 100000)
    y1 = st.f.pdf(x1, 4.674778113098572, 2.286074375310185, 0.002319518312796533, 0.18146554308894638)
    plt.plot(x1, y1)
    sns.distplot(w, bins=[x / 100 for x in range(0, 2000)], label="F分布")
    plt.show()

    '''ax1 = plt.subplot(221)
    ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
    ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)
    ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)

    sns.distplot(w, bins=[x / 100 for x in range(-1000, 1000)], fit=st.norm, label="正态分布", ax=ax1)
    sns.distplot(w, bins=[x / 100 for x in range(-1000, 1000)], fit=st.chi2, label="卡方分布", ax=ax2)
    sns.distplot(w, bins=[x / 100 for x in range(-1000, 1000)], fit=st.gamma, label="伽马分布", ax=ax3)
    sns.distplot(w, bins=[x / 100 for x in range(-1000, 1000)], fit=st.f, label="F分布", ax=ax4)
    
    plt.xlim(-4, 4)
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    ax3.legend(loc='upper right')
    ax4.legend(loc='upper right')
    plt.show()'''
