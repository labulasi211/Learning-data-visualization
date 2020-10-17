from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

# 创建两个Die类
die_1 = Die(8)
die_2 = Die(8)

results = []
for value in range(50_0000):
    result = die_2.roll()*die_1.roll()
    results.append(result)

# 分析结果
max_result = die_2.num_sides * die_1.num_sides
frequencies = []
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_value = list(range(1, max_result+1))
y_value = frequencies
data = [Bar(x=x_value, y=y_value)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='同时投两个D8面数相乘 50000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8 x d8.html')