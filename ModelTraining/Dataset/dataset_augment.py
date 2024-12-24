import os
import random
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, UnidentifiedImageError


def random_rotate(image):
    """随机旋转图像"""
    angle = random.randint(-45, 45)  # 随机旋转角度
    return image.rotate(angle)


def random_scale(image, target_size=(400, 400)):
    """随机缩放图像并调整回原尺寸"""
    scale = random.uniform(0.8, 1.2)  # 随机缩放比例
    width, height = image.size
    new_width, new_height = int(width * scale), int(height * scale)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    # 裁剪中心区域
    left = max((new_width - target_size[0]) // 2, 0)
    top = max((new_height - target_size[1]) // 2, 0)
    right = left + target_size[0]
    bottom = top + target_size[1]
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image.resize(target_size, Image.Resampling.LANCZOS)


def add_random_noise(image):
    """向图像添加随机噪声"""
    np_image = np.array(image)
    noise = np.random.normal(0, 25, np_image.shape)  # 生成高斯噪声
    noisy_image = np_image + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)  # 保证像素值在有效范围内
    return Image.fromarray(noisy_image)


def random_brightness(image):
    """随机调整图像亮度"""
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(0.5, 1.5)  # 随机亮度调整因子
    return enhancer.enhance(factor)


def enhance_image(image_path, output_dir , target_size=(400, 400)):
    """增强图像并保存"""
    try:
        image = Image.open(image_path).convert("RGB")
    except (UnidentifiedImageError, OSError) as e:
        print(f"Skipping damaged image: {image_path} ({e})")
        return  # 跳过无法识别的损坏图片

    base_name = os.path.basename(image_path).split('.')[0]
    augmented_image = image.copy()
    # 随机应用增强
    augmented_image_with_rotate = random_rotate(augmented_image)
    augmented_image_with_scale = random_scale(augmented_image, target_size)

    # 随机噪声
    augmented_image_with_noise = add_random_noise(augmented_image)

    # 随机亮度调整
    augmented_image_with_brightness = random_brightness(augmented_image)

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 保存原图
    image.save(os.path.join(output_dir, f"{base_name}.jpg"))
    # 保存增强图像
    augmented_image_with_rotate.save(os.path.join(output_dir, f"{base_name}_aug1_rotate.jpg"))
    augmented_image_with_scale.save(os.path.join(output_dir, f"{base_name}_aug2_scale.jpg"))
    augmented_image_with_noise.save(os.path.join(output_dir, f"{base_name}_aug3_noise.jpg"))
    augmented_image_with_brightness.save(os.path.join(output_dir, f"{base_name}_aug4_brightness.jpg"))


def augment_dataset(data_dir, output_dir, target_size=(400, 400)):
    """增强训练集数据"""
    train_dir = os.path.join(data_dir, "train")
    output_train_dir = os.path.join(output_dir, "train")
    for category in os.listdir(train_dir):
        category_path = os.path.join(train_dir, category)
        output_category_path = os.path.join(output_train_dir, category)
        if os.path.isdir(category_path):
            print(f"Processing category: {category}")
            for image_name in os.listdir(category_path):
                image_path = os.path.join(category_path, image_name)
                if image_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                    enhance_image(image_path, output_category_path, target_size=target_size)


# 原始数据目录
data_dir = "./data/Cassava"
# 目标目录
output_dir = "./augmented_data/Cassava"

# 开始增强
augment_dataset(data_dir, output_dir)
