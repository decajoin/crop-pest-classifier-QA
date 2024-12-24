import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from index.models import Crop, PestDisease

# 创建农作物
crop1 = Crop.objects.create(
    name="玉米",
    description="玉米是一种常见的粮食作物",
    image_path="images/crops/玉米.jpg"
)
crop2 = Crop.objects.create(
    name="番茄",
    description="番茄是一种营养丰富的蔬菜",
    image_path="images/crops/番茄.jpg"
)
crop3 = Crop.objects.create(
    name="木薯",
    description="木薯是一种重要的根茎类作物",
    image_path="images/crops/木薯.jpg"
)
crop4 = Crop.objects.create(
    name="腰果",
    description="腰果是一种营养丰富的坚果",
    image_path="images/crops/腰果.jpg"
)

# 添加病虫害
PestDisease.objects.create(
    crop=crop1,
    type="秋粘虫",
    description="秋粘虫可大量啃食禾本科如水稻、甘蔗和玉米之类细粒禾榖及菊科、十字花科等多种农作物，造成严重的经济损失",
    image_path="images/pests/玉米_秋粘虫.jpg"
)

PestDisease.objects.create(
    crop=crop1,
    type="蝗虫",
    description="蝗虫会大量啃食玉米叶片，导致叶片出现孔洞、残缺甚至完全丧失。这不仅影响了玉米的光合作用，还降低了叶片对养分的吸收能力",
    image_path="images/pests/玉米_蝗虫.jpg"
)
PestDisease.objects.create(
    crop=crop1,
    type="叶枯病",
    description="叶片出现水渍状小圆斑点，逐渐扩展成椭圆形和沿叶脉方向的长条形病斑。病斑边缘淡红褐色，严重时整株叶片病斑满布，呈撕裂状干枯坏死",
    image_path="images/pests/玉米_叶枯病.jpg"
)
PestDisease.objects.create(
    crop=crop1,
    type="叶斑病",
    description="叶斑病会在玉米叶片上形成圆形或不规则的斑点，斑点通常呈现褐色、黑色或灰色，严重时斑点会扩大并连成一片，导致叶片大面积枯死",
    image_path="images/pests/玉米_叶斑病.jpg"
)
PestDisease.objects.create(
    crop=crop1,
    type="玉米条斑病毒",
    description="一种由昆虫介导传播的病毒，主要影响玉米，导致叶片上出现褪绿条纹，严重时会导致叶片枯死。它属于环状病毒科",
    image_path="images/pests/玉米_玉米条斑病毒.jpg"
)

PestDisease.objects.create(
    crop=crop2,
    type="卷叶病",
    description="番茄叶片卷曲会导致叶片表面积减小，进而降低光合作用的效率，影响植物的生长和果实的养分积累，植株生长缓慢",
    image_path="images/pests/番茄_卷叶病.jpg"
)
PestDisease.objects.create(
    crop=crop2,
    type="叶枯病",
    description="叶片出现水渍状小圆斑点，逐渐扩展成椭圆形和沿叶脉方向的长条形病斑。病斑边缘淡红褐色，严重时整株叶片病斑满布，呈撕裂状干枯坏死",
    image_path="images/pests/番茄_叶枯病.jpg"
)
PestDisease.objects.create(
    crop=crop2,
    type="叶斑病",
    description="叶斑病会在番茄叶片上形成圆形或不规则的斑点，斑点通常呈现褐色、黑色或灰色，严重时斑点会扩大并连成一片，导致叶片大面积枯死",
    image_path="images/pests/番茄_叶斑病.jpg"
)
PestDisease.objects.create(
    crop=crop2,
    type="黄萎病",
    description="叶片边缘开始出现黄色斑点，逐渐扩展到整个叶片，导致叶片变黄并最终枯死。患病植株生长缓慢，叶片可能保持绿色一段时间后突然脱落",
    image_path="images/pests/番茄_黄萎病.jpg"
)

PestDisease.objects.create(
    crop=crop3,
    type="细菌性枯萎病",
    description="细菌性枯萎病感染木薯后，患病木薯的叶片会出现失绿、枯萎和坏死等症状。叶片可能从边缘开始变黄，逐渐扩展到整个叶片，最终干枯脱落",
    image_path="images/pests/木薯_细菌性枯萎病.jpg"
)
PestDisease.objects.create(
    crop=crop3,
    type="褐斑病",
    description="褐斑病在木薯叶片上形成褐色或黑色的病斑，这些病斑通常是圆形或椭圆形，大小不一。严重时，病斑可能会扩大并合并，导致叶片大面积枯死",
    image_path="images/pests/木薯_褐斑病.jpg"
)
PestDisease.objects.create(
    crop=crop3,
    type="木薯绿螨",
    description="木薯绿螨以木薯叶片的汁液为食，它们在叶片上刺吸，造成叶片出现斑点、失绿和变形。受害叶片通常会变得苍白，表面出现许多小孔",
    image_path="images/pests/木薯_木薯绿螨.jpg"
)
PestDisease.objects.create(
    crop=crop3,
    type="木薯花叶病毒",
    description="感染木薯花叶病毒的木薯植株会出现典型的花叶症状，即叶片上出现不规则的黄色或白色斑点，这些斑点可能会连成大片，导致叶片颜色不均匀",
    image_path="images/pests/木薯_木薯花叶病毒.jpg"
)

PestDisease.objects.create(
    crop=crop4,
    type="炭疽病",
    description="炭疽病在腰果叶片上表现为不规则形状的黑色或棕色斑点，这些斑点随着病情的发展可能会扩大并连成片，导致叶片枯萎和脱落",
    image_path="images/pests/腰果_炭疽病.jpg"
)
PestDisease.objects.create(
    crop=crop4,
    type="流胶病",
    description="树干或枝条上形成小黑点，随后这些黑点扩大并渗出粘稠的树脂状物质，即所谓的“流胶”。这种流胶会导致树皮裂开，枝条和树干内部组织坏死",
    image_path="images/pests/腰果_流胶病.jpg"
)
PestDisease.objects.create(
    crop=crop4,
    type="潜叶虫",
    description="潜叶虫的幼虫在腰果叶片内部取食，形成弯曲的潜道，这些潜道破坏了叶片的叶绿体和细胞结构，导致叶片光合作用能力下降",
    image_path="images/pests/腰果_潜叶虫.jpg"
)
PestDisease.objects.create(
    crop=crop4,
    type="红锈病",
    description="红锈病在腰果叶片上表现为橙红色或黄色的斑点，随后这些斑点会扩大并合并成较大的斑块，严重时会导致叶片变黄、枯萎并最终脱落",
    image_path="images/pests/腰果_红锈病.jpg"
)