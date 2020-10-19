import csv
from datetime import datetime
import matplotlib.pyplot as plt


# 从文件中获取每日最高温度，日期，以及每日最低温度
filename = '../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))
        lows.append(int(row[6]))


# 根据最高温和最低温图绘制图形
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title('2018年每日最高温度与最低温度', fontsize=20)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('温度（F）', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)


plt.show()