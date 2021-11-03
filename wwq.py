# import re
# import pandas as pd
# import pymysql
# from snownlp import SnowNLP
#
# from sqlalchemy import create_engine
#
# con = pymysql.connect(host='39.99.141.81',
#                       user='spider',
#                       password='Spider.774337!',
#                       database='spd_social')
#
# cursor = con.cursor()
# sql = """SELECT * FROM weibo_backup where crawl_date not like '2021-03%' limit 2000"""
#
# cursor.execute(sql)
# sina = cursor.fetchall()
# con.close()
#
# sina2 = pd.DataFrame(sina,
#                      columns=['id', 'user_id', 'user_name', 'user_age', 'user_sex', 'industry_type', 'friend_link',
#                               'user_head_url', 'user_country', 'user_follow', 'post_url', 'post_id', 'post_content',
#                               'post_topic', 'post_like_num', 'post_forward_num', 'post_comment_num', 'post_time',
#                               'search_keyword', 'user_tag', 'post_comment', 'user_info', 'platform_certification',
#                               'platform_source', 'post_user_url', 'crawl_date'])
#
# ### Drop id
# sina2 = sina2.drop(columns=['id'])
# sina2.to_csv('C:/Users/小志/Desktop/New folder/weibo_sample_data.csv',encoding='utf-8-sig')
#
#
# # ### Copy data
# # sina1 = sina2.copy(deep=True)
# #
# #
# # ### Remove duplicate post content
# # for i in range(len(sina1['post_content'])):
# #     if sina1.loc[i, 'post_content'].partition('展开全文')[1] == '展开全文':
# #         sina1.loc[i, 'post_content'] = sina1.loc[i, 'post_content'].partition('展开全文')[2]
# #     else:
# #         sina1.loc[i, 'post_content'] = sina1.loc[i, 'post_content']
# #
# #
# # ### Sentiment Analysis
# # # Remove English words
# # shit = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
# # for i in range(len(sina1['post_content'])):
# #     sina1.loc[i, 'post_content'] = re.sub(shit, '', sina1.loc[i, 'post_content'])
# #
# #
# # def emotion_check(post_content):
# #     s = SnowNLP(post_content)
# #     if s.sentiments >= 0.6:
# #         return 1
# #     elif 0.4 <= s.sentiments < 0.6:
# #         return 0
# #     else:
# #         return -1
# #
# #
# # def emotion_index(post_content):
# #     s = SnowNLP(post_content)
# #     return s.sentiments
# #
# #
# # sina1['emotion_index'] = sina1.post_content.apply(emotion_index)
# # sina1['emotion'] = sina1.post_content.apply(emotion_check)
#
# # # Change charset to utf8mb4
# # engine = create_engine(
# #     str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % ('root', 'Ss.768754763', '115.28.187.85',
# #                                                                      'bi_db'))
# # sina1.to_sql(name='social_media', con=engine, if_exists='append', index=False)
#
#
# # emotion = pd.read_csv('C:/Users/小志/Desktop/New folder/emotion2.csv')
# # emotion1 = pd.read_csv('C:/Users/小志/Desktop/New folder/emotion3.csv')
# #
# # negative = pd.concat([emotion[emotion['emotion'] == -1], emotion1[emotion1['emotion'] == -1]])
# # positive = pd.concat([emotion[emotion['emotion'] == 1], emotion1[emotion1['emotion'] == 1]])
# #
# # emotion2 = pd.concat([negative, positive])

from striprtf.striprtf import rtf_to_text
from io import StringIO
import pandas as pd
#
# with open('ymy.RRF', 'r',encoding='utf8') as file:
#     text = file.read()

# ymy = pd.DataFrame(text)
# ymy.to_csv('F:/social media/test/ymy.csv')

import pandas as pd
wwq = pd.read_excel("C:/Users/小志/Desktop/wwq.xlsx",sheet_name="Sheet1")