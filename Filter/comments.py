from datetime import datetime
import json


def sep(name):
    with open(name + '_comments.json', 'rb') as f:
        load_dict = json.load(f)
    load_dict = sorted(load_dict, key=lambda x: datetime.strptime(x['created_at'], '%Y-%m-%d %H:%M:%S').date())
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    for d in load_dict:
        date = datetime.strptime(d['created_at'], '%Y-%m-%d %H:%M:%S')
        if date < datetime.strptime('2020-01-23', '%Y-%m-%d'):
            f1.append(d)
        elif datetime.strptime('2020-01-23', '%Y-%m-%d') <= date < datetime.strptime('2020-02-10', '%Y-%m-%d'):
            f2.append(d)
        elif datetime.strptime('2020-02-10', '%Y-%m-%d') <= date < datetime.strptime('2020-04-04', '%Y-%m-%d'):
            f3.append(d)
        else:
            f4.append(d)

    with open(name + "1.json", "wb") as f:
        f.write(json.dumps(f1, indent=4, ensure_ascii=False).encode('utf-8'))
    with open(name + "2.json", "wb") as f:
        f.write(json.dumps(f2, indent=4, ensure_ascii=False).encode('utf-8'))
    with open(name + "3.json", "wb") as f:
        f.write(json.dumps(f3, indent=4, ensure_ascii=False).encode('utf-8'))
    with open(name + "4.json", "wb") as f:
        f.write(json.dumps(f4, indent=4, ensure_ascii=False).encode('utf-8'))


if __name__ == '__main__':
    sep('rmrb')
    sep('ysxw')
    sep('ttxw')
    sep('xhsd')
