import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 创建一个 RandomWalk 实例。
rw = RandomWalk()
rw.fill_walk()
# 将所有的点都绘制出来
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=10, c=(0, 0.8, 0))
plt.show()