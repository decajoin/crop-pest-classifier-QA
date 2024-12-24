from django.db import models

# 农作物表
class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 农作物名称
    description = models.TextField()                      # 农作物描述
    image_path = models.CharField(                       # 存储static目录下的相对路径
        max_length=255,
        help_text='图片在static目录下的相对路径，例如: static/images/crops/玉米.jpg'
    )

    def __str__(self):
        return self.name


# 病虫害表
class PestDisease(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='pest_diseases')
    type = models.CharField(max_length=100)               # 病虫害类型
    description = models.TextField()                      # 病虫害描述
    image_path = models.CharField(                       # 存储static目录下的相对路径
        max_length=255,
        help_text='图片在static目录下的相对路径，例如: images/pests/病虫害.jpg'
    )

    def __str__(self):
        return f"{self.type} ({self.crop.name})"