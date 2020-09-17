import fasttext
import config
def build_classify_model():
    model=fasttext.train_supervised(config.classify_corpus_path,epoch=20,wordNgrams=2,minCount=1)
    model.save_model(config.classify_model_path)

def get_classify_model():
    """
    加载model
    :return:
    """
    model=fasttext.load_model(config.classify_model_path)
    return model

#TODO 模型测试