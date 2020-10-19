from datetime import datetime
import matplotlib.pyplot as plt
import csv


file_name = '../data/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期，每日最高温度以及最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        try:
            high = int(row[4])
        except ValueError:
            print(f'Missing data of high temperature for {current_date}.')
        highs.append(high)
        try:
            low = int(row[5])
        except ValueError:
            print(f'Missing data of low temperature for {current_date}')
        lows.append(low)

# 根据每日最高温度与最低温度来绘制图形
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 一些图像设置
ax.set_title('2018死亡谷每日最高温度与最低温度', fontsize=20)
ax.set_xlabel('日期', fontsize=10)
ax.set_ylabel('温度（F）', fontsize=10)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()