import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse
from .mmpretrain.apis.image_classification import ImageClassificationInferencer
from main import settings

# 配置字典，保存每种农作物的模型路径和检查点路径
MODEL_CONFIGS = {
    "maize": {
        "config": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Maize/efficientnetv2-l_8xb32_in21k_Maize.py",
        "checkpoint": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Maize/epoch_21.pth"
    },
    "tomato": {
        "config": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Tomato/efficientnetv2-l_8xb32_in21k_Tomato.py",
        "checkpoint": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Tomato/epoch_38.pth"
    },
    "cassava": {
        "config": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Cassava/efficientnetv2-l_8xb32_in21k_Cassava.py",
        "checkpoint": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Cassava/epoch_20.pth"
    },
    "cashew": {
        "config": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Cashew/efficientnetv2-l_8xb32_in21k_Cashew.py",
        "checkpoint": "./classifier/mmpretrain/efficientnetv2/efficientnetv2-l_8xb32_in21k_Cashew/epoch_30.pth"
    }
}

# 标签映射字典
LABEL_MAP = {
    "fall armyworm": "秋粘虫",
    "grasshoper": "蝗虫",
    "leaf beetle": "叶甲虫",
    "leaf blight": "叶枯病",
    "leaf spot": "叶斑病",
    "streak virus": "玉米条斑病毒",
    "healthy": "健康",
    "leaf curl": "卷叶病",
    "septoria leaf spot": "叶斑病",
    "verticillium wilt": "黄萎病",
    "bacterial blight": "细菌性枯萎病",
    "brown spot": "褐斑病",
    "green mite": "木薯绿螨",
    "mosaic": "木薯花叶病毒",
    "anthracnose": "炭疽病",
    "gummosis": "流胶病",
    "leaf miner": "潜叶虫",
    "red rust": "红锈病"
}


# 分类功能
def classify(request):
    if request.method == "POST" and request.FILES.get('image'):

        # 获取上传的图片文件
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # 获取前端传过来的农作物类型
        crop_type = request.POST.get('crop_type', 'maize')  # 默认值为maize（玉米）

        # 获取对应农作物类型的模型配置
        model_config = MODEL_CONFIGS.get(crop_type)

        if model_config:
            config = model_config["config"]
            checkpoint = model_config["checkpoint"]

            # 初始化分类推理器
            inferencer = ImageClassificationInferencer(model=config, pretrained=checkpoint, device='cuda')

            # 进行分类
            result = inferencer(file_path)[0]
            print(result)
            print('\n' + result['pred_class'] + " : " + str(result['pred_score']))

            # 获取英文标签并映射到中文标签
            pred_class = result['pred_class']
            chinese_class = LABEL_MAP.get(pred_class, pred_class)  # 默认返回英文标签，如果找不到映射

            # 返回分类结果（使用中文标签）
            if result['pred_score'] <= 0.6:
                result = {"class": chinese_class, "score": result['pred_score'],
                          "warnning": "分类结果置信度偏低，模型可能会犯错。请核查重要信息"}
            else:
                result = {"class": chinese_class, "score": result['pred_score'], "warnning": ""}
            return JsonResponse(result)
        else:
            return JsonResponse({"error": "农作物类型未找到"}, status=400)

    return render(request, 'classify.html')
