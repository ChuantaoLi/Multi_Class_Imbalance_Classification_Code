import numpy as np


def InverseGeneralDensity(X, y, generalDensities):
    """
    计算每个样本的逆密度
    :param X: 数据集自变量
    :param y: 数据集标签
    :param generalDensities: 每个样本的一般密度字典
    :return: 每个样本的逆密度字典
    """
    inverseDensities = {}  # 存储每个样本的逆密度

    # 遍历每个样本，计算逆密度
    for idx, sample in enumerate(X):
        sampleLabel = y.iloc[idx]  # 当前样本的标签
        sampleTuple = tuple(sample)  # 将样本转为元组形式，作为字典键

        # 获取当前样本的密度 rho(X_i, y_i)
        rho = generalDensities.get(sampleTuple, 0)

        # 计算该样本的 Z_i
        sumExpRho = 0
        count = 0
        for j, neighbor in enumerate(X):
            if y.iloc[j] == sampleLabel:  # 只考虑与当前样本同标签的样本
                neighborTuple = tuple(neighbor)
                neighborRho = generalDensities.get(neighborTuple, 0)
                sumExpRho += np.exp(-neighborRho)
                count += 1

        Z_i = sumExpRho / count if count > 0 else 1  # 防止除0错误

        # 计算逆密度 rho^-1(X_i, y_i)
        inverseRho = np.exp(-rho) / Z_i if Z_i != 0 else 0
        inverseDensities[sampleTuple] = inverseRho

    return inverseDensities
