from datetime import datetime
import json
import time

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
x = []
y = []

if __name__ == '__main__':
    weight = {'like_num': 50000, 'comment_num': 3000, 'repost_num': 2500}

    with open("ysxw.json", 'rb') as load_f:
        load_dict = json.load(load_f)
    weights = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}

    output = []

    data = {'likes': 0, 'comments': 0, 'reposts': 0}
    i = 0
    for d in load_dict:
        # print(d['content'])
        '''if d['repost_num'] > 1000000:
            print(d['weibo_url'])'''

        # print(datetime.strptime(d['created_at'], '%Y-%m-%d %H:%M:%S').date())
        x.append(datetime.strptime(d['created_at'], '%Y-%m-%d %H:%M:%S').date())

        weighted = (d['like_num'] / weight['like_num']
                    + d['comment_num'] / weight['comment_num']
                    + d['repost_num'] / weight['repost_num'])
        y.append(weighted)

        '''if weighted > 100:
            print(d['weibo_url'])'''

        data['likes'] = data['likes'] + d['like_num']
        data['comments'] = data['comments'] + d['comment_num']
        data['reposts'] = data['reposts'] + d['repost_num']
        i = i + 1

        if weighted < 1:
            weights['1'] = weights['1'] + 1
        elif weighted < 2:
            weights['2'] = weights['2'] + 1
        elif weighted < 3:
            weights['3'] = weights['3'] + 1
        elif weighted < 4:
            weights['4'] = weights['4'] + 1
        elif weighted < 5:
            weights['5'] = weights['5'] + 1
        elif weighted < 6:
            weights['6'] = weights['6'] + 1
        elif weighted < 7:
            weights['7'] = weights['7'] + 1
        elif weighted < 8:
            weights['8'] = weights['8'] + 1
        elif weighted < 9:
            weights['9'] = weights['9'] + 1
        else:
            weights['10'] = weights['10'] + 1

        '''if weighted > 0.22:
            output.append(d)'''
        '''if weighted > 50:
            print(d['weibo_url'])'''
        if d['like_num'] > 1500000:
            print(d['weibo_url'])
    print(weights)

    '''with open("output.json", "wb") as f:
        f.write(json.dumps(output, indent=4, ensure_ascii=False).encode('utf-8'))'''

    print(data)
    print(data['likes'] / i)
    print(data['comments'] / i)
    print(data['reposts'] / i)

    plt.plot(x, y, 'ob')
    plt.xlabel("时间")
    plt.ylabel("加权热点系数")
    plt.show()
