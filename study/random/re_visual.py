import plotly.offline as offlien
import plotly.graph_objs as go

from random_walk import RandomWalk


while True:
    # 创建一个 RandomWalk 实例。
    rw = RandomWalk(10_000)
    rw.fill_walk()
    # 将所有的点都绘制出来
    fig = go.Scatter(x=rw.x_values, y=rw.y_values, mode='markers', marker=dict(size=2))

    offlien.plot({'data': fig}, filename='random.html')

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break