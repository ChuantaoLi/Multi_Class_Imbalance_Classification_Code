from scipy.spatial import distance


def GeneralDensity(X, kiLabelNeighbor, k_i):
    """
    计算每个样本的一般密度
    :param X: 数据集自变量
    :param kiLabelNeighbor: 存储每个样本的相同类别邻居的索引
    :param k_i: 存储每个样本的相同类别邻居个数
    :return: 每个样本的一般密度字典
    """
    densities = {}  # 存储每个样本的密度
    totalDensity = 0  # 用于计算归一化因子 T

    for idx, sample in enumerate(X):
        sampleTuple = tuple(sample)  # 将当前样本转化为元组形式，作为字典键
        k = k_i.get(sampleTuple, [0])[0]  # 获取当前样本的 k_i，如果没有则为 0
        if k == 0:
            densities[sampleTuple] = 0  # 如果 k_i 为 0，密度为 0
        else:
            sumInverseDistances = 0
            neighbors = kiLabelNeighbor.get(sampleTuple, [])  # 获取当前样本的相同类别邻居
            for neighbor in neighbors:
                # 计算欧式距离
                dist = distance.euclidean(sample, X[neighbor])
                sumInverseDistances += 1 / dist
            # 计算当前样本的一般密度
            rho = (1 / k) * sumInverseDistances
            densities[sampleTuple] = rho
            totalDensity += rho  # 累加密度值用于归一化，第一个样本的一般密度不是0.8828，因为只有把全部的分子计算完才知道T是多少

    # 归一化因子 T
    n = len(X)
    print(f"totalDensity:{totalDensity}")
    normalizationFactor = totalDensity / n
    print(f"n:{n}")
    print(f"normalizationFactor:{normalizationFactor}")

    # 对每个样本进行归一化
    for sample in densities:
        densities[sample] /= normalizationFactor  # 归一化是为了应对不同数据集的数据尺度，不然有的数据集的一般密度在1左右，有的数据集的一般密度在100左右

    return densities
