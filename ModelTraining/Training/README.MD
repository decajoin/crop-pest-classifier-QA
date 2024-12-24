# 模型训练

如果需要进行模型训练，将本目录下的几个模型配置文件文件夹导入到 `MMPretrain` 框架的主目录下

执行命令即可开始训练：

```bash
python ./tools/train.py ./efficientnetv2-l_8xb32_in21k_Cashew/efficientnetv2-l_8xb32_in21k_Cashew.py（刚才存放的模型配置文件的文件位置）
```

如果需要修改模型相关参数直接在对应配置文件中按需修改即可
