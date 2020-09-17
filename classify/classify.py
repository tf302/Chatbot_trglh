# -*- coding: utf-8 -*-
# 意图识别模型的封装


import config
import fasttext
class Classify():
    def __init__(self):

        #加载训练好的模型
        self.model=fasttext.load_model(config.classify_model_path)
    def predict(self,sentence_cuted):
        """
        :param sentence_cuted: 分词之后的句子
        :return:
        """
        # 预测输入数据的结果，准确率
        # return (label,acc)
        result=self.model.predict(sentence_cuted)
        for label,acc in zip(*result):
            #计算准确率
            if label=="__label__chat":
                label="__label__QA"
                acc=1-acc
        # label,acc = self.model.predict(sentence_cuted)
        # if label == "__label__chat":
        #     label = "__label__QA"
        #     acc=1-acc
        #判断准确率
        if acc>0.95:
            return ("QA",acc)
        else:
            return ("chat",1-acc)
