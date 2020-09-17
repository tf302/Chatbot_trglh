"""
测试分类相关的api
"""
from classify.build_model import build_classify_model,get_classify_model
from classify.classify import Classify

if __name__ == '__main__':
    # build_classify_model()
    # model=get_classify_model()
    # text=[
    #     "你好",
    #     "今天 天气 非常 好",
    #     "计算机 软件 有 哪些 特点"
    # ]
    # ret=model.predict("今天 天气 非常 好")
    # print(ret)
    get_model=Classify()
    a="你好"
    result=get_model.predict(a)
    print(result)