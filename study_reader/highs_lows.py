import csv
from datetime import datetime
import matplotlib.pyplot as plt


# 从文件中获取最高温度
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))

# 根据最高温图绘制图形
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red')

# 设置图形的格式
ax.set_title('2018年7月每日最高温度', fontsize=20)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('温度（F）', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()