import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 创建一个 RandomWalk 实例。
rw = RandomWalk(100000)
rw.fill_walk()
# 将所有的点都绘制出来
plt.style.use('classic')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=1, c=(0, 0.8, 0))
ax.set_title("漫步散点题", fontsize=20)
plt.show()