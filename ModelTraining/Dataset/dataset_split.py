import os
import shutil
import random

# 设置随机种子确保可复现
random.seed(42)

# 原始数据目录
data_dir = "./Tomato"
# 目标目录
output_dir = "./data/Tomato"

# 划分比例
train_ratio = 0.75
val_ratio = 0.15
test_ratio = 0.15

# 创建输出目录结构
for split in ["train", "val", "test"]:
    for class_name in os.listdir(data_dir):
        os.makedirs(os.path.join(output_dir, split, class_name), exist_ok=True)

# 遍历类别文件夹
for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if not os.path.isdir(class_dir):
        continue

    # 获取当前类别下的所有文件
    files = os.listdir(class_dir)
    random.shuffle(files)

    # 计算划分索引
    train_end = int(len(files) * train_ratio)
    val_end = train_end + int(len(files) * val_ratio)

    # 划分数据
    train_files = files[:train_end]
    val_files = files[train_end:val_end]
    test_files = files[val_end:]

    # 复制文件到目标目录
    for split, split_files in zip(["train", "val", "test"], [train_files, val_files, test_files]):
        for file_name in split_files:
            src_path = os.path.join(class_dir, file_name)
            dst_path = os.path.join(output_dir, split, class_name, file_name)
            shutil.copy(src_path, dst_path)

print("数据集划分完成！")
