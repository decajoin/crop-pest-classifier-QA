# 数据集与数据预处理

## 数据集

数据集来源 [开源作物病虫害检测数据集](https://data.mendeley.com/datasets/bwh3zbpkpv/1)

![image-20241224155804502](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224155804502.png)

### Maize - 玉米

fall armyworm - [秋粘虫](https://zh.wikipedia.org/wiki/草地貪夜蛾)

grasshopper - [蝗虫](https://zh.wikipedia.org/zh-sg/蝗蟲)

leaf beetle - 叶甲虫

leaf blight -  [叶枯病](https://baike.baidu.com/item/叶枯病/7514521)

leaf spot - [叶斑病](https://baike.baidu.com/item/叶斑病/4177053)

streak virus - 玉米条斑病毒

healthy - 健康

### Tomato - 番茄

leaf curl - 卷叶病

leaf blight -  [叶枯病](https://baike.baidu.com/item/叶枯病/7514521)

septoria leaf spot - [叶斑病](https://baike.baidu.com/item/叶斑病/4177053)

verticillium wilt - 黄萎病

healthy - 健康

### Cassava - 木薯

bacterial blight - 细菌性枯萎病

brown spot - 褐斑病

green mite - 木薯绿螨

mosaic - 木薯花叶病毒

healthy - 健康

### Cashew - 腰果

anthracnose -  炭疽病  

gummosis - 流胶病

leaf miner - 潜叶虫

red rust - 红锈病

healthy - 健康

## 数据预处理

对开源数据集中的原始图像进行数据预处理

`broken_img_delete.py` 遍历数据集将其中中损坏的图片进行删除

`dataset_split.py` 对数据集进行划分

`dataset_augment.py` 对原始数据进行数据增强

`mean_std.py` 计算训练集的 **mean_std** ，用于训练代码的初始参数设置

