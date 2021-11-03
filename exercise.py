import pandas as pd
import pymysql

con = pymysql.connect(host='***',
                      user='***',
                      password='***',
                      database='***')

cursor = con.cursor()
sql = """SELECT * FROM instagram_user limit 20"""

cursor.execute(sql)
ins_offcial = cursor.fetchall()
con.close()

ins_offcial2 = pd.DataFrame(ins_offcial,
                     columns=['id', 'user_name', 'post_count', 'user_follow', 'user_profile', 'post_id', 'post_url',
                              'post_content', 'post_topic', 'post_comment_num', 'post_like_num', 'posts_comment',
                              'crawl_date'])

ins_offcial2.to_csv('***',encoding='utf-8-sig')
