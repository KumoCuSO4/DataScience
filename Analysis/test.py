from math import log2
import jieba.analyse
import json

if __name__ == '__main__':
    # 导入心态词典
    moodwords = [line.strip() for line in open('心态词典.txt', encoding='UTF-8').readlines()]
    ws = [line.strip() for line in open('新建文本文档.txt', encoding='UTF-8').readlines()]
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

    with open("Comments.json", 'rb') as load_f:
        loads = json.load(load_f)
        wordnum = 0  # 文档总词数
        num1 = 0  # 总的文档数
        dict = {}
        dict1 = {}
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
                        dict[word] = 1
                        dict1[word] = 1
                    else:
                        dict[word] = dict[word] + 1
        # tfidf关键词提取
        for w in loads:
            for key in dict1:
                if key in w['content']:
                    dict1[key] = dict1[key] + 1
        tfidf = {}
        for word in dict:
            tfidf[word] = (dict[word] / wordnum) * log2(num1 / (dict1[word]))
        #统计对应心态的占比
        for word in dict:
            if word in moodwords1:
                mood['开心'] += tfidf[word]
            if word in moodwords2:
                mood['赞美'] += tfidf[word]
            if word in moodwords3:
                mood['关切'] += tfidf[word]
            if word in moodwords4:
                mood['感动'] += tfidf[word]
            if word in moodwords5:
                mood['坚定'] += tfidf[word]
            if word in moodwords6:
                mood['期盼'] += tfidf[word]
            if word in moodwords7:
                mood['悲伤'] += tfidf[word]
            if word in moodwords8:
                mood['反对'] += tfidf[word]
            if word in moodwords9:
                mood['担忧'] += tfidf[word]
            if word in moodwords10:
                mood['愤怒'] += tfidf[word]
            if word in moodwords11:
                mood['恐惧'] += tfidf[word]
            if word in moodwords12:
                mood['急切'] += tfidf[word]
        for i in mood:
            y.append(mood[i])
        #反向拟合
        for w in loads:
            t = 0
            cw = jieba.cut(w['content'])
            for word in cw:
                if word in ws:
                    t = 1
            if t ==1:
                print(w['content'])
                #if word in moodwords1:
                #    print("开心", end='')
                #if word in moodwords2:
                #    print("赞美", end='')
                #if word in moodwords3:
                #    print("关切", end='')
                #if word in moodwords4:
                #    print("感动", end='')
                #if word in moodwords5:
                #    print("坚定", end='')
                #if word in moodwords6:
                #    print("期盼", end='')
                #if word in moodwords7:
                #    print("悲伤", end='')
                #if word in moodwords8:
                #    print("反对", end='')
                #if word in moodwords9:
                #    print("担忧", end='')
                #if word in moodwords10:
                #    print("愤怒", end='')
                #if word in moodwords11:
                #    print("恐惧", end='')
                #if word in moodwords12:
                #    print("急切", end='')