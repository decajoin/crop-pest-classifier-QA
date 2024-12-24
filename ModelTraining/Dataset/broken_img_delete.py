import os
from PIL import Image
from PIL import UnidentifiedImageError
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO)

def delete_invalid_images_in_folder(folder_path):
    """递归删除文件夹中所有读取失败的图片，并在控制台显示删除的图片"""
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):  # 只处理图像文件
                try:
                    # 尝试打开图片文件
                    Image.open(file_path)
                except (UnidentifiedImageError, OSError) as e:
                    # 如果读取图片失败，则删除该图片
                    os.remove(file_path)
                    logging.info(f"Deleted invalid image: {file_path}")

# 指定要清理的文件夹路径
folder_path = "./augmented_data/Cassava"  # 可以根据需要修改

# 开始删除无效图片
delete_invalid_images_in_folder(folder_path)
