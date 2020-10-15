import matplotlib.pyplot as plt

input_values = list(range(1, 6))
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)

# 设置图表标题并给坐标轴加上标签
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax.set_title("平方数", fontsize=20)
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值的平方", fontsize=10)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=10)

plt.show()