# -*- coding: utf-8 -*-
"""
准备闲聊语料
"""
import string
from lib import cut
from tqdm import tqdm


def filter(pair):
    if pair[0][1] in list(string.ascii_lowercase):  # input只有一个字母
        return True
    elif pair[1][1].count("=")>=2 and len(pair[1][0].split())<4:#防止是标点符号= =
        return True
    elif "黄鸡" in pair[0][1] or "黄鸡" in pair[1][1] or "小通" in pair[0][1] or "小通" in pair[1][1]:
        return True
    elif len(pair[0][0].strip())==0 or len(pair[1][0].strip())==0:#过滤空行
        return True

def prepar_xiaohuangji(by_word=False):
    path = "/Users/apple/Desktop/聊天机器人/corpus/origin_corpus/xiaohuangji50w_nofenci.conv"
    if by_word:
        input_path = "/Users/apple/Desktop/聊天机器人/corpus/chatbot/input_by_word.txt"
        target_path = "/Users/apple/Desktop/聊天机器人/corpus/chatbot/target_by_word.txt"
    else: 
        input_path = "/Users/apple/Desktop/聊天机器人/corpus/chatbot/input.txt"
        target_path = "/Users/apple/Desktop/聊天机器人/corpus/chatbot/target.txt"
    f_input = open(input_path, "a", encoding="utf-8")
    f_target = open(target_path, "a", encoding="utf-8")
    one_qa_pair = []
    num=0
    for line in tqdm(open(path, "r", encoding="utf-8").readlines(), ascii=True, desc="处理小黄鸡语料"):
        if line.startswith("E"):
            continue
        else:
            line = line[1:].strip().lower()
            line_cuted = cut(line, by_word=by_word)
            line_cuted = " ".join(line) + "\n"
            if len(one_qa_pair) < 2:
                one_qa_pair.append([line_cuted,line])
            if len(one_qa_pair)==2:  # 写入
                # 判断句子是否需要：
                if filter(one_qa_pair):
                    one_qa_pair=[]
                    continue
                f_input.write(one_qa_pair[0][0])
                f_target.write(one_qa_pair[1][0])
                num+=1
                one_qa_pair = []

    f_input.close()
    f_target.close()
    return num
