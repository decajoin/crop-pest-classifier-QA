# 数据集与数据预处理

## 数据集

数据集来源 [开源作物病虫害检测数据集](https://data.mendeley.com/datasets/bwh3zbpkpv/1)

![image-20241224155804502](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224155804502.png)

## 数据预处理

对开源数据集中的原始图像进行数据预处理

`broken_img_delete.py` 遍历数据集将其中中损坏的图片进行删除

`dataset_split.py` 对数据集进行划分

`dataset_augment.py` 对原始数据进行数据增强

`mean_std.py` 计算训练集的 **mean_std** ，用于训练代码的初始参数设置

