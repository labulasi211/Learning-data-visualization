import csv
from datetime import datetime


# 从文件中获取最高温度
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))

    print(highs)
    print(dates)