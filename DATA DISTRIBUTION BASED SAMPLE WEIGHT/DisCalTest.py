import pandas as pd
from scipy.spatial import distance

# 读取数据
data = pd.read_excel(r'haberman.xlsx')
data = data.drop_duplicates(subset=['Age', 'Year'])
X, y = data.iloc[:, :-1], data.iloc[:, -1]

# 获取指定索引的样本
sample_2 = X.iloc[2].values
sample_0 = X.iloc[0].values
samples_2_neighbors = [X.iloc[i].values for i in [13, 135, 130]]
samples_0_neighbors = [X.iloc[i].values for i in [16, 73, 143, 29, 86]]

distance_sum_2 = sum(distance.euclidean(sample_2, neighbor) for neighbor in samples_2_neighbors)
distance_inverse_sum_2 = sum((1 / distance.euclidean(sample_2, neighbor)) for neighbor in samples_2_neighbors)

distance_sum_0 = sum(distance.euclidean(sample_0, neighbor) for neighbor in samples_0_neighbors)
distance_inverse_sum_0 = sum((1 / distance.euclidean(sample_0, neighbor)) for neighbor in samples_0_neighbors)

# 输出结果
print(f"索引2样本与13, 142, 220样本的欧式距离之和: {distance_sum_2:.4f}")
print(f"索引2样本与13, 142, 220样本的距离倒数之和: {distance_inverse_sum_2:.4f}")
print(f"索引0样本与16, 75, 152, 29, 89样本的欧式距离之和: {distance_sum_0:.4f}")
print(f"索引0样本与16, 75, 152, 29, 89样本的距离倒数之和: {distance_inverse_sum_0:.4f}")

generalDensity_2 = distance_inverse_sum_2 / (len(samples_2_neighbors) * 0.6794185617462776)
generalDensity_0 = distance_inverse_sum_0 / (len(samples_0_neighbors) * 0.6794185617462776)
print(f"索引2的一般密度为：{generalDensity_2:.4f}")
print(f"索引0的一般密度为：{generalDensity_0:.4f}")