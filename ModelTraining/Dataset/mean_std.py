import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像到224x224
    transforms.ToTensor()
])

# 定义数据集路径和加载方式
data_path = './augmented_data/Cassava/train'
dataset = datasets.ImageFolder(root=data_path, transform=transform)

dataloader = DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)

# 初始化变量
mean = torch.zeros(3)
std = torch.zeros(3)
total_images = 0

# 遍历数据集
for images, _ in dataloader:
    # 计算每个通道的均值与标准差
    batch_size = images.size(0)
    mean += images.mean([0, 2, 3]) * batch_size  # 按通道计算均值
    std += images.std([0, 2, 3]) * batch_size   # 按通道计算标准差
    total_images += batch_size

# 归一化
mean /= total_images
std /= total_images

print(f"Mean: {mean * 255}")
print(f"Std: {std * 255}")
