import numpy as np

def ComputeDataDistributionFactor(X, y, inverseDensities, imbalanceRatios):
    """
    计算数据分布因子（data distribution factor）
    :param X: 数据集自变量
    :param y: 数据集标签
    :param inverseDensities: 每个样本的逆密度
    :param imbalanceRatios: 每个类别的不平衡比
    :return: dataDistributionFactor 字典
    """
    dataDistributionFactor = {}

    for idx, sample in enumerate(X):
        label = y[idx]
        inverseDensity = inverseDensities.get(tuple(sample), 0)
        imbalanceRatio = imbalanceRatios.get(label, 1)

        # 计算 data distribution factor
        alpha = np.exp(-imbalanceRatio * inverseDensity)
        dataDistributionFactor[tuple(sample)] = alpha

    return dataDistributionFactor
