from http import HTTPStatus
import dashscope
import yaml


def qwen_llm(question, config_path):
    # 加载配置文件
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)

    api_key = config['qwen']['api_key']
    model_name = config['qwen']['model_name']
    temperature = config['qwen']['temperature']

    dashscope.api_key = api_key

    messages = [{'role': 'system', 'content': '你是一个智能助手，请总结知识库返回的内容来回答问题，请列举知识库中的数据详细回答，回答时一定一定要标记处内容来源（你可以在内容来源处标记上标比如内容1[1]，内容2[2]，最后在结尾给出[1]，[2]的具体来源，注意相同的来源标号保持一致）。当所有知识库内容都与问题无关时，你的回答必须包括“知识库中未找到您要的答案！”这句话。回答需要考虑聊天历史。'},
                {'role': 'user', 'content': '%s' % question}]

    response  = dashscope.Generation.call(
        model=model_name,
        messages=messages,
        result_format='message',  # set the result to be "message" format.
        temperature=temperature,
        stream=True,
        incremental_output=True
    )

    def generate_chunks(response):
        for chunk in response:
            if chunk.status_code == HTTPStatus.OK:
                content = chunk.output.choices[0]['message']['content']
                if content is not None:
                    yield content
            else:
                print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                    response.request_id, response.status_code,
                    response.code, response.message
                ))

    return generate_chunks(response)
