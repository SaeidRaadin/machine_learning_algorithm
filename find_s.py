import pandas as pd


def find_s(datasets, init_hypotesis):
    for x, y in datasets.iterrows():
        for z in datasets.columns:
            if init_hypotesis[z] != '?':
                if init_hypotesis[z] != y[z]:
                    init_hypotesis[z] = '?'
    return init_hypotesis


# import dataset into pandas dataframe
datasets = pd.read_csv('datasets/enjoy_sport.csv')
print(datasets)
print('--------------------------------------------------------------\n')

# remove any samples with 'no' target
data = datasets[datasets.enjoy_sport != 'no']
print(data)
print('\n')
# drop target atribute
data = data.drop(['enjoy_sport'], axis=1)
# initialize hypotesis
h = data.loc[0]
print(h)
print('\n')

data = data.drop([0], axis=0)
print(data)
print('\n')

print(find_s(data, h))
