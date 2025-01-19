def CalculateSameClassNeighbors(withinClassNeighbor, y):
    """
    计算每个样本的相同类别邻居个数 k_i
    :param withinClassNeighbor: 字典，包含每个样本的5个最近邻的索引
    :param y: 样本的标签（类别）
    :return: 两个字典：kiLabelNeighbor 和 k_i
            kiLabelNeighbor: 存储每个样本的相同类别邻居的索引
            k_i: 存储每个样本的相同类别邻居个数
    """
    kiLabelNeighbor = {}  # 存储每个样本的相同类别邻居的索引
    k_i = {}  # 存储每个样本的相同类别邻居个数
    idx = 0  # 用于追踪当前样本的索引
    for samples, neighbors in withinClassNeighbor.items():
        # 获取当前样本的类别
        sampleLabel = y.iloc[idx]  # 当前样本的类别
        idx += 1
        k = 0

        kiLabelNeighbor.setdefault(samples, [])  # 如果 samples 不存在，初始化为 []
        k_i.setdefault(samples, [])  # 如果 samples 不存在，初始化为 []

        for neighbor in neighbors:
            # 获取第 i 个邻居样本的类别
            neighborLabel = y.iloc[neighbor]
            if neighborLabel == sampleLabel:
                k += 1
                kiLabelNeighbor[samples].append(neighbor)  # 将邻居添加到 kiLabelNeighbor

        k_i[samples].append(k)  # 将相同类别邻居个数 k 添加到 k_i

    return kiLabelNeighbor, k_i
