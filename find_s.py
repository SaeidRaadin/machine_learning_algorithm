import pandas as pd

datasets = pd.read_csv('datasets/enjoy_sport.csv')
print(datasets)
print('--------------------------------------------------------------\n')

data = datasets[datasets.enjoy_sport != 'no']
print(data)
print('\n')
data = data.drop(['enjoy_sport'], axis=1)
h = data.loc[0]
print(h)
print('\n')
data = data.drop([0], axis=0)
print(data)
print('\n')
for x, y in data.iterrows():
    for z in data.columns:
        if h[z] != '?':
            if h[z] != y[z]:
                h[z] = '?'

print(h)
