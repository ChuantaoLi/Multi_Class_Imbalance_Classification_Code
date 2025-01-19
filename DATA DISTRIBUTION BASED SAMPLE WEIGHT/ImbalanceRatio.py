def ImbalanceRatio(X, y):
    labels = {}

    for row in range(len(X)):
        label = y[row]
        if label in labels:
            labels[label].append(X[row].tolist())  # 将样本转换为列表并添加到对应的类别
        else:
            labels[label] = [X[row].tolist()]  # 创建新的列表并添加样本（已转换为列表）

    # 计算最少数类别的样本数量
    minClassSampleCount = min(len(samples) for samples in labels.values())

    imbalanceRatios = {}
    # 计算并输出每个类别的样本数量和不平衡比
    for i in list(set(y)):
        sampleCount = len(labels[i])
        imbalanceRatio = sampleCount / minClassSampleCount
        imbalanceRatios[i] = imbalanceRatio
        print(f"Label {i} sample count: {sampleCount}, Imbalance Ratio: {imbalanceRatio:.4f}")

    return labels, imbalanceRatios
