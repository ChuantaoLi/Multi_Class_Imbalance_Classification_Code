# Multi_Class_Imbalance_Classification_Code

## DATA DISTRIBUTION BASED SAMPLE WEIGHT

### 数据集
haberman.xlsx：二维二分类的数据集，需要去除重复值，代码中已包含该处理

balance.xlsx:多维度多分类的数据集

enhanced_haberman.csv:导出的带有几个不平衡度量指标的haberman数据集

distances.csv:第一个样本与各样本之间的欧式距离，测试用的

### 代码
main.py：主函数

ImbalanceRatio.py：计算不平衡比

FindNearestNeighbors.py：计算每个样本的5个最近邻的索引和距离

CalculateSameClassNeighbors.py：计算每个样本的类内近邻集合

GeneralDensity.py：计算每个样本的一般密度general density

InverseGeneralDensity.py：计算每个样本的逆密度

ComputeDataDistributionFactor.py：计算每个样本的数据分布因子

