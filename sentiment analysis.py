import cv as cv
import re
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB as nb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd

# emotion = pd.read_csv('***.csv')
# emotion['emotion'] = emotion['emotion'].astype(int)

emotion1 = pd.read_csv('***.csv')
emotion2 = pd.read_csv('***.csv')

negative = pd.concat([emotion1[emotion1['emotion'] == -1], emotion2[emotion2['emotion'] == -1]])
positive = pd.concat([emotion1[emotion1['emotion'] == 1], emotion2[emotion2['emotion'] == 1]])

emotion = pd.concat([negative, positive])
emotion = emotion.reset_index(drop=True)

### Remove duplicate post content
for i in range(len(emotion['post_content'])):
    if emotion.loc[i, 'post_content'].partition('展开全文')[1] == '展开全文':
        emotion.loc[i, 'post_content'] = emotion.loc[i, 'post_content'].partition('展开全文')[2]
    else:
        emotion.loc[i, 'post_content'] = emotion.loc[i, 'post_content']

### Clean Text (can adjust)
# Remove Punctuation
punctuation = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'
emotion['post_content'] = emotion['post_content'].str.replace(punctuation, '')

# Remove English words
shit = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
for i in range(len(emotion['post_content'])):
    emotion.loc[i, 'post_content'] = re.sub(shit, '', emotion.loc[i, 'post_content'])


### Jieba cut words
def cut_words(mytext):
    return " ".join(jieba.cut(mytext))


emotion['cut_content'] = emotion.post_content.apply(cut_words)

### Prepare X_train, X_test, y_train, y_test
X = emotion['cut_content']
y = emotion.emotion

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)


### Stopwords for cn  
def load_stopword():
    cn_stop = open('cn_stopwords.txt', encoding='utf-8')
    sw = [line.strip() for line in cn_stop]
    cn_stop.close()
    return sw


cn_stop = load_stopword()

### Bad of words (or try td*idf)
# from sklearn.feature_extraction.text import TfidfVectorizer
vect = CountVectorizer(max_df=0.8,
                       min_df=3,
                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                       stop_words=frozenset(cn_stop))

### Check data structure
# test = pd.DataFrame(vect.fit_transform(X_train).toarray(), columns=vect.get_feature_names())
# test.head()

### Overfit

### Model training

train_data_features = vect.fit_transform(X_train)
# train_data_features = train_data_features.toarray()

model_NB = nb()
y_train = y_train.reset_index(drop=True)
model_NB.fit(train_data_features, y_train)

### Accuracy for training data
# Without Cross-validation
# train_score = model_NB.score(train_data_features, y_train)
# print(train_score)

# use cross_validation, cv =20
score = np.mean(cross_val_score(model_NB, train_data_features, y_train, cv=10, scoring='accuracy'))
print("Accuracy: ", score)

# sina2['post_content'] = sina2['post_content'].apply(lambda x: [item for item in x if item not in cn_stop])

# # Predict and accuracy for test data
# test_data_features = vect.transform(X_test)
# test_data_features = test_data_features.toarray()
# result = model_NB.score(test_data_features, y_test)
# print("Accuracy on test: ", result)

### Save model
# from sklearn.externals import joblib
#
# joblib.dump(model_NB, '***/model_NB.pkl')
#
# ###Load model
# model_NB = joblib.load('***/model_NB.pkl')

