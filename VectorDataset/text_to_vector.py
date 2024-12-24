import os
import json
import torch
from transformers import AutoTokenizer, AutoModel

# 检查是否有GPU可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载模型和分词器，并将它们移动到GPU
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-base-zh-v1.5")
model = AutoModel.from_pretrained("BAAI/bge-base-zh-v1.5")
model.to(device)

# 定义文本转向量的函数
def text_to_vector(text):
    # 使用分词器将文本转换为tokens，并将其移动到GPU
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    # 推理（获取文本向量）
    with torch.no_grad():
        # 将tokens传递给GPU上的模型进行推理
        outputs = model(**tokens)
    # 获取最后一层的CLS token作为整个文本的向量表示
    text_vector = outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
    # 将向量转换为FloatVector格式
    text_vector_float = text_vector.tolist()

    return text_vector_float

# 定义处理和保存文件的函数
def process_and_save_files(input_dir, output_dir):
    # 获取data文件夹中的所有json文件
    input_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]

    for input_file in input_files:
        input_path = os.path.join(input_dir, input_file)

        # 读取文件内容
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 对每个条目进行处理
        for row in data["rows"]:
            content = row["content"]
            embedding = text_to_vector(content)
            row["embedding"] = embedding

        # 创建输出文件夹（如果不存在）
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 定义输出文件路径
        output_file = os.path.join(output_dir, input_file)

        # 保存处理后的数据到result文件夹
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

# 设置输入和输出文件夹路径
input_directory = "./data_json"
output_directory = "./target_json/"

# 处理文件并保存结果
process_and_save_files(input_directory, output_directory)
