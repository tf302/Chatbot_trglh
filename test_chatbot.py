# -*- coding: utf-8 -*-
"""
测试chatbot相关的api
"""

from chatbot.word_senquence import Word_sequence
import config
import pickle
from chatbot.dataset import dataloader
import torch
from chatbot.train import train
from chatbot.eval import eval
from chatbot.chatbot import Chatbot
def save_ws():
    ws = Word_sequence()
    for line in open(config.chatbot_input_path, "r", encoding="utf-8").readlines():
        ws.fit(line.strip().split())
    ws.build_vocab()
    print(len(ws))
    pickle.dump(ws, open(config.chatbot_ws_by_word_input_path, "wb"))

    ws = Word_sequence()
    for line in open(config.chatbot_target_path, "r", encoding="utf-8").readlines():
        ws.fit(line.strip().split())
    ws.build_vocab()
    print(len(ws))
    pickle.dump(ws, open(config.chatbot_ws_by_word_target_path, "wb"))
def train_seq2seq():
    for i in range(10):
        train(i)
if __name__ == '__main__':
    # save_ws()
    # for idx,(input,target,input_length,target_length) in enumerate(dataloader):
    #     print(input)
    #     print(target)
    #     print(input_length)
    #     print(target_length)
    #     break
   # train_seq2seq()
    chatbot=Chatbot()
    while True:
      print(chatbot.predict(input("请输入：")))