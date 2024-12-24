import os
import json

# 定义合并文件的函数
def merge_json_files(input_dir, output_file):
    # 创建一个空的rows列表来存储所有的内容
    merged_rows = []

    # 获取target_data文件夹中的所有json文件
    input_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]

    # 遍历每个文件
    for input_file in input_files:
        input_path = os.path.join(input_dir, input_file)

        # 读取文件内容
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 将该文件的rows部分追加到merged_rows列表中
            merged_rows.extend(data.get("rows", []))

    # 将合并后的数据保存到一个新文件
    merged_data = {"rows": merged_rows}

    # 将合并后的结果写入output_file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(merged_data, outfile, ensure_ascii=False, indent=2)

# 设置输入文件夹路径和输出文件路径
input_directory = "./target_json"
output_file = "./merged_data.json"

# 调用合并函数
merge_json_files(input_directory, output_file)
