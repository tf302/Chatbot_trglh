"""
分词
"""

import jieba
import config
import string
import jieba.posseg as psg
from lib.stopwords import stopwords
import logging
#关闭jieba log输出
jieba.setLogLevel(logging.INFO)
jieba.load_userdict(config.user_dict_path)
# 准备英文字符
letters = string.ascii_lowercase + "+"


def cut_sentence_by_word(sentence):
    """
    实现中英文分词
    :param sentence:句子
    :return:
    """
    temp = ""
    result = []
    # python 和c++那个难-->[python ,和, c++,那个,难]
    for word in sentence:
        if word.lower() in letters:
            temp += word
        else:
            if temp != "":
                result.append(temp.lower())
                temp = ""
            result.append(word)
    if temp != "":
        result.append(temp.lower())
    return result


def cut(sentence, by_word=False, use_stopwords=False, with_sg=False):
    """

    :param sentence: 句子
    :param by_word: 是否按照单个字分词
    :param use_stopwords: 是否使用停用词
    :param with_sg: 是否返回词性
    :return:
    """
    if by_word:
        result = cut_sentence_by_word(sentence)
    else:
        result = psg.lcut(sentence)
        result = [(i.word, i.flag) for i in result]
        if not with_sg:
            result = [i[0] for i in result]
    if use_stopwords:
        result = [i for i in result if i not in stopwords]

    return result


if __name__ == '__main__':
    print(cut_sentence_by_word("python和c++那个难?UI/UE"))
