import csv
data_ = []
with open('inflation_russia.csv', 'r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=';')
    for i in data:
        print(i)
        data_.append(i)
    # data_ = list(data)