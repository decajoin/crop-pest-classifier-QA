import openai
import yaml


def kimi_llm(question, config_path):
    # 加载配置文件
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)

    api_key = config['kimi']['api_key']
    base_url = config['kimi']['base_url']
    model_name = config['kimi']['model_name']
    temperature = config['kimi']['temperature']

    # 设置API密钥和基础URL
    openai.api_key = api_key
    openai.api_base = base_url

    # 发起请求获取流式响应
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "你是一个智能助手，请总结知识库返回的内容来回答问题，请列举知识库中的数据详细回答，回答时一定一定要标记处内容来源（你可以在内容来源处标记上标比如内容1[1]，内容2[2]，最后在结尾给出[1]，[2]的具体来源，注意相同的来源标号保持一致）。当所有知识库内容都与问题无关时，你的回答必须包括“知识库中未找到您要的答案！”这句话。回答需要考虑聊天历史。",
            },
            {"role": "user", "content": question},
        ],
        temperature=temperature,
        stream=True,
    )

    # 生成每一块响应
    def generate_chunks(response):
        for chunk in response:
            content = chunk.choices[0].delta.get('content', None)
            if content:
                yield content

    return generate_chunks(response)
