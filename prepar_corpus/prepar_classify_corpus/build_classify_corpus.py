from tqdm import tqdm
from lib import cut
import config

xiaohuangji_path = "corpus/origin_corpus/xiaohuangji50w_nofenci.conv"
byhand_path = "corpus/origin_corpus/Q.txt"
keywords_panduan = "corpus/origin_corpus/dictionary_byhand.txt"


def keywords_in_line(line):
    # 判断line中是否存在不符合要求的词
    keywords_list = [i.strip() for i in open(keywords_panduan, "r", encoding="utf-8").readlines()]
    for word in line:
        if word in keywords_list:
            return True
        else:
            return False


def process_xiaohuangji(file):
    # TODO 句子长度为1，考虑删除
    num=0
    for line in tqdm(open(xiaohuangji_path, "r", encoding="utf-8").readlines(),desc="小黄鸡"):
        if line.startswith("E"):
            flag = 0
            continue
        elif line.startswith("M"):
            if flag == 0:
                line = line[1:].strip()
                if len(line)==1:
                    continue
                flag = 1
            else:
                continue

        line_cut = cut(line)
        if not keywords_in_line(line_cut):
            line_cut = " ".join(line_cut) + "\t" + "__label__chat"
            num+=1
            file.write(line_cut + "\n")
    return num


def process_byhand_data(file):
    num=0
    for line in tqdm(open(byhand_path, "r",encoding="utf-8").readlines(),desc="问答对"):
        line = line.strip()
        line_cut = cut(line)

        line_cut = " ".join(line_cut) + "\t" + "__label__QA"
        num+=1
        file.write(line_cut + "\n")
    return num


def process():
    f = open(config.classify_corpus_path, "a", encoding="utf-8")
    # 1、处理小黄鸡语料
    num_chat=process_xiaohuangji(f)
    # 2、处理手写的语料
    num_QA=process_byhand_data(f)
    #3、加上爬虫检索相似的句子
    f.close()
    print(num_chat,num_QA)
    # print(num_QA)

