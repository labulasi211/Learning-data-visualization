import csv
from datetime import datetime
import matplotlib.pyplot as plt


def read_file_data(file_name):
    # 根据文件名找到对应的文件来读取里面一些特定的信息
    data = {
        'highs': [],
        'lows': [],
        'dates': [],
        'precipitation': [],
        'name': ''
    }
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # 记录需要储存的数据所在行的位置
        for index, column_header in enumerate(header_row):
            if column_header == 'NAME':
                name_index = index
            elif column_header == 'PRCP':
                prcp_index = index
            elif column_header == 'TMAX':
                high_index = index
            elif column_header == 'TMIN':
                low_index = index
            elif column_header == 'DATE':
                date_index = index

        # 开始记录数据
        value = 0
        high, low, current_data, prcp = 0, 0, '2018-1-1', 0
        for row in reader:
            value += 1
            # 记录名字
            try:
                high = int(row[high_index])
            except ValueError:
                print(f'the {value} line missed the data of high temperature.')
            try:
                low = int(row[low_index])
            except ValueError:
                print(f'the {value} line missed the data of low temperature.')
            try:
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            except ValueError:
                print(print(f'the {value} line missed the data of current date.'))
            try:
                prcp = float(row[prcp_index])
            except ValueError:
                print(print(f'the {value} line missed the data of precipitation.'))

            data['highs'].append(high)
            data['lows'].append(low)
            data['precipitation'].append(prcp)
            data['dates'].append(current_date)
        data['name'] = row[name_index]

        return data

def show_plot(data):
    """通过特定的气候数据字典将最高温度，最低温度以及降雨量同时绘制在一个图上"""
    # 根据最高温度和最低温度以及降雨量绘制图形
    plt.style.use('seaborn')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['dates'], data['highs'], c='red', alpha=0.5, linewidth=1)
    ax.plot(data['dates'], data['lows'], c='green', alpha=0.5, linewidth=1)
    ax.fill_between(data['dates'], data['highs'], data['lows'], facecolor='green', alpha=0.1)
    ax2 = ax.twinx()
    ax2.plot(data['dates'], data['precipitation'], c='blue', alpha=0.5, linewidth=1)

    # 设置图形的格式
    ax.set_title(data['name'], fontsize=20)
    ax.set_xlabel('日期', fontsize=10)
    ax.set_ylabel('温度（F）', fontsize=10)
    fig.autofmt_xdate()
    ax2.set_ylabel('降雨量', fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.set_ylim(0, 100)

    plt.show()