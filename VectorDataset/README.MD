# 向量知识库数据与数据处理

## 向量知识库数据

1. `/data_json` 文件夹中的文件是网络上收集到的各虫害的相关防治措施

关于 `json` 文件的生成可以直接通过大模型得到，可以把网页原文和对应来源给大模型，然后提示词可以参考下面。

> 后面我将给出一些文章要求如下： 
> 文章按照下面的格式划分（下面某个找不到就直接跳过，如果是英文就先翻译为中文） 1．病虫害的描述（外观、生活习性等）。 
> 2．病虫害的为害特点。
> 3．防治措施（物理方法、生物防治、化学药剂等）。 
> 4．注意事项和特殊建议。（如果有） 
>
> 然后将每个部分按 
> 字段名    描述     
> id    段落唯一标识符     
> title    段落的标题/病虫害名称     
> content    段落的主要的内容     
> tags    相关标签（供检索用）     
> source    数据来源     
> embedding    段落内容的向量表示 （embedding置空就可以！） 
> 然后将内容转为JSON格式，JSON格式模版为 {"rows":[{"embedding":[],"title":"title1","content":"content1","tags":"tags1","source":"source1"},{"embedding":[],"title":"title2","content":"content2","tags":"tags2","source":"source2"}]} 输出JSON文件

![image-20241224164658506](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20241224164658506.png)

直接复制大模型返回的 `json` 即可



2. `/target_json` 文件夹中的文件是将`/data_json` 文件夹中的文件进行向量化后的数据（补充了 **embedding** 部分的空缺）

## 数据处理

`text_to_vector.py` 将 `json` 文件中的 `content` 字段进行向量化并补充完整 `embedding` 字段

`json_merge.py` 将`/target_json` 文件夹中的文件进行整合，得到一个符合 `Zilliz` 要求的导入格式

