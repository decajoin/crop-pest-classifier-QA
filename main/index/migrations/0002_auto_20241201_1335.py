from django.db import migrations

def create_crops_and_pests(apps, schema_editor):
    Crop = apps.get_model('index', 'Crop')
    PestDisease = apps.get_model('index', 'PestDisease')

    # 创建农作物
    crop1 = Crop.objects.create(
        name="玉米",
        description="一种重要的粮食作物，广泛种植。",
        image_path="images/crops/玉米.jpg"
    )

    # 添加病虫害
    PestDisease.objects.create(
        crop=crop1,
        type="秋粘虫",
        description="秋粘虫可大量啃食禾本科如水稻、甘蔗和玉米之类细粒禾榖及菊科、十字花科等多种农作物，造成严重的经济损失。",
        image_path="images/pests/玉米_秋粘虫.jpg"
    )

    PestDisease.objects.create(
        crop=crop1,
        type="蝗虫",
        description="蝗虫会大量啃食玉米叶片，导致叶片出现孔洞、残缺甚至完全丧失。这不仅影响了玉米的光合作用，还降低了叶片对养分的吸收能力‌，导致产量大幅度减少。",
        image_path="images/pests/玉米_蝗虫.jpg"
    )

class Migration(migrations.Migration):
    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_crops_and_pests),
    ]
