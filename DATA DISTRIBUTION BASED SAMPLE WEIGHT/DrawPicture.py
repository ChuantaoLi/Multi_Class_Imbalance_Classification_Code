import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel(r'haberman.xlsx')
data = data.drop_duplicates(subset=['Age', 'Year'])
X, y = data.iloc[:, :-1], data.iloc[:, -1]

# 创建散点图，y=-1 的点为蓝色，y=1 的点为红色
plt.figure(figsize=(14, 8.6))
scatter = plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=plt.cm.bwr, marker='o')

# 标记特定的样本点
highlighted_points_black = [2, 13, 135, 130]  # 黑色标记的样本索引
highlighted_points_red = [0, 16, 73, 143, 29, 86]  # 红色标记的样本索引
highlighted_points_blue = [6, 106, 60]  # 蓝色标记的样本索引

# 用黑色标记
for idx in highlighted_points_black:
    plt.annotate(f'({idx})',
                 (X.iloc[idx, 0], X.iloc[idx, 1]),
                 textcoords="offset points",
                 xytext=(0, 5),
                 ha='center',
                 fontsize=12,
                 color='black')

# 用红色标记
for idx in highlighted_points_red:
    plt.annotate(f'({idx})',
                 (X.iloc[idx, 0], X.iloc[idx, 1]),
                 textcoords="offset points",
                 xytext=(0, 5),
                 ha='center',
                 fontsize=12,
                 color='red')

# 用蓝色标记
for idx in highlighted_points_blue:
    plt.annotate(f'({idx})',
                 (X.iloc[idx, 0], X.iloc[idx, 1]),
                 textcoords="offset points",
                 xytext=(0, 5),
                 ha='center',
                 fontsize=12,
                 color='blue')

# 添加图形标题和标签
plt.title('Scatter plot of the data', fontsize=16)
plt.xlabel(X.columns[0], fontsize=14)
plt.ylabel(X.columns[1], fontsize=14)

# 显示图形
plt.tight_layout()
plt.show()
