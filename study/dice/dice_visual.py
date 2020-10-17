import matplotlib
import matplotlib.pyplot as plt


from die import Die

# 对pyplot进行一些设置
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 创建两个Die类
die_1 = Die()
die_2 = Die(10)

results = []
for value in range(50_000):
    result = die_2.roll()+die_1.roll()
    results.append(result)

# 分析结果
max_result = die_2.num_sides + die_1.num_sides
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_value = list(range(2, max_result+1))
y_value = frequencies
fig, ax = plt.subplots(figsize=(10,6))

ax.bar(x_value, y_value)
ax.set_xlabel('结果', fontsize=10)
ax.set_ylabel('结果的频率', fontsize=10)
ax.set_title('投一个D6和一个D10 50 000次的结果', fontsize=20)

plt.show()