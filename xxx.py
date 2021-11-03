import re
from snownlp import sentiment
import pandas as pd
from snownlp import SnowNLP
#
# emotion = pd.read_csv('C:/Users/小志/Desktop/New folder/emotion2.csv')
# emotion['emotion'] = emotion['emotion'].astype(int)
#
# for i in range(len(emotion['post_content'])):
#     if emotion.loc[i, 'post_content'].partition('展开全文')[1] == '展开全文':
#         emotion.loc[i, 'post_content'] = emotion.loc[i, 'post_content'].partition('展开全文')[2]
#     else:
#         emotion.loc[i, 'post_content'] = emotion.loc[i, 'post_content']
#
# # Remove English words
# shit = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
# for i in range(len(emotion['post_content'])):
#     emotion.loc[i, 'post_content'] = re.sub(shit, '', emotion.loc[i, 'post_content'])

### Remove stopwords
# def load_stopword():
#     cn_stop = open('cn_stopwords.txt', encoding='utf-8')
#     sw = [line.strip() for line in cn_stop]
#     cn_stop.close()
#     return sw
#
#
# cn_stop = load_stopword()
#
#
# def cut_words(mytext):
#     return " ".join(jieba.cut(mytext))
#
#
# emotion['cut_content'] = emotion.post_content.apply(cut_words)
#
# emotion['cut_content'] = emotion['cut_content'].apply(lambda x: [item for item in x if item not in cn_stop])


### Train Snownlp
# sentiment.train('negative.txt', 'positive.txt')
# sentiment.save('sentiment.marshal')

def emotion_check(post_content):
    s = SnowNLP(post_content)
    if s.sentiments >= 0.75:
        return 1
    elif 0.2 <= s.sentiments < 0.75:
        return 0
    else:
        return -1


def emotion_index(post_content):
    s = SnowNLP(post_content)
    return s.sentiments


# emotion['emotion_index'] = emotion.post_content.apply(emotion_index)
# emotion['emotion_predict'] = emotion.post_content.apply(emotion_check)

### Choose threshold
# for i in np.logspace(0.4, 0.5, 10):
#     for n in np.logspace(0.5, 0.6, 10):
#         comb = []
#         if emotion['emotion_index'] >= i:
#             emotion['emotion_predict'] = 1
#         elif i <= emotion['emotion_index'] < n:
#             emotion['emotion_predict'] = 0
#         else:
#             emotion['emotion_predict'] = -1
#         accuracy = sum(emotion['emotion_predict'] == emotion['emotion']) / len(emotion['emotion_predict'])
#         comb = comb.append(i, n, accuracy)
#
# accuracy = sum(emotion['emotion_predict'] == emotion['emotion']) / len(emotion['emotion_predict'])
#
# print('Accuracy: ', accuracy)

