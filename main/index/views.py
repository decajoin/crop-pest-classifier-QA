from django.shortcuts import render
from .models import Crop  # 导入 Crop 模型

# 首页展示所有农作物
def index(request):
    crops = Crop.objects.all()  # 从数据库中获取所有农作物
    return render(request, 'index.html', {"crops": crops})



# 农作物具体信息
def crops_info(request, crop_name):
    try:
        crop = Crop.objects.get(name=crop_name)  # 根据农作物名称获取对应的农作物对象
    except Crop.DoesNotExist:
        crop = None  # 如果没有找到该农作物，返回 None 或处理错误
    return render(request, 'crops_info.html', {"crop": crop})
