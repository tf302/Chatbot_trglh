"""
配置文件
"""
import pickle

#############语料相关##############
user_dict_path = "corpus/user_dict/keywords.txt"
stopwords_path = "corpus/user_dict/stopwords.txt"
classify_corpus_path = "corpus/classify/classify.txt"

############分类相关的路径################
classify_model_path = "model/classify.model"

##########chatbot相关的路径#############
chatbot_input_path = "corpus/chatbot/input-30000"
chatbot_target_path = "corpus/chatbot/output-30000"
# ws
chatbot_ws_by_word_input_path = "model/chatbot/ws_by_word_input_path.pkl"
chatbot_ws_by_word_target_path = "model/chatbot/ws_by_word_target_path.pkl"

chatbot_ws_input = pickle.load(open(chatbot_ws_by_word_input_path, "rb"))
chatbot_ws_target = pickle.load(open(chatbot_ws_by_word_target_path, "rb"))

chatbot_batch_size = 128
chatbot_input_max_len = 20
chatbot_target_max_len = 20
chatbot_embedding_dim = 256
chatbot_encoder_num_layers = 1
chatbot_encoder_hidden_size = 128

chatbot_decoder_num_layer = 1
chatbot_decoder_hidden_size = 128

chatbot_teacher_forcing_ratio = 0.7

chatbot_model_save_path="model/chatbot/seq2seq.model"
chatbot_optimizer_save_path="model/chatbot/optimizer.model"

beam_width=3
