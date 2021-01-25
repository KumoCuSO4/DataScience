from datetime import datetime
import json
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel("加权热点系数")
plt.ylabel("概率")

weight = {'like_num': 50000, 'comment_num': 3000, 'repost_num': 2500}
bits = 2


def paint(name):
    with open(name + ".json", 'rb') as load_f:
        load_dict = json.load(load_f)

    my_dict = {}
    i = 0
    for d in load_dict:
        i = i + 1
        weighted = (d['like_num'] / weight['like_num']
                    + d['comment_num'] / weight['comment_num']
                    + d['repost_num'] / weight['repost_num'])
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
    plt.plot(x, y, color=c, label=l)


if __name__ == '__main__':
    paint('ysxw')
    paint('rmrb')
    paint('xhsd')
    paint('ttxw')
    plt.legend(loc='upper right')
    plt.show()
