import matplotlib.pyplot as plt


plt.style.use('seaborn')
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.Blues)

# 设置图表标题并给坐标轴加上标签
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax.set_title("平方数", fontsize=20)
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值的平方", fontsize=10)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=10)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

file_name = '/images/squares_plot.png'
plt.savefig(file_name, bbox_inches='tight')