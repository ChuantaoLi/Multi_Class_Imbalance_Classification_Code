from ImbalanceRatio import *
from FindNearestNeighbors import *
from CalculateSameClassNeighbors import *
from GeneralDensity import *
from InverseGeneralDensity import *
from ComputeDataDistributionFactor import *

data = pd.read_excel(r'haberman.xlsx')
data = data.drop_duplicates(subset=['Age', 'Year'])
# data.to_csv(r'delect_haberman.csv', index=False)
X, y = data.iloc[:, :-1], data.iloc[:, -1]

# 计算不平衡比
categorySamples, imbalanceRatios = ImbalanceRatio(X.values, y.values)  # categorySamples 是一个字典，键是类别

# 计算每个样本的5个最近邻的索引和距离
withinClassNeighbor = {}
withinDistanceNeighbor = {}
for category in categorySamples.values():
    for sample in category:
        sampleTuple = tuple(sample)
        withinClassNeighbor[sampleTuple], withinDistanceNeighbor[sampleTuple] = FindNearestNeighbors(X.values, sample,
                                                                                                     5)

print('每个样本的近邻集合的样本索引：')
print(withinClassNeighbor)
print('每个样本的近邻集合的距离：')
print(withinDistanceNeighbor)

# 计算每个样本的类内近邻集合
kiLabelNeighbor, k_i = CalculateSameClassNeighbors(withinClassNeighbor, y)
print('每个样本的近邻集合中相同类别的样本索引：')
print(kiLabelNeighbor)
print('每个样本的近邻集合中相同类别的样本数量：')
print(k_i)

# 计算每个样本的一般密度
generalDensities = GeneralDensity(X.values, kiLabelNeighbor, k_i)
print('每个样本的一般密度：')
print(generalDensities)

# 计算每个样本的逆密度
inverseDensities = InverseGeneralDensity(X.values, y, generalDensities)
print('每个样本的逆密度：')
print(inverseDensities)

# 计算数据分布因子
dataDistributionFactor = ComputeDataDistributionFactor(X.values, y.values, inverseDensities, imbalanceRatios)
print('每个样本的数据分布因子：')
print(dataDistributionFactor)

# 转换字典为列表，按样本顺序排列
kiLabelNeighborList = [kiLabelNeighbor.get(tuple(sample), []) for sample in X.values]
k_iList = [k_i.get(tuple(sample), 0) for sample in X.values]
generalDensitiesList = [generalDensities.get(tuple(sample), 0) for sample in X.values]
inverseDensitiesList = [inverseDensities.get(tuple(sample), 0) for sample in X.values]

# 将新列添加到原始数据集
data['kiLabelNeighbor'] = kiLabelNeighborList
data['k_i'] = k_iList
data['generalDensity'] = generalDensitiesList
data['inverseDensity'] = inverseDensitiesList
data['dataDistributionFactor'] = [dataDistributionFactor.get(tuple(sample), 0) for sample in X.values]

# 保留四位小数
data = data.round({'k_i': 4,
                   'generalDensity': 4,
                   'inverseDensity': 4,
                   'dataDistributionFactor': 4})

# 导出为 CSV 文件
data.to_csv('enhanced_haberman.csv', index=False)
