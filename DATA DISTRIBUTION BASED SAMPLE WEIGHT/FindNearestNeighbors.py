import pandas as pd
from scipy.spatial import distance


def FindNearestNeighbors(X, sample, k):
    """
    :param X: 数据集自变量
    :param sample: 查找近邻的样本 X_i
    :param k: 近邻个数
    :return: 最近邻的索引 indices 和最近邻的距离 distValues
    """
    distances = []

    # 遍历数据集中的每个样本，计算与样本的距离
    for idx, x in enumerate(X):
        # 跳过样本与其本身的距离
        # if tuple(x) == tuple(sample):
        #     continue
        dist = distance.euclidean(x, sample)  # 计算欧式距离
        distances.append((idx, dist))

    # 按距离排序，选择前 k 个最近邻
    distances.sort(key=lambda x: x[1])  # 按距离从小到大排序
    nearestNeighbors = distances[1:k + 1]

    indices = [nn[0] for nn in nearestNeighbors]  # 最近邻的索引
    distValues = [nn[1] for nn in nearestNeighbors]  # 最近邻的距离

    return indices, distValues
