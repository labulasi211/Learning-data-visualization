import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # 创建一个 RandomWalk 实例。
    rw = RandomWalk(100000)
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use('classic')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=1, c=range(rw.num_points), cmap=plt.cm.Blues, edgecolors='none')

    # 突出起点和终点
    ax.scatter(0, 0, s=20, c='green', edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)

    ax.set_title("漫步散点题", fontsize=20)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break