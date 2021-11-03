import re
import pandas as pd
import pyodbc
import pymysql
import csv
from datetime import datetime, timedelta
import numpy as np
from snownlp import SnowNLP

from sqlalchemy import create_engine

con = pymysql.connect(host='39.99.141.81',
                      user='spider',
                      password='Spider.774337!',
                      database='spd_social')

cursor = con.cursor()
sql = """SELECT * FROM weibo_backup where post_time like '2021-05-06%'"""

cursor.execute(sql)
sina = cursor.fetchall()
con.close()

sina2 = pd.DataFrame(sina,
                     columns=['id', 'user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
                              'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
                              'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
                              'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
                              'platform_source', 'post_user_url', 'crawl_date'])

### Drop id
sina2 = sina2.drop(columns=['id'])

# create CSV
# sina2.to_csv('F:/social media/test/weibo.csv',encoding='utf-8-sig')


### Copy data
sina1 = sina2.copy(deep=True)

### Remove duplicate post content
# for i in range(len(sina1['post_content'])):
#     if sina1.loc[i, 'post_content'].partition('展开全文')[1] == '展开全文':
#         sina1.loc[i, 'post_content'] = sina1.loc[i, 'post_content'].partition('展开全文')[2]
#     else:
#         sina1.loc[i, 'post_content'] = sina1.loc[i, 'post_content']

### Create posts release date
# sina1['crawl_date'] = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d') #Today
# sina1['crawl_date'] = pd.to_datetime(sina1['crawl_date']).dt.date

### Unify Names
names = {'古驰': 'Gucci',
         '路易威登': 'Louis Vuitton',
         '芬迪': 'Fendi',
         '爱马仕': 'Hermes'}

for old, new in names.items():
    for i in sina1['search_keyword'].index:
        if sina1['search_keyword'][i] == old:
            sina1['search_keyword'][i] = new

sina1['search_keyword'] = sina1['search_keyword'].str.title()

### Remove Duplicate
columns = ['user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
           'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
           'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
           'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
           'platform_source', 'post_user_url', 'crawl_date']

dat1 = pd.DataFrame(columns=columns)
for i in np.unique(sina1['search_keyword']):
    rows = np.where(sina1['search_keyword'] == i)
    rows = rows[0].tolist()
    dat = sina1.iloc[rows,].drop_duplicates(subset=['post_id'])
    dat1 = dat1.append(dat, sort=False)

sina1 = dat1.copy(deep=True)

### Remove Punctuations
sina1['post_topic'] = sina1['post_topic'].str.replace('[^\w\s]', '')

### Lowercase
sina1["post_topic"] = sina1["post_topic"].str.lower()

### Word Frequency
# sina1.post_topic.str.split(expand=True).stack().value_counts()


### Sentiment Analysis
# Remove English words
shit = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
for i in range(len(sina1['post_content'])):
    sina1.loc[i, 'post_content'] = re.sub(shit, '', sina1.loc[i, 'post_content'])


def emotion_check(post_content):
    s = SnowNLP(post_content)
    if s.sentiments >= 0.6:
        return 1
    elif 0.4 <= s.sentiments < 0.6:
        return 0
    else:
        return -1


def emotion_index(post_content):
    s = SnowNLP(post_content)
    return s.sentiments


sina1['emotion_index'] = sina1.post_content.apply(emotion_index)
sina1['emotion'] = sina1.post_content.apply(emotion_check)

# # Change charset to utf8mb4
engine = create_engine(
    str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % ('root', 'Ss.768754763', '115.28.187.85',
                                                                     'bi_db'))
sina1.to_sql(name='social_media', con=engine, if_exists='append', index=False)
sina1.to_sql(name='social_media_backup', con=engine, if_exists='append', index=False)
