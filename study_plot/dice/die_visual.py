from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die


die = Die()

results = []
for value in range(10000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_value = list(range(die.num_sides))
y_value = frequencies
data = [Bar(x=x_value, y=y_value)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='投一个D6 10000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')