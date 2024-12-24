from django.http import StreamingHttpResponse
from django.shortcuts import render
from .zilliz.search_from_zilliz import search_from_zilliz
from .llm_api.kimi_llm import kimi_llm
from .llm_api.qwen_llm import qwen_llm
from .llm_api.zhipu_llm import zhipu_llm


# 用于流式处理LLM返回的响应
def RAG(request):
    if request.GET.get('question'):
        question = request.GET.get('question')
        llm_choice = request.GET.get('llm', 'zhipu_llm')  # 默认为 zhipu_llm
        config_path = './RAG/cfgs/config.yaml'  # 配置文件路径

        # 从 Zilliz 获取相关的知识库数据
        zilliz_output = search_from_zilliz(question, config_path)

        # 根据选择的LLM调用不同的处理函数
        if llm_choice == 'kimi_llm':
            llm_response = kimi_llm(zilliz_output, config_path)
        elif llm_choice == 'qwen_llm':
            llm_response = qwen_llm(zilliz_output, config_path)
        else:  # 默认使用 zhipu_llm
            llm_response = zhipu_llm(zilliz_output, config_path)

        # 创建一个流式响应
        response = StreamingHttpResponse(generate(llm_response), content_type='text/event-stream')

        # 设置缓存控制
        response['Cache-Control'] = 'no-cache'
        response['Content-Type'] = 'text/event-stream; charset=utf-8'

        return response
    else:
        return render(request, 'RAG.html')


# 生成流式响应的生成器
def generate(llm_response):
    # 逐块生成内容
    for chunk in llm_response:
        yield f"{chunk}"
