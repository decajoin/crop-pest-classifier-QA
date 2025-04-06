# README

## 1. 环境配置

### 1.1. 安装 CUDA

首先需要根据自身硬件要求安装 CUDA

如果安装完成可以使用

```cmd
nvcc --version
```

进行查看本机的 CUDA 版本

![img](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/1732612233419-bc6e2ed8-8c98-48d1-b084-99176a5d5b41.png)

### 1.2. 安装 Pytorch

**第 1 步** 从[官网](https://docs.conda.io/en/latest/miniconda.html)下载并安装 Miniconda。

**第 2 步** 创建一个 conda 虚拟环境并激活它。

```bash
conda create --name torch python=3.10 -y
conda activate torch
```

**第 3 步** 按照[官方指南](https://pytorch.org/get-started/locally/)安装 PyTorch。例如：

本机的 **CUDA 版本是 11.7**，安装原则是 Pytorch 的 CUDA 版本需要小于本机的 CUDA 版本。

Pytorch 的历史版本 https://pytorch.org/get-started/previous-versions/

```bash
# CUDA 11.6
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
```

### 1.3. 安装 MMPretrain 框架

官方文档 https://mmpretrain.readthedocs.io/en/latest/get_started.html#id2

```bash
git clone https://github.com/open-mmlab/mmpretrain.git
cd mmpretrain
pip install -U openmim && mim install -e .
```

进行验证安装

```bash
python demo/image_demo.py demo/demo.JPEG resnet18_8xb32_in1k --device cpu
```

如果结果如下则说明上述环境配置成功

![image.png](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/1732616832450-8b9d7727-1f4d-45b2-a4a3-05ca3afef3cf.png)

如果验证安装时，提示 NumPy 版本不兼容问题，可以参考如下方法。

> NumPy 从 1.x 升级到 2.x 之后，可能会导致一些依赖于 NumPy 1.x 版本编译的模块不兼容，并在调用时崩溃，所以需要对其进行降级

```bash
pip install "numpy<2"
```

## 2. 安装项目依赖

进入项目文件夹（djangoProject），执行下面命令进行依赖安装

```bash
pip install -r requirements.txt
```

（PS. 依赖统计可能有缺失，如果运行项目时有其他依赖未安装，可以 `pip install XXX` 进行安装 ）

## 3. 项目配置

### 3.1. 检查数据库配置

打开 **main** 文件夹下的 `settings.py` 文件检查数据库配置，根据自己的数据库进行修改。

![image-20241224152714034](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224152714034.png)

### 3.2. 进行数据库迁移

执行数据库迁移命令，将所有的数据库表结构创建到数据库中。迁移命令会根据你项目中的 `models.py` 文件生成相应的数据库表。

执行命令：

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3.3. 导入分类模型

[下载模型文件](https://pan.baidu.com/s/1RFvgMkoV9UMjri_EXraSxw?pwd=hym9)

解压 `/Models.zip`，将其中所有文件夹导入到 `/main/classifier/mmpretrain/efficientnetv2`目录下

### 3.4. 运行 Django 项目

在本地环境中启动 Django 开发服务器来运行项目。默认情况下，Django 会在 `localhost:8000` 上启动一个开发服务器。

执行命令：

```bash
python manage.py runserver
```

这时你可以通过浏览器访问 `http://127.0.0.1:8000/` 查看项目是否成功运行。

## 4. 各 API Key 的配置

各 **API** 主要是在 **RAG 应用** 中使用到

**Zilliz 向量数据库**相关配置，参考 https://docs.zilliz.com/docs/quick-start

![image-20241224154532063](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224154532063.png)

如果要导入本项目的数据，可以直接在 **Zilliz 平台** 导入 `/VectorDataset/merged_data.json`

![image-20241224161325537](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224161325537.png)

**Kimi 大模型**相关配置，参考 https://platform.moonshot.cn/docs/guide/start-using-kimi-api

![image-20241224154729545](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224154729545.png)

**通义千问大模型**相关配置，参考 https://help.aliyun.com/zh/model-studio/developer-reference/use-qwen-by-calling-api

![image-20241224154837134](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224154837134.png)

**智谱清言大模型**相关配置，参考 https://bigmodel.cn/dev/api/normal-model/glm-4

![image-20241224154900308](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224154900308.png)

申请各平台 API 后修改 `/main/RAG/cfgs/config.yaml` 文件中对应的各部分，即可开始使用。

## 5. 目录结构说明

`/main` 文件夹存放 Django 的主要代码

`/ModelTraining` 文件夹存放图片分类模型训练相关代码和部分测试数据以供功能测试

`/VectorDataset` 文件夹存放 `RAG` 的向量知识库数据和相关处理代码

`/Models.zip` 此压缩文件存放的是图片分类训练的具体模型，模型文件太大无法上传，需要手动下载

## 6. 平台运行图示

![image-20241224203955285](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224203955285.png)

![image-20241224204006772](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224204006772.png)

![image-20241224204032964](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224204032964.png)

![image-20250406110249170](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20250406110249170.png)

![image-20241224204104420](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224204104420.png)

![image-20250406110135751](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20250406110135751.png)

