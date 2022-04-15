import pandas as pd

csv_file = './Data/train.csv'

pd_all = pd.read_csv(csv_file)
moods = {0: '喜悦', 1: '愤怒', 2: '厌恶', 3: '低落'}

print('微博数目（总体）：%d' % pd_all.shape[0])

pd_all['label_str'] = pd_all.apply(lambda x: moods[x['label']], axis=1)
pd_all['id'] = 0

train = []
test = []

for label, mood in moods.items():
    label_data = pd_all[pd_all.label == label]
    print('微博数目（{}）：{}'.format(mood, label_data.shape[0]))

    train_num = int(len(label_data) * 0.8)
    train_data = label_data[:train_num].copy()
    train_data['id'] = ['train_{0}'.format(i) for i in range(len(train_data))]
    train.append(train_data)

    test_data = label_data[train_num:].copy()
    test_data['id'] = ['test_{0}'.format(i) for i in range(len(test_data))]
    test.append(test_data)

train_total = pd.concat(train)
test_total = pd.concat(test)

train_total.to_csv('./newData/train.csv')
test_total.to_csv('./newData/test.csv')