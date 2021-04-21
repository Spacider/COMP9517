import matplotlib.pyplot as plt
import pandas as pd # 导入pandas库用来处理csv文件

unrate = pd.read_csv('data/COVID_train_data.csv') # 读csv文件

first_twelve = unrate[180:192] # 取前12行数据
# first_twelve = unrate
plt.plot(first_twelve['day'], first_twelve['dailly_cases'] / 500)
plt.plot(first_twelve['day'], first_twelve['max_wind_speed'])

plt.xticks(rotation=30) # 有时候x轴标签比较长，就会重叠在一起，这里旋转一定角度就能更方便显示，如下图
plt.xlabel('day') # 给x轴数据加上名称
plt.ylabel('numbers') # 给y轴数据加上名称
plt.title('daily_cases with day') # 给整个图表加上标题

plt.show() # 将刚画的图显示出来