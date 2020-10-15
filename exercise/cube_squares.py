import matplotlib.pyplot as plt


# 设置图标风格
plt.style.use('seaborn')

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=1)

# 设置中文字体以及图表标题并给坐标轴加上标签
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax.set_title("立方数", fontsize=20)
ax.set_xlabel('值', fontsize=10)
ax.set_ylabel('值的立方', fontsize=10)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=10)

# 设置每个坐标轴的取值范围
ax.axis([0, 5000, 0, 5000**3])

file_name = 'F:\\Windows\\桌面\\大三上学期\\python\\项目\\Learning-data-visualization\\images\\cube_image.png'
plt.show()
plt.savefig(file_name, bbox_inches='tight')