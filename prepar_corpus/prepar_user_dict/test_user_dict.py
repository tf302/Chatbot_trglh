"""
测试用户词典
"""

import jieba
import config
jieba.load_userdict(config.user_dict_path)
def test_user_dict():
    sentence ="人工智能+python和c++那个难"
    ret=jieba.lcut(sentence)
    print(ret)