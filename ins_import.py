import pandas as pd
import pyodbc
import pymysql
import csv
import numpy as np
from sqlalchemy import create_engine

con = pymysql.connect(host='39.99.141.81',
                      user='spider',
                      password='Spider.774337!',
                      database='spd_social')

cursor = con.cursor()
sql = """SELECT * FROM instagram_backup where post_time LIKE '2021-05-04%'"""

cursor.execute(sql)
ins = cursor.fetchall()
con.close()

ins2 = pd.DataFrame(ins,
                     columns=['id', 'user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
                              'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
                              'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
                              'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
                              'platform_source', 'post_user_url', 'crawl_date'])

### Drop id
ins2 = ins2.drop(columns=['id'])

# create CSV
#ins2.to_csv('F:/social media/test/weibo.csv',encoding='utf-8-sig')

### Unify Names
names = {'古驰': 'Gucci',
         '路易威登': 'Louis Vuitton',
         '芬迪': 'Fendi',
         '爱马仕': 'Hermes',
         'lv': 'Louis Vuitton',
         'louisvuitton': 'Louis Vuitton'}

for old, new in names.items():
    for i in ins2['search_keyword'].index:
        if ins2['search_keyword'][i] == old:
            ins2['search_keyword'][i] = new

ins2['search_keyword'] = ins2['search_keyword'].str.title()


### Remove Duplicate
columns = ['user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
           'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
           'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
           'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
           'platform_source', 'post_user_url', 'crawl_date']

dat1 = pd.DataFrame(columns=columns)
for i in np.unique(ins2['search_keyword']):
    rows = np.where(ins2['search_keyword'] == i)
    rows = rows[0].tolist()
    dat = ins2.iloc[rows,].drop_duplicates(subset=['post_id'])
    dat1 = dat1.append(dat, sort=False)

ins2 = dat1.copy(deep=True)

# ins2.groupby(['search_keyword']).count().iloc[:,1]

### Remove Punctuations
ins2['post_topic'] = ins2['post_topic'].str.replace('[^\w\s]', '')

### Lowercase
ins2["post_topic"] = ins2["post_topic"].str.lower()

# # Change charset to utf8mb4
engine = create_engine(
    str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % ('root', 'Ss.768754763', '115.28.187.85',
                                                                     'bi_db'))
ins2.to_sql(name='social_media', con=engine, if_exists='append', index=False)
ins2.to_sql(name='social_media_backup', con=engine, if_exists='append', index=False)