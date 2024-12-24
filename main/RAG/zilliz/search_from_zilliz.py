import requests
import yaml
import torch
from transformers import AutoTokenizer, AutoModel


def search_from_zilliz(text, config_path):
    # 检查是否有GPU可用
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 加载模型和分词器，并将它们移动到GPU
    tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-base-zh-v1.5")
    model = AutoModel.from_pretrained("BAAI/bge-base-zh-v1.5")
    model.to(device)

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

    # 加载配置文件
    config_path = config_path
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)

    # 获取数据
    headers = config['headers']
    url = config['urls']['data_search']
    limit = config['ziliz']['limit']

    # 构建请求payload
    payload = (
                  "{\"collectionName\":\"crops_pests\",\"data\": [%s],\"limit\": %s,\"outputFields\":[\"title\", \"content\", \"tags\", \"source\"]}") % (
                  text_vector_float, limit)

    # 发送POST请求获取数据
    response = requests.post(url, data=payload, headers=headers)

    # 构建输出字符串
    output_string = ""
    output_string += "问题:" + text + "\n"
    output_string += "-" * 25 + "下面是在知识库中找到的可能有用的信息" + "-" * 25 + "\n"

    response_data = response.json()
    if 'data' not in response_data or len(response_data['data']) == 0:
        output_string += "知识库中未找到您要的答案！"
    else:
        for item in response_data['data']:
            output_string += "标题:" + str(item['title']) + "\n"
            output_string += "内容:" + str(item['content']) + "\n"
            output_string += "标签:" + str(item['tags']) + "\n"
            output_string += "内容来源:" + str(item['source']) + "\n"
            output_string += "向量相似度:" + str(item['distance']) + "\n"
            output_string += "-" * 50 + "\n"

    output_string += (
        "你是一个智能助手，请总结知识库返回的内容来回答问题，请列举知识库中的数据详细回答，回答时一定一定要标记处内容来源（你可以在内容来源处标记上标比如内容1[1]，内容2[2]，最后在结尾给出[1]，[2]的具体来源，注意相同的来源标号保持一致）。当所有知识库内容都与问题无关时，你的回答必须包括“知识库中未找到您要的答案！”这句话。回答需要考虑聊天历史。")

    return output_string
