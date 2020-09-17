from prepar_corpus.prepar_user_dict.test_user_dict import test_user_dict
from lib import cut
from lib import stopwords
if __name__ == '__main__':
    t="python难不难，不是很难,哈，啊"
    print(cut(t,with_sg=False,use_stopwords=True))